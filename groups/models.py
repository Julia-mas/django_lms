from django.db import models
from faker import Faker


class Groups(models.Model):
    groups_name = models.CharField(max_length=100)
    groups_country = models.CharField(max_length=100)
    groups_language = models.CharField(max_length=100)
    members_qty = models.IntegerField(default=5)

    headman = models.OneToOneField(
        'students.Students',
        on_delete=models.SET_NULL,
        null=True,
        related_name='headman_group'
    )

    teachers = models.ManyToManyField(
        'teachers.Teachers',
        related_name='groups'

    )

    def __str__(self):
        return f'{self.groups_name} - {self.groups_country}'

    @classmethod
    def _generate(cls):
        f = Faker()
        obj = cls(
            groups_name=f.name(),
            groups_country=f.country(),
        )
        obj.save()

        return obj

    @classmethod
    def generate(cls, cnt):
        for _ in range(cnt):
            cls._generate()