from django.core.management import call_command
import os
import django

# Setup Django if needed
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_portfolio.settings')
django.setup()

with open('data.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', stdout=f, indent=2)