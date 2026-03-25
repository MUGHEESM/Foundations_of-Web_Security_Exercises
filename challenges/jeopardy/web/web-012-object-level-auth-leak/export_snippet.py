def export_posts(request):
    author = request.GET.get("author")
    posts = Post.objects.filter(author__username=author)
    return [{"id": p.id, "body": p.body} for p in posts]
