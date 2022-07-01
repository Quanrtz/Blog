from django.db import models


class Economy(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Economic'


class It(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Description')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'It'


class Sports(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Description')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Sport'




class ToDo(models.Model):
    title = models.CharField('Название задания', max_length=500)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title


# Create your models here.
