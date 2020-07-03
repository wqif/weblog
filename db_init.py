import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlogBackend.settings.develop')

django.setup()
from django.contrib.auth.models import User




# create super user
User.objects.create_superuser('admin', 'admin@weblog.com', 'admin123')
