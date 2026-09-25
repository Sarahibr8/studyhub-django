# StudyHub

A Django learning resources portal built to demonstrate practical backend development with Django, including routing, views, templates, forms, sessions, cookies, authentication, validation, and responsive UI.

## Live Demo

🌐 **[StudyHub Live Demo](https://studyhub-production-6f03.up.railway.app)**

## Highlights

- Django URL routing and function-based views
- Reusable templates with template inheritance
- Django Forms with server-side validation
- User authentication with Sign Up, Login, and Logout
- Login-protected Favorites, Preferences, and Feedback
- Session-based favorites
- Cookie-based light/dark theme preferences
- CSRF-protected POST forms
- Custom 404 page
- Responsive UI with CSS Grid and Flexbox
- WhiteNoise static-file serving for deployment
- Automated Django tests
- Railway deployment with Docker


## Django Concepts

| Concept | Implementation |
|---|---|
| URL Routing | Project and app URL configuration |
| Path Converters | `/resources/<int:id>/` |
| Query Parameters | Resource detail tabs |
| Views | Function-based Django views |
| Templates | Django Template Language and inheritance |
| Static Files | CSS and images |
| Cookies | Theme preference |
| Sessions | Favorites and temporary feedback data |
| Forms | `FeedbackForm` |
| Validation | Built-in and custom validation |
| Authentication | Django user authentication |
| Access Control | Login-required views |
| Redirects | Post/Redirect/Get |
| CSRF | Protected POST forms |
| Error Handling | Custom 404 page |

## Main Routes

- `/` — Home
- `/resources/` — Resource list
- `/resources/<int:id>/` — Resource details
- `/signup/` — Create an account
- `/login/` — Login
- `/logout/` — Logout
- `/favorites/` — Favorites
- `/preferences/` — Theme preferences
- `/feedback/` — Feedback form
- `/feedback/thanks/` — Successful submission

## Technologies

- Python
- Django
- HTML
- CSS
- Django Templates
- SQLite — used for database-backed authentication and sessions
- WhiteNoise
- Gunicorn
- Docker
- Railway

## Testing

The project includes automated tests covering:

- Public page rendering
- Resource details and custom 404 handling
- Favorites add/remove behavior
- Theme preference changes
- Feedback validation and redirect flow
- User registration and login
- Login protection for private pages

Tests run automatically during the Docker image build.

Run them locally with:

```bash
python manage.py test
```

## Project Structure

```text
studyhub-django/
├── .github/
│   └── assets/
├── core/
│   ├── templates/core/
│   ├── templates/registration/
│   ├── apps.py
│   ├── forms.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
│   ├── css/
│   └── images/
├── templates/
│   ├── 404.html
│   └── base.html
├── media/
├── studyhub_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── Dockerfile
├── manage.py
├── requirements.txt
└── README.md
```

## Running Locally

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations and run:

```bash
python manage.py migrate
python manage.py runserver
```

For local development, set:

```text
DJANGO_DEBUG=True
```

For deployment, use a strong `DJANGO_SECRET_KEY`, set `DJANGO_DEBUG=False`, and configure `DJANGO_ALLOWED_HOSTS`.

## Current Limitations

- Resources are currently predefined Python data rather than database models.
- Favorites are session-based rather than permanently linked to user accounts.
- Feedback is validated but not stored permanently.
- Theme preferences are stored in a browser cookie.

## Future Development

- Add database models for learning resources
- Persist favorites per user
- Store feedback submissions
- Add search and filtering
- Expand the authentication flow with password reset
- Continue improving accessibility and responsive behavior

## Author

**Sarah Alsubaie**

- GitHub: https://github.com/Sarahibr8
- LinkedIn: https://www.linkedin.com/in/sarah-alsubaie-a41199217/
