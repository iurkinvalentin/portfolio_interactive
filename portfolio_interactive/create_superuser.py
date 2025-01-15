from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'securepassword')
    print("Superuser created.")
else:
    print("Superuser already exists.")
