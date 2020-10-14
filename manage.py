#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from decouple import config

def main():
    """Run administrative tasks."""
    try:
        """if .env file exists and ENV=dev django dev settings will be targeted"""
        env = config('ENV')
        if env == 'dev':
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inniventes_employee.settings.dev')
        elif env == 'prod':
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inniventes_employee.settings.prod')
        elif env == 'staging':
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inniventes_employee.settings.staging')
    except Exception:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inniventes_employee.settings.prod')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
