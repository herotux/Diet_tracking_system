# API Documentation

This document provides a summary of the API endpoints. For full, interactive documentation, visit `/api/schema/swagger-ui/` once the backend is running.

## Authentication

-   `POST /api/auth/register/`: Register a new user.
-   `POST /api/auth/login/`: Obtain a JWT token pair for authentication.
-   `POST /api/auth/token/refresh/`: Refresh an expired access token.

## Programs

-   `GET /api/programs/`: List programs (for doctors, their created programs; for patients, their assigned programs).
-   `POST /api/programs/`: Create a new program (doctors only).
-   `GET /api/programs/{id}/`: Retrieve a specific program.
-   `PUT/PATCH /api/programs/{id}/`: Update a program (doctors only).
-   `DELETE /api/programs/{id}/`: Delete a program (doctors only).

## Progress

-   `GET /api/progress/`: List all progress entries for the authenticated patient.
-   `POST /api/progress/`: Submit a new progress entry for a task.
-   `GET /api/progress/{program_id}/summary/`: Get a summary of patient progress for a specific program (doctors only).

## Internationalization

-   `GET /api/i18n/languages/`: Get a list of supported languages.