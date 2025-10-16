# Setup Guide

This guide provides instructions for setting up all components of the Diet & Fitness Tracking System.

## Backend

The backend is a Dockerized Django application.

1.  Navigate to the `backend` directory.
2.  Create a `.env` file from the `.env.example` and provide the necessary values.
3.  Run `docker-compose up --build`.

The backend will be available at `http://localhost:8000`.

## Flutter App

The mobile app is built with Flutter.

1.  Ensure you have the Flutter SDK installed.
2.  Navigate to the `flutter_app` directory.
3.  Run `flutter pub get` to install dependencies.
4.  Run `flutter run` to launch the app on an emulator or a connected device.

## Telegram Bot

The Telegram bot is a Python application.

1.  Navigate to the `telegram_bot` directory.
2.  Create a `.env` file from the `.env.example` and add your Telegram bot token.
3.  Install dependencies: `pip install -r requirements.txt`.
4.  Run the bot: `python bot.py`.