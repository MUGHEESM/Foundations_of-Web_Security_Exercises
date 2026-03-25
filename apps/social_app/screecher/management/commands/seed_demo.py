from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from screecher.models import Comment, Post


class Command(BaseCommand):
    help = "Seed demo users, posts, and comments for practice labs"

    def handle(self, *args, **options):
        users = [
            ("alice", "alice12345"),
            ("bob", "bob12345"),
            ("charlie", "charlie12345"),
        ]

        user_map = {}
        for username, password in users:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(password)
                user.save()
                self.stdout.write(self.style.SUCCESS(f"created user: {username}"))
            user_map[username] = user

        post_specs = [
            ("alice", "Launching week packs today. Please review security notes before deploying."),
            ("bob", "Reminder: never trust cross-origin messages without strict origin checks."),
            ("charlie", "Database exports should always enforce ownership checks."),
        ]

        for username, body in post_specs:
            author = user_map[username]
            post, created = Post.objects.get_or_create(author=author, body=body)
            if created:
                self.stdout.write(self.style.SUCCESS(f"created post for: {username}"))

        first_post = Post.objects.filter(author=user_map["alice"]).first()
        if first_post:
            Comment.objects.get_or_create(
                post=first_post,
                author=user_map["bob"],
                body="Looks good. We should audit CSP and CORS headers in the next sprint.",
            )
            Comment.objects.get_or_create(
                post=first_post,
                author=user_map["charlie"],
                body="I will validate DB query paths and export authorization.",
            )

        self.stdout.write(self.style.SUCCESS("demo seed complete"))
