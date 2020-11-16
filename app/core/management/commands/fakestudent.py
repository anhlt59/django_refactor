from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.management import BaseCommand, CommandError
from faker import Faker
from itertools import islice
import random

from app.share_resources.users import Student

User = get_user_model()


class Command(BaseCommand):
    """ python manage.py fakestudent 10
        # to fake 10 student
    """
    help = 'Fake data user'

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help='number of record', default=1)

    def create_bulk_data(self, n):
        fake = Faker(['en_US'])
        default_password = "123456"
        default_type = User.TYPES.STUDENT

        for _ in range(n):
            user_name = fake.user_name()
            email = f"{user_name}{random.randint(1, 100)}@yopmail.com".lower()

            yield Student(
                username=email,
                email=email,
                password=default_password,
                type=default_type,
                is_superuser=False
            )

    def handle(self, *args, **options):
        N = options['number']
        count = 0

        objs = self.create_bulk_data(N)
        while True:
            batch = list(islice(objs, 100))
            if not batch:
                break
            Student.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)
            self.stdout.write(f"> create {count} students")

        # collect stats
        self.stdout.write(f"Total {Student.objects.count()} students")
