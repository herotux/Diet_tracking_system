import logging
import os
import requests
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

API_BASE = os.environ.get("API_BASE", "http://localhost:8000")
BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

# Load translations
with open('messages.json', 'r', encoding='utf-8') as f:
    MESSAGES = json.load(f)

# In-memory store for chat sessions; in production, use Redis or a database
CHAT_SESSIONS = {}  # chat_id -> {"user_id":..., "jwt":..., "lang": "en"}

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def get_text(key, lang):
    return MESSAGES.get(lang, {}).get(key, f"Missing translation for {key}")

def api_headers(chat_id):
    sess = CHAT_SESSIONS.get(chat_id, {})
    headers = {"Accept": "application/json", "Accept-Language": sess.get("lang", "en")}
    if sess.get("jwt"):
        headers["Authorization"] = f"Bearer {sess['jwt']}"
    return headers

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    CHAT_SESSIONS.setdefault(chat_id, {"lang": "en"})
    lang = CHAT_SESSIONS[chat_id]["lang"]
    await update.message.reply_text(get_text("start", lang))

async def setlang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    args = context.args
    if not args or args[0] not in ("fa", "en", "ku"):
        await update.message.reply_text("Usage: /setlang fa|en|ku")
        return
    CHAT_SESSIONS.setdefault(chat_id, {})["lang"] = args[0]
    await update.message.reply_text(f"Language set to {args[0]}")

async def link_account(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    username = context.args[0]
    password = context.args[1]
    try:
        r = requests.post(f"{API_BASE}/api/auth/login/", json={"username": username, "password": password})
        r.raise_for_status()
        data = r.json()
        CHAT_SESSIONS[chat_id]["jwt"] = data["access"]
        await update.message.reply_text(get_text("link_success", CHAT_SESSIONS[chat_id]["lang"]))
    except requests.HTTPError:
        await update.message.reply_text(get_text("link_fail", CHAT_SESSIONS[chat_id]["lang"]))

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    headers = api_headers(chat_id)
    if "Authorization" not in headers:
        await update.message.reply_text(get_text("not_linked", CHAT_SESSIONS[chat_id]["lang"]))
        return
    try:
        # Assuming the first program is the active one
        r_programs = requests.get(f"{API_BASE}/api/programs/", headers=headers)
        r_programs.raise_for_status()
        programs = r_programs.json()
        if not programs:
            await update.message.reply_text(get_text("no_programs", CHAT_SESSIONS[chat_id]["lang"]))
            return

        active_program = programs[0]
        today_dow = datetime.datetime.today().isoweekday()
        today_tasks = [t for t in active_program['tasks'] if t['day_of_week'] == today_dow]

        if not today_tasks:
            await update.message.reply_text(get_text("no_tasks_today", CHAT_SESSIONS[chat_id]["lang"]))
            return

        msg_lines = [get_text("today_header", CHAT_SESSIONS[chat_id]["lang"])]
        for task in today_tasks:
            msg_lines.append(f"• {task['name']} (`/complete {task['id']}`)")
        await update.message.reply_text("\n".join(msg_lines), parse_mode='Markdown')

    except Exception as e:
        logger.error(f"Error fetching today's plan: {e}")
        await update.message.reply_text(get_text("fetch_fail", CHAT_SESSIONS[chat_id]["lang"]))

async def complete_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    lang = CHAT_SESSIONS[chat_id]["lang"]
    headers = api_headers(chat_id)
    if "Authorization" not in headers:
        await update.message.reply_text(get_text("not_linked", lang))
        return

    args = context.args
    if len(args) < 2 or args[1] not in ['COMPLETED', 'PARTIALLY_COMPLETED', 'NOT_COMPLETED']:
        await update.message.reply_text(get_text("complete_usage", lang))
        return

    task_id = args[0]
    status = args[1]
    note = " ".join(args[2:]) if len(args) > 2 else ""
    payload = {"task": task_id, "status": status, "note": note}

    try:
        r = requests.post(f"{API_BASE}/api/progress/", json=payload, headers=headers)
        r.raise_for_status()
        await update.message.reply_text(get_text("update_success", lang))
    except Exception as e:
        logger.error(f"Failed to update item: {e}")
        await update.message.reply_text(get_text("update_fail", lang))

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setlang", setlang))
    app.add_handler(CommandHandler("link", link_account))
    app.add_handler(CommandHandler("today", today))
    app.add_handler(CommandHandler("complete", complete_command))

    logger.info("Bot started")
    app.run_polling()

import datetime

if __name__ == "__main__":
    main()