import datetime
from django.core.validators import MinLengthValidator
from django.db import models

from dateutil.relativedelta import relativedelta
from faker import Faker


class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    age = models.IntegerField()
    birthday = models.DateField(
        default=datetime.date.today)

    def __str__(self):
        return f'{self.__full_name()}{self.birthday}'

    def __full_name(self):
        return f'{self.first_name}{self.last_name}'

    def save(self, *args, **kwargs):
        if isinstance(self.birthday, str):
            self.birthday = datetime.datetime.strptime(self.birthday, '%Y-%m-%d')

        self.age = relativedelta(datetime.date.today(), self.birthday).years
        super().save(*args, **kwargs)

    @classmethod
    def _generate(cls):
        f = Faker()
        obj = cls(
            first_name=f.first_name(),
            last_name=f.last_name(),
            birthday=f.date_between(start_date='-65y', end_date='-18y')
        )

        obj.age = relativedelta(datetime.date.today(), obj.birthday).years
        obj.save()

        return obj

    @classmethod
    def generate(cls, cnt):
        for _ in range(cnt):
            cls._generate()
