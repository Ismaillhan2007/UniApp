# UniAPP

Django + React Full Stack App

## Setup Instructions

### Backend (Django)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend (React)
```bash
cd frontend
npm install
npm start
```

## API Endpoints
- `GET /api/hello/` - Test endpoint