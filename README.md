# Portfolio Website

A full-stack portfolio website with React TypeScript frontend and FastAPI backend, featuring user authentication, blog management, contact forms, and admin panel.

## Project Structure

```
portfolio/
├── backend/          # FastAPI backend
├── frontend/         # React TypeScript frontend
└── README.md         # This file
```

## Backend (FastAPI)

### Features

- **User Authentication**: Register, login, JWT tokens with refresh
- **Projects**: Showcase portfolio projects
- **Blogs**: Technical blogs accessible to logged-in users
- **Contact Form**: Public contact submissions
- **Products/Services**: Manage offerings
- **Media**: File management
- **Admin Panel**: Full CRUD operations for admins

### Setup

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in `backend/.env`:
   ```
   MONGO_URI=mongodb://localhost:27017
   DATABASE_NAME=portfolio_db
   SECRET_KEY=your-secret-key-here
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   REFRESH_TOKEN_EXPIRE_DAYS=7
   ```

4. Start MongoDB locally or update MONGO_URI.

5. Run the backend:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Bootstrap admin user:
   POST to `/api/v1/auth/bootstrap-admin` with user data.

### Authentication

- Access tokens expire after `ACCESS_TOKEN_EXPIRE_MINUTES` (default 30 minutes)
- Refresh tokens expire after `REFRESH_TOKEN_EXPIRE_DAYS` (default 7 days)
- When access token expires, use the refresh endpoint to get new tokens
- Tokens are rotated on refresh for security

### API Endpoints

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

### Database

Uses MongoDB with collections for users, projects, blogs, contacts, products, services, media.

## Frontend (React TypeScript)

### Features

- **Responsive Design**: Built with Tailwind CSS
- **Authentication**: Login, register, token management
- **Routing**: React Router for navigation
- **State Management**: Context API for auth state
- **API Integration**: Axios for backend communication
- **Protected Routes**: Route protection based on auth status

### Setup

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables in `frontend/.env`:
   ```
   VITE_API_BASE_URL=http://localhost:8000
   ```

4. Run the frontend:
   ```bash
   npm run dev
   ```

### Pages

- **Home**: Welcome page with overview
- **Projects**: Display portfolio projects
- **Blogs**: Technical blogs (authenticated users only)
- **Contact**: Contact form
- **Login/Register**: Authentication pages
- **Admin Dashboard**: Admin panel (admin users only)

## Running the Full Application

1. Start the backend:
   ```bash
   cd backend && uvicorn app.main:app --reload
   ```

2. Start the frontend:
   ```bash
   cd frontend && npm run dev
   ```

3. Open http://localhost:3000 in your browser

## Technologies Used

### Backend
- FastAPI
- MongoDB with Motor
- JWT for authentication
- Pydantic for data validation

### Frontend
- React 18 with TypeScript
- Vite for build tooling
- Tailwind CSS for styling
- React Router for routing
- Axios for HTTP requests
- JWT decode for token handling

## Development

- Backend API docs available at http://localhost:8000/docs
- Frontend uses hot reload for development
- CORS configured for local development