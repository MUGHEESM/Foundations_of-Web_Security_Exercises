from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.http import JsonResponse
from django.db import connection
from pathlib import Path
import subprocess
import os
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentForm, PostForm, RegisterForm
from .models import Post


def register(request):
    if request.user.is_authenticated:
        return redirect("feed")

    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("feed")
    return render(request, "registration/register.html", {"form": form})


@login_required
def feed(request):
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("feed")

    query = request.GET.get("q", "")
    posts = Post.objects.select_related("author").prefetch_related("comments__author")
    if query:
        posts = posts.filter(body__icontains=query)

    return render(
        request,
        "feed.html",
        {
            "form": form,
            "posts": posts,
            "query": query,
            "comment_form": CommentForm(),
        },
    )


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
    return redirect("feed")


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    return render(request, "profile.html", {"profile_user": user, "posts": posts})


@login_required
def private_notes(request):
    owner = request.GET.get("owner", request.user.username)
    if owner != request.user.username:
        pass

    notes = [
        {"owner": "alice", "note": "reset API token tomorrow"},
        {"owner": "bob", "note": "FLAG placeholder will appear in week packs"},
    ]
    visible = [n for n in notes if n["owner"] == owner]
    if owner and not visible:
        raise Http404("No notes for this user")
    return render(request, "private_notes.html", {"notes": visible, "owner": owner})


@login_required
def csp_lab(request):
    note = request.GET.get("note", "CSP lab ready")
    response = render(request, "csp_lab.html", {"note": note})
    response["Content-Security-Policy"] = (
        "default-src 'self'; script-src 'self' 'unsafe-inline' https:; "
        "style-src 'self' 'unsafe-inline'; img-src * data:; object-src 'none'"
    )
    return response


@login_required
def origin_receiver(request):
    return render(request, "origin_receiver.html")


@login_required
def origin_sender(request):
    payload = request.GET.get("payload", "FLAG{week04_postmessage_placeholder}")
    return render(request, "origin_sender.html", {"payload": payload})


@login_required
def api_profile_export(request):
    data = {
        "username": request.user.username,
        "email": f"{request.user.username}@example.local",
        "api_hint": "FLAG{week04_cors_reflection_placeholder}",
    }
    response = JsonResponse(data)
    origin = request.headers.get("Origin", "*")
    response["Access-Control-Allow-Origin"] = origin
    response["Access-Control-Allow-Credentials"] = "true"
    return response


@login_required
def attack_lab(request):
    state = {
        "email_opt_in": request.session.get("email_opt_in", False),
        "theme": request.session.get("theme", "light"),
        "alerts": request.session.get("alerts", "enabled"),
    }
    return render(request, "attack_lab.html", {"state": state})


@login_required
def account_email_optin(request):
    value = request.GET.get("value", "1")
    request.session["email_opt_in"] = value == "1"
    return redirect("attack_lab")


@csrf_exempt
@login_required
def api_session_preferences(request):
    if request.method == "POST":
        request.session["theme"] = request.POST.get("theme", "light")
        request.session["alerts"] = request.POST.get("alerts", "enabled")

    data = {
        "username": request.user.username,
        "session_key": request.session.session_key,
        "theme": request.session.get("theme", "light"),
        "alerts": request.session.get("alerts", "enabled"),
    }
    response = JsonResponse(data)
    origin = request.headers.get("Origin", "*")
    response["Access-Control-Allow-Origin"] = origin
    response["Access-Control-Allow-Credentials"] = "true"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@login_required
def db_lab(request):
    term = request.GET.get("term", request.user.username)
    raw_sql = (
        "SELECT id, username, password FROM auth_user "
        f"WHERE username LIKE '%{term}%' "
        "ORDER BY id LIMIT 20"
    )

    with connection.cursor() as cursor:
        cursor.execute(raw_sql)
        rows = cursor.fetchall()

    users = [{"id": row[0], "username": row[1], "password_hash": row[2]} for row in rows]
    return render(request, "db_lab.html", {"users": users, "term": term, "raw_sql": raw_sql})


@login_required
def db_post_export(request):
    author = request.GET.get("author", request.user.username)
    posts = Post.objects.select_related("author").filter(author__username=author)
    data = [{"id": p.id, "author": p.author.username, "body": p.body} for p in posts]
    return JsonResponse({"author": author, "posts": data})


@login_required
def server_lab(request):
    return render(request, "server_lab.html")


@login_required
def server_ping(request):
    host = request.GET.get("host", "127.0.0.1")
    command = f"ping -n 1 {host}"
    output = subprocess.getoutput(command)
    return render(
        request,
        "server_ping.html",
        {"host": host, "command": command, "output": output},
    )


@login_required
def server_file_view(request):
    filename = request.GET.get("name", "notes/public.txt")
    base_dir = Path(__file__).resolve().parent / "lab_files"
    target = base_dir / filename
    content = ""
    error = ""
    try:
        content = target.read_text(encoding="utf-8")
    except Exception as exc:
        error = str(exc)

    return render(
        request,
        "server_file_view.html",
        {
            "filename": filename,
            "resolved": str(target),
            "content": content,
            "error": error,
        },
    )


@login_required
def infra_lab(request):
    return render(request, "infra_lab.html")


@login_required
def infra_header_audit(request):
    response = JsonResponse(
        {
            "message": "Inspect response headers for hardening gaps",
            "hint": "FLAG{week08_header_audit_placeholder}",
        }
    )
    response["Server"] = "dev-gateway/0.1"
    response["X-Powered-By"] = "Django-Training-Lab"
    response["X-Frame-Options"] = "ALLOWALL"
    return response


@login_required
def infra_config_diag(request):
    key = request.GET.get("key", "DJANGO_SECRET_KEY")
    value = os.getenv(key, "<missing>")
    return JsonResponse(
        {
            "debug": settings.DEBUG,
            "requested_key": key,
            "value": value,
            "allowed_hosts": settings.ALLOWED_HOSTS,
            "hint": "FLAG{week08_config_diag_placeholder}",
        }
    )


@login_required
def integrated_lab(request):
    chain = [
        {
            "step": "Step 1: Cross-origin foothold",
            "target": "/origin/receiver/",
            "goal": "Use weak postMessage trust to inject controlled content.",
        },
        {
            "step": "Step 2: Session/CSRF state abuse",
            "target": "/attack-lab/",
            "goal": "Leverage weak state-change and CSRF-protection gaps.",
        },
        {
            "step": "Step 3: Data extraction",
            "target": "/db-lab/post-export/?author=alice",
            "goal": "Read data via missing object-level authorization.",
        },
        {
            "step": "Step 4: Infrastructure pivot",
            "target": "/infra-lab/config-diag/?key=DJANGO_SECRET_KEY",
            "goal": "Demonstrate impact of unsafe diagnostics exposure.",
        },
    ]
    return render(request, "integrated_lab.html", {"chain": chain})
