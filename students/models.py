
import datetime
import random

from django.db import models

from core.models import Person

from .validators import phone_number_validator

from groups.models import Groups


# students.students
class Students(Person):

    phone_number = models.CharField(
        max_length=30,
        null=True,
        validators=[phone_number_validator]
    )
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)
    group = models.ForeignKey(
        Groups,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )

    @classmethod
    def _generate(cls):
        student = super()._generate()
        student.phone_number = random.randint(100000000, 999999999)
        student.save()



