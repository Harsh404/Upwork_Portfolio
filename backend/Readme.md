# Portfolio Backend

A FastAPI backend for a portfolio website with user authentication, blog management, contact forms, and admin panel.

## Features

- **User Authentication**: Register, login, JWT tokens
- **Projects**: Showcase portfolio projects
- **Blogs**: Technical blogs accessible to logged-in users
- **Contact Form**: Public contact submissions
- **Products/Services**: Manage offerings
- **Media**: File management
- **Admin Panel**: Full CRUD operations for admins

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables in `.env`:
   ```
   MONGO_URI=mongodb://localhost:27017
   DATABASE_NAME=portfolio_db
   SECRET_KEY=your-secret-key-here
   ACCESS_TOKEN_EXPIRE_MINUTES=60
   REFRESH_TOKEN_EXPIRE_DAYS=7
   ```

3. Start MongoDB locally or update MONGO_URI.

4. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Bootstrap admin user:
   POST to `/api/v1/auth/bootstrap-admin` with user data.

## Authentication

- Access tokens expire after `ACCESS_TOKEN_EXPIRE_MINUTES` (default 60 minutes)
- Refresh tokens expire after `REFRESH_TOKEN_EXPIRE_DAYS` (default 7 days)
- When access token expires, use the refresh endpoint to get new tokens
- Tokens are rotated on refresh for security

## API Endpoints

- **Auth**: `/api/v1/auth/`
  - POST `/register` - User registration
  - POST `/login` - User login (returns access_token and refresh_token)
  - POST `/refresh` - Refresh access token using refresh_token
  - POST `/bootstrap-admin` - Create first admin

- **Projects**: `/api/v1/projects/` (Public read, Admin CRUD)
- **Blogs**: `/api/v1/blogs/` (Authenticated read, Admin CRUD)
- **Contacts**: `/api/v1/contacts/` (Public submit, Admin view/delete)
- **Products**: `/api/v1/products/` (Public read, Admin CRUD)
- **Services**: `/api/v1/services/` (Public read, Admin CRUD)
- **Media**: `/api/v1/media/` (Public read, Admin CRUD)

## Database

Uses MongoDB with collections for users, projects, blogs, contacts, products, services, media.
