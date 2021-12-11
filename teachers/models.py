from django.db import models

from faker import Faker


class Teachers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    seniority_years = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.subject} - {self.seniority_years}'

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
