from django.db import models


class Groups(models.Model):
    groups_name = models.CharField(max_length=100)
    groups_nationality = models.CharField(max_length=100)
    groups_language = models.CharField(max_length=100)
    members_qty = models.IntegerField()

    headman = models.OneToOneField(
        'students.Students',
        on_delete=models.SET_NULL,
        null=True,
        related_name='headman_group'
    )

    def __str__(self):
        return f'{self.groups_name} {self.groups_nationality} {self.groups_language} - ' \
               f'{self.members_qty}'
