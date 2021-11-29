import datetime

from django.db import models

from faker import Faker


# students.students
class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    birthday = models.DateField(default=datetime.date.today)
    # birthday1 = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.age}'

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
