#!/bin/sh
./manage.py migrate
if [ -n "${DJANGO_ADMIN_USERNAME}" ] && [ -n "${DJANGO_ADMIN_EMAIL}" ] && [ -n "${DJANGO_ADMIN_PASSWORD}" ]; then
    ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('${DJANGO_ADMIN_USERNAME}', '${DJANGO_ADMIN_EMAIL}', '${DJANGO_ADMIN_PASSWORD}') if not User.objects.filter(username='${DJANGO_ADMIN_USERNAME}').exists() else print('User already exists')"
fi
gunicorn -b :${PORT} prb.wsgi