import random

from django.db import models


from core.models import Person
from teachers.validators import phone_number_validator


class Teachers(Person):

    seniority_years = models.IntegerField(default=5)
    phone_number = models.CharField(
        max_length=30,
        null=True,
        validators=[phone_number_validator]
    )
    group = models.ManyToManyField(
        'groups.Groups',
        related_name='groups_teachers'
    )

    @classmethod
    def _generate(cls):
        teacher = super()._generate()
        teacher.seniority_years = random.randint(1, 30)
        teacher.phone_number = random.randint(100000000, 999999999)
        teacher.save()
