from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.feed, name="feed"),
    path("csp-lab/", views.csp_lab, name="csp_lab"),
    path("origin/receiver/", views.origin_receiver, name="origin_receiver"),
    path("origin/sender/", views.origin_sender, name="origin_sender"),
    path("api/profile-export/", views.api_profile_export, name="api_profile_export"),
    path("attack-lab/", views.attack_lab, name="attack_lab"),
    path("account/email-optin/", views.account_email_optin, name="account_email_optin"),
    path("api/session-preferences/", views.api_session_preferences, name="api_session_preferences"),
    path("db-lab/", views.db_lab, name="db_lab"),
    path("db-lab/post-export/", views.db_post_export, name="db_post_export"),
    path("server-lab/", views.server_lab, name="server_lab"),
    path("server-lab/ping/", views.server_ping, name="server_ping"),
    path("server-lab/file-view/", views.server_file_view, name="server_file_view"),
    path("infra-lab/", views.infra_lab, name="infra_lab"),
    path("infra-lab/header-audit/", views.infra_header_audit, name="infra_header_audit"),
    path("infra-lab/config-diag/", views.infra_config_diag, name="infra_config_diag"),
    path("integrated-lab/", views.integrated_lab, name="integrated_lab"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("post/<int:post_id>/comment/", views.add_comment, name="add_comment"),
    path("u/<str:username>/", views.profile, name="profile"),
    path("notes/", views.private_notes, name="private_notes"),
]
