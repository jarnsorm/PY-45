from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    icon = models.ImageField(width_field=512, height_field=512, blank=True, null=True)
    date_of_registration = models.DateTimeField(auto_now_add=True, verbose_name='date of registration')

    def __str__(self):
        return f'{self.lastname} {self.firstname}'

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
