from django.db import models
import datetime
from faker import Faker


class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.date.today)
    format_education = models.CharField(max_length=100)
    group = models.OneToOneField(
        'groups.Groups',
        on_delete=models.SET_NULL,
        null=True,
        related_name='course_group'
    )

    def __str__(self):
        return f'{self.name} {self.duration}'

    @classmethod
    def _generate(cls):
        f = Faker()
        obj = cls(
            name=f.name(),
        )
        obj.save()

        return obj

    @classmethod
    def generate(cls, cnt):
        for _ in range(cnt):
            cls._generate()

