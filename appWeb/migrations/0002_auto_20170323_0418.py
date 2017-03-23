from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import User

def create_admin_user(apps, schema_editor):
    user = User(pk=1, username="admin", is_active=True,
                is_superuser=True, is_staff=True,
                email="email@gmail.com")
    user.set_password('admin')
    user.save()
    user = User(pk=2, username="monitor", is_active=True,
                is_superuser=False, is_staff=True,
                email="email@gmail.com")
    user.set_password('monitor')
    user.save()

class Migration(migrations.Migration):

    dependencies = [
    	('appWeb', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython(create_admin_user),
    ]
