# Generated by Django 3.2.8 on 2021-10-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_todolist_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='category',
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2021-10-20'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2021-10-20'),
        ),
    ]
