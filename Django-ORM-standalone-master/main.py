import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())

    # Step 2
    print(Passcard.objects.all())

    # Step 3
    passcard = Passcard.objects.all()[0]
    print(f"""owner_name: {passcard.owner_name}
passcode: {passcard.passcode}
created_at: {passcard.created_at}
is_active: {passcard.is_active}""")
