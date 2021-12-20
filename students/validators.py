from django.core.exceptions import ValidationError

import students.models


def phone_number_validator(phone_number):
    # from .models import Students
    #
    # all_data = Students.objects.filter(phone_number=phone_number)
    # if len(all_data) > 0:
    #     raise ValidationError(f'The phone number {phone_number} is not unique.')
    #
    # all_data = students.models.Students.objects.filter(phone_number=phone_number)
    # if len(all_data) > 0:
    #     raise ValidationError(f'The phone number {phone_number} is not unique.')

    if students.models.Students.objects.filter(phone_number=phone_number).exists():
        raise ValidationError(f'The phone number {phone_number} is not unique.')
