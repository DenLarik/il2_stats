#!/bin/bash

cd ../src || exit

../.venv/bin/python manage.py collectstatic --noinput
read -p "Press any key to continue... "
