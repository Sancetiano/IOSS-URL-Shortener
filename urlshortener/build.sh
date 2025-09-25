#!/usr/bin/env bash
set -e  # Exit on error

# Install dependencies
python -m pip install -r requirements.txt

# Collect static files (for CSS/JS)
python manage.py collectstatic --noinput