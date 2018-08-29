#!/usr/bin/env python
import os
import sys
from pathlib import Path
from dotenv import load_dotenv


def load_env():
    env = os.environ.get('ENV')
    env_file = Path('.') / '.env.{}'.format(env)
    if not env_file.exists():
        env_file = Path('.') / '.env.development'
    load_dotenv(dotenv_path=env_file.as_posix())


if __name__ == "__main__":
    load_env()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nexaas_id_django_example.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
