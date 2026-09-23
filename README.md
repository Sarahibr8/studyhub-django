# StudyHub

A Django learning resources portal demonstrating routing, views, templates, forms, sessions, cookies, validation, redirects, custom 404 handling, and responsive UI.

## Features

- Browse learning resources
- View resource details with query parameters
- Add and remove favorites using Django sessions
- Light and dark theme preferences using cookies
- Feedback form with server-side validation
- Post/Redirect/Get after successful feedback
- Custom 404 page
- Responsive UI with CSS Grid and Flexbox
- CSS transitions and animations

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
| Redirects | Post/Redirect/Get |
| CSRF | Protected POST forms |
| Error Handling | Custom 404 page |

## Main Routes

- `/` — Home
- `/resources/` — Resource list
- `/resources/<int:id>/` — Resource details
- `/favorites/` — Favorites
- `/preferences/` — Theme preferences
- `/feedback/` — Feedback form
- `/feedback/thanks/` — Successful submission

## Technologies

- Python
- Django
- HTML5
- CSS3
- Django Templates
- SQLite for Django's built-in session system

## Project Structure

```text
studyhub-django/
├── core/
│   ├── templates/core/
│   ├── apps.py
│   ├── forms.py
│   ├── urls.py
│   └── views.py
├── static/
│   ├── css/
│   └── images/
├── templates/
│   ├── 404.html
│   └── base.html
├── screenshots/
├── media/
├── studyhub_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Running Locally

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install Django:

```bash
pip install django
```

Apply migrations and run:

```bash
python manage.py migrate
python manage.py runserver
```

## Current Limitations

- Resources are currently predefined Python data rather than database models.
- Favorites are session-based rather than linked to user accounts.
- Feedback is validated but not stored permanently.
- Theme preferences are stored in a browser cookie.

## Future Development

- Add database models for resources
- Add authentication and user accounts
- Persist favorites per user
- Store feedback submissions
- Add search and filtering
- Add automated tests
- Prepare the project for deployment
- Continue improving accessibility and responsive behavior

## Author

**Sarah Alsubaie**

GitHub: https://github.com/Sarahibr8  
LinkedIn: https://www.linkedin.com/in/sarah-alsubaie-a41199217/
