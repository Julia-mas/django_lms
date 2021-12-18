from django.core.exceptions import ValidationError

import teachers


def phone_number_validator(phone_number):
    if teachers.models.Teachers.objects.filter(phone_number=phone_number).exists():
        raise ValidationError(f'The phone number {phone_number} is not unique.')


def normalize_phone(phone):
    phone_update = "".join(p for p in phone if p.isdecimal())
    return phone_update
