# URL Shortener

A Django-based web application that allows users to shorten long URLs, redirect to original URLs using short codes, and manage their shortened URLs with user authentication. The project includes a modern frontend styled with Tailwind CSS and dynamic client-side validation for a better user experience.

## Features

- **URL Shortening**: Convert long URLs into short links (e.g., `http://127.0.0.1:8000/abc123`).
- **User Authentication**: Sign up, log in, and log out to manage shortened URLs.
- **Recent URLs**: Logged-in users can view their 10 most recent shortened URLs on the homepage.
- **Dynamic Validation**: Client-side validation for signup (username, password length, password match) and login (non-empty fields) with error messages displayed on the page.
- **Responsive Design**: Clean, modern UI using Tailwind CSS, optimized for mobile and desktop.
- **Database**: Uses PostgreSQL for persistent storage, suitable for local and cloud deployment.

## Project Structure

```
urlshortener/
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── urlshortener/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── shortener/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── templates/
│   │   ├── shortener/
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── login.html
│   │   │   ├── signup.html
```

- `urlshortener/`: Project settings and configuration.
- `shortener/`: Main app containing models, views, and templates.
- `requirements.txt`: Lists dependencies (Django, psycopg2-binary, etc.).
- `Procfile` and `runtime.txt`: For deployment to Heroku/Render.

## Prerequisites

- **Python**: 3.12.3 (specified in `runtime.txt`).
- **PostgreSQL Database**: A cloud-hosted database
- **Git**: For version control and deployment.
- **Heroku CLI** or **Render account**: For deployment (optional).

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd urlshortener
```

### 2. Install Dependencies
Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Set up a `.env` file in the project root or configure environment variables:
```bash
DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<dbname>
SECRET_KEY=<your-secret-key>
```
- Obtain `DATABASE_URL` from a PostgreSQL provider like ElephantSQL.
- Generate a secure `SECRET_KEY` (e.g., using `django.core.management.utils.get_random_secret_key()`).

Update `urlshortener/settings.py` if not already configured:
```python
import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['*']  # Update for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### 4. Apply Migrations
Initialize the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)
For admin access (`/admin/`):
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
Start the server:
```bash
python manage.py runserver
```
Access the app at `http://127.0.0.1:8000/`.

## Usage

- **Homepage (`/`)**:
  - Shorten URLs by entering a long URL and clicking "Shorten".
  - Logged-in users see their 10 most recent shortened URLs.
  - Links to signup (`/signup/`) and login (`/login/`) for unauthenticated users.
- **Signup (`/signup/`)**:
  - Create an account with a username and password (minimum 8 characters).
  - Dynamic validation ensures passwords match and meet requirements.
- **Login (`/login/`)**:
  - Log in with username and password.
  - Dynamic validation ensures fields are not empty.
- **Shortened URLs**:
  - Access via `http://<domain>/<short_code>/` (e.g., `/abc123/`).
  - Redirects to the original long URL.
- **Logout (`/logout/`)**:
  - Logs out and redirects to the homepage.

## Deployment

### Heroku
1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
2. Log in: `heroku login`
3. Create an app: `heroku create your-app-name`
4. Set environment variables:
   ```bash
   heroku config:set DATABASE_URL=<your-elephantsql-url>
   heroku config:set SECRET_KEY=<your-secret-key>
   ```
5. Deploy:
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   heroku run python manage.py migrate
   ```
6. Open: `heroku open`

### Render
1. Push code to a GitHub repository.
2. Sign up at https://render.com and create a new Web Service.
3. Connect your GitHub repo.
4. Configure:
   - Runtime: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn urlshortener.wsgi`
   - Environment Variables: `DATABASE_URL`, `SECRET_KEY`, `PYTHON_VERSION=3.12.3`
5. Deploy and access at `https://your-app.onrender.com`.


## Troubleshooting

- **Unresolved Reference in PyCharm**: Invalidate caches (`File > Invalidate Caches / Restart`).
- **Template Not Found**: Ensure templates are in `shortener/templates/shortener/`.
- **Database Errors**: Verify `DATABASE_URL` and run migrations.
- **Validation Issues**: Check browser console for JavaScript errors; ensure Tailwind CDN loads.

## Future Improvements
- Add URL validation (e.g., check if URL is reachable).
- Implement password reset functionality.
- Compile Tailwind CSS locally for better performance.
- Add analytics for URL click tracking.

## License
MIT License. Feel free to use and modify this project.
