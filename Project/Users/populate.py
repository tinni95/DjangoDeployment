import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Users.settings')

import django
django.setup()

import random
from UserApp.models import User
from faker import Faker

fakegen = Faker()

def pop(N=5):
    for entry in range(N):
        fake_first_name = fakegen.name().split()[0]
        fake_last_name = fakegen.name().split()[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,
                                         email=fake_email)[0]

if __name__ == '__main__':
    print("populating script")
    pop(20)
    print("complete..")
