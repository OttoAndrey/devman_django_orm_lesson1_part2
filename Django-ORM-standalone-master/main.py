import os
import sys
import django
from django.utils.timezone import localtime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit, format_duration


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

    # Step 4
    active_passcards = []
    passcards = Passcard.objects.all()
    for p in passcards:
        if p.is_active:
            active_passcards.append(p)
    print('Количество пропусков:', Passcard.objects.count())
    print(f'Активных пропусков: {len(active_passcards)}')

    # Step 5
    active_passcards = Passcard.objects.filter(is_active=True)
    print('Количество пропусков:', Passcard.objects.count())
    print(f'Активных пропусков: {len(active_passcards)}')

    # Step 8
    print(Visit.objects.all())

    # Step 9
    not_leaved_visits = Visit.objects.filter(leaved_at=None)
    print(not_leaved_visits)

    # Step 10
    for not_leaved in not_leaved_visits:
        print(f"""Зашёл в хранилище, время по Москве:
{localtime(not_leaved.entered_at)}

Находится в хранилище:
{localtime()- localtime(not_leaved.entered_at)}""")

    # Step 11
    for not_leaved in not_leaved_visits:
        print(not_leaved.passcard.owner_name)

    # Step 12
    for not_leaved in not_leaved_visits:
        duration = not_leaved.get_duration()
        print(f"""Зашёл в хранилище, время по Москве:
{localtime(not_leaved.entered_at)}

Находится в хранилище:
{format_duration(duration)}""")
