import datetime

from django.core.exceptions import ValidationError

import students

ADULT_AGE_LIMIT = 18


def adult_validator(birthday, age_limit=18):
    age = datetime.date.today().year - birthday.year
    if age < age_limit:
        raise ValidationError(f'Age should be greater than {age_limit}y.o.')


def phone_number_validator(phone_number):
    from .models import Students

    # all_data = Students.objects.filter(phone_number=phone_number)
    # if len(all_data) > 0:
    #     raise ValidationError(f'The phone number {phone_number} is not unique.')
    #
    # all_data = students.models.Students.objects.filter(phone_number=phone_number)
    # if len(all_data) > 0:
    #     raise ValidationError(f'The phone number {phone_number} is not unique.')

    if students.models.Students.objects.filter(phone_number=phone_number).exist:
        raise ValidationError(f'The phone number {phone_number} is not unique.')


class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    # def __call__(self, birthday):
    def __call__(self, *args, **kwargs):
        adult_validator(args[0], self.age_limit)

#
# av = AdultValidator(20)
