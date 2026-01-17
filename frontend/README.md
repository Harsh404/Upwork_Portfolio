# Portfolio Frontend

React TypeScript frontend for the portfolio website.

## Features

- Responsive design with Tailwind CSS
- User authentication with JWT tokens
- Protected routes for authenticated content
- API integration with FastAPI backend
- Automatic token refresh

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Set up environment variables in `.env`:
   ```
   VITE_API_BASE_URL=http://localhost:8000
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Project Structure

```
src/
├── components/       # Reusable components
├── contexts/         # React contexts (Auth)
├── pages/           # Page components
├── App.tsx          # Main app component
├── main.tsx         # Entry point
└── index.css        # Global styles
```