from django.db import models


class Groups(models.Model):
    groups_name = models.CharField(max_length=100)
    groups_nationality = models.CharField(max_length=100)
    groups_language = models.CharField(max_length=100)
    groups_avg_life_expectancy = models.IntegerField()

    def __str__(self):
        return f'{self.groups_name} {self.groups_nationality} {self.groups_language} {self.groups_language} - ' \
               f'{self.groups_avg_life_expectancy}'
