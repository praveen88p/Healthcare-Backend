# Healthcare Backend API 🚑

This is a Django REST framework-based backend for a healthcare application, featuring authentication, user registration, and patient/doctor management.

## Features 🚀
- JWT-based authentication using `SimpleJWT`
- User registration & login
- Patient & doctor management
- PostgreSQL database integration
- RESTful API endpoints

## Tech Stack 🛠️
- **Django** (Backend Framework)
- **Django REST Framework (DRF)** (API)
- **PostgreSQL** (Database)
- **SimpleJWT** (Authentication)

## Setup Instructions 🏗️

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/healthcare-backend.git
cd healthcare-backend
```
### 2. Create a Virtual Environment
```bash
python -m venv healthcare-env
source healthcare-env/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables
```bash
Create a .env file in the root directory and add:
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Apply Migrations
```bash
cd healthcare then run
python manage.py makemigrations
python manage.py migrate
```
### 7. Run the Server
```bash
python manage.py runserver
```

## 📡 API Endpoints  

### 🔑 Authentication  
- **Register:** `POST /api/auth/register/`  
- **Login:** `POST /api/auth/login/`  

### 👨‍⚕️ Patients  
- **List Patients:** `GET /api/patients/`  
- **Create Patient:** `POST /api/patients/`  
- **Retrieve Patient:** `GET /api/patients/{id}/`  

### 🩺 Doctors  
- **List Doctors:** `GET /api/doctors/`  
- **Create Doctor:** `POST /api/doctors/`  
- **Retrieve Doctor:** `GET /api/doctors/{id}/`  

---

## 🔐 Authentication  

The API uses **JWT tokens** for authentication.  
Include the `Authorization` header with the **Bearer Token** in your requests:  

```http
Authorization: Bearer your_access_token



