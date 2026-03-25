def toggle_newsletter(request):
    value = request.GET.get("value", "1")
    request.session["newsletter"] = value == "1"
    return "ok"
