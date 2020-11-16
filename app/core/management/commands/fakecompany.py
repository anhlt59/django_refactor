from django.contrib.auth import get_user_model
from django.core.management import BaseCommand, CommandError
from faker import Faker
from itertools import islice

from app.share_resources.users import Company

User = get_user_model()


class Command(BaseCommand):
    help = 'Fake data user'

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help='number of record', default=1)

    def create_bulk_data(self, n):
        fake = Faker(['en_US'])
        default_password = "123456"

        for _ in range(n):
            username = fake.random_letters(8)

            yield Company(
                username=username,
                password=default_password,
                type=User.TYPES.COMPANY,
                is_staff=True,
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
            Company.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)
            self.stdout.write(f"> create {count} companies")

        # collect stats
        self.stdout.write(f"Total {Company.objects.count()} companies")
