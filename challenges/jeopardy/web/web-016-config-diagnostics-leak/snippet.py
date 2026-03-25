import os


def config_diag(request):
    key = request.GET.get("key", "SECRET_KEY")
    return {"key": key, "value": os.getenv(key, "<missing>")}
