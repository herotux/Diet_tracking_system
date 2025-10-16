# Diet & Fitness Tracking System

This is a full-stack system for personalized diet and fitness programs prescribed by doctors for patients.

## Components

-   **Backend:** A Django application providing a RESTful API.
-   **Flutter App:** A mobile app for patients to view their plans and track progress.
-   **Telegram Bot:** A bot for patients to interact with the system via Telegram.

## Setup

For detailed setup instructions, please refer to the `README.md` file within each component's directory:

-   [Backend README](./backend/README.md)
-   [Flutter App README](./flutter_app/README.md)
-   [Telegram Bot README](./telegram_bot/README.md)

## API Documentation

The API documentation is available at `http://localhost:8000/api/schema/swagger-ui/` after starting the backend.
A summary is also available in [docs/API_DOCUMENTATION.md](./docs/API_DOCUMENTATION.md).

## CI/CD

The project includes a GitHub Actions workflow to build and test the backend and the Android app. See [.github/workflows/android_build.yml](./.github/workflows/android_build.yml) for details.