import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

ADULT_AGE_LIMIT = 18


def adult_validator(birthday, age_limit=18):
    age = datetime.date.today().year - birthday.year
    if age < age_limit:
        raise ValidationError(f'Age should be greater than {age_limit}y.o.')


@deconstructible
class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    # def __call__(self, birthday):
    def __call__(self, *args, **kwargs):
        adult_validator(args[0], self.age_limit)

    def __eq__(self, other):
        return(
            isinstance(other, self.__class__) and
            self.age_limit == other.age_limit
        )
#
# av = AdultValidator(20)
