from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.utils import query_counter


class Command(BaseCommand):
    @query_counter
    def handle(self, *args, **kwargs):
        if not User.objects.all():
            admin = User(username='friend')
            admin.set_password('123')
            admin.is_superuser = True
            admin.is_staff = True
            admin.save()
