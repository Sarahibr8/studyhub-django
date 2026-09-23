from django.http import Http404
from django.shortcuts import redirect, render

from .forms import FeedbackForm

RESOURCES = [
    {"id": 1, "title": "Django URL Dispatcher Guide", "type": "Article", "description": "How Django matches a URL to a view, including path converters and include().", "url": "https://docs.djangoproject.com/en/stable/topics/http/urls/"},
    {"id": 2, "title": "Django Templates Guide", "type": "Article", "description": "Template language basics: variables, tags, filters, and template inheritance.", "url": "https://docs.djangoproject.com/en/stable/topics/templates/"},
    {"id": 3, "title": "Django Sessions Guide", "type": "Article", "description": "How Django stores per-visitor data in request.session between requests.", "url": "https://docs.djangoproject.com/en/stable/topics/http/sessions/"},
    {"id": 4, "title": "Working with Django Forms", "type": "Article", "description": "Form classes, validation, cleaned_data, and displaying errors.", "url": "https://docs.djangoproject.com/en/stable/topics/forms/"},
    {"id": 5, "title": "Django Tutorial Videos", "type": "Video", "description": "A YouTube search for beginner-friendly Django video tutorials.", "url": "https://www.youtube.com/results?search_query=django+tutorial"},
    {"id": 6, "title": "Django Official Website", "type": "External Link", "description": "The home of the Django web framework: news, downloads, and community links.", "url": "https://www.djangoproject.com/"},
]

THEMES = ["light", "dark"]
DEFAULT_THEME = "light"
THEME_COOKIE_MAX_AGE = 60 * 60 * 24 * 365


def get_theme(request):
    theme = request.COOKIES.get("theme", DEFAULT_THEME)
    return theme if theme in THEMES else DEFAULT_THEME


def get_favorite_ids(request):
    return request.session.get("favorites", [])


def find_resource(resource_id):
    for resource in RESOURCES:
        if resource["id"] == resource_id:
            return resource
    return None


def home(request):
    return render(request, "core/home.html", {"theme": get_theme(request)})


def resource_list(request):
    return render(request, "core/resource_list.html", {
        "theme": get_theme(request),
        "resources": RESOURCES,
        "favorite_ids": get_favorite_ids(request),
    })


def resource_detail(request, id):
    resource = find_resource(id)
    if resource is None:
        return custom_404(request, None)

    tab = request.GET.get("tab", "overview")
    if tab not in ("overview", "details"):
        tab = "overview"

    return render(request, "core/resource_detail.html", {
        "theme": get_theme(request),
        "resource": resource,
        "tab": tab,
        "is_favorite": id in get_favorite_ids(request),
    })


def favorites(request):
    favorite_ids = get_favorite_ids(request)

    if request.method == "POST":
        action = request.POST.get("action")
        try:
            resource_id = int(request.POST.get("resource_id", ""))
        except ValueError:
            raise Http404("Resource not found")

        if find_resource(resource_id) is None:
            raise Http404("Resource not found")

        if action == "add" and resource_id not in favorite_ids:
            favorite_ids.append(resource_id)
        elif action == "remove" and resource_id in favorite_ids:
            favorite_ids.remove(resource_id)

        request.session["favorites"] = favorite_ids
        return redirect("favorites")

    favorite_resources = [
        resource for resource_id in favorite_ids
        if (resource := find_resource(resource_id)) is not None
    ]
    return render(request, "core/favorites.html", {
        "theme": get_theme(request),
        "favorite_resources": favorite_resources,
    })


def preferences(request):
    if request.method == "POST":
        selected = request.POST.get("theme")
        response = redirect("preferences")
        if selected in THEMES:
            response.set_cookie("theme", selected, max_age=THEME_COOKIE_MAX_AGE)
        return response

    return render(request, "core/preferences.html", {
        "theme": get_theme(request),
        "themes": THEMES,
    })


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            request.session["feedback_name"] = form.cleaned_data["name"]
            return redirect("feedback_thanks")
    else:
        form = FeedbackForm()

    return render(request, "core/feedback.html", {
        "theme": get_theme(request),
        "form": form,
    })


def feedback_thanks(request):
    return render(request, "core/feedback_thanks.html", {
        "theme": get_theme(request),
        "name": request.session.pop("feedback_name", None),
    })


def custom_404(request, exception=None, invalid_path=None):
    return render(request, "404.html", {"theme": get_theme(request)}, status=404)
