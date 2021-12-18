from django.db import models

from faker import Faker

from teachers.validators import phone_number_validator


class Teachers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    seniority_years = models.IntegerField()
    phone_number = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        validators=[phone_number_validator]
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.subject} - {self.seniority_years} - {self.phone_number}'

    @staticmethod
    def generate_teachers(cnt):
        fa = Faker()
        for _ in range(cnt):
            st = Teachers(
                first_name=fa.first_name(),
                last_name=fa.last_name(),
                seniority_years=fa.pyint(1, 100),
            )

            st.save()
