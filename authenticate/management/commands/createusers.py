from django.core.management.base import BaseCommand
from authenticate.models import CustomUser
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create Users'

    def add_arguments(self, parser):
        parser.add_argument('users', type=int, help='Create n number of Users')

    def handle(self, *args, **options):
      
      for UserNo in range(options['users']):
        randomPassword = CustomUser.objects.make_random_password()
        username = get_random_string(10)
        email = username + '@gmail.com'
        CustomUser.objects.create_user(username=username, email=email, password=randomPassword)

      self.stdout.write(self.style.SUCCESS( '%s users successfully created.' % options['users'] ))
