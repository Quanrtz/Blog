# Generated by Django 4.0.5 on 2022-07-01 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Economy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name')),
                ('task', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Posts',
                'verbose_name_plural': 'Economic',
            },
        ),
        migrations.CreateModel(
            name='It',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name')),
                ('task', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Posts',
                'verbose_name_plural': 'It',
            },
        ),
    ]
