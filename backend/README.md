# Backend

This is the Django backend for the Diet & Fitness Tracking System.

## Setup

1.  Create a `.env` file from the `.env.example` and fill in the values.
2.  Run `docker-compose up --build`.

The API will be available at `http://localhost:8000/api/`.
The admin panel will be at `http://localhost:8000/admin/`.
The API documentation will be at `http://localhost:8000/api/schema/swagger-ui/`.

## Internationalization

To work with translations:

1.  Make changes to the translatable strings in the code.
2.  Run `docker-compose exec backend python manage.py makemessages -l <lang_code>` (e.g., `fa`, `en`, `ku`).
3.  Edit the `.po` files in the `locale` directory.
4.  Run `docker-compose exec backend python manage.py compilemessages`.