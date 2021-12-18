
import datetime

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

# from .validators import adult_validator
from core.validators import AdultValidator

from .validators import phone_number_validator

from groups.models import Groups


# students.students
class Students(models.Model):
    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    phone_number = models.CharField(
        max_length=30,
        null=True,
        validators=[phone_number_validator]
    )
    age = models.IntegerField()
    birthday = models.DateField(
        default=datetime.date.today,
        # validators=[adult_validator]
        validators=[AdultValidator(20)]
    )
    # birthday1 = models.DateField(default=datetime.date.today)
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)
    group = models.ForeignKey(
        Groups,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.age} - {self.phone_number}'

    def save(self, *args, **kwargs):
        self.age = relativedelta(datetime.date.today(), self.birthday).years
        super().save(*args, **kwargs)

    @staticmethod
    def generate_students(cnt):
        fa = Faker()
        for _ in range(cnt):
            st = Students(
                first_name=fa.first_name(),
                last_name=fa.last_name(),
                age=fa.pyint(1, 100),
                birthday=fa.date_between_dates(date_start='-45y', date_end='-5y')
            )

            st.save()
