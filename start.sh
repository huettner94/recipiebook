#!/bin/sh
./manage.py migrate
gunicorn -b :$PORT prb.wsgi