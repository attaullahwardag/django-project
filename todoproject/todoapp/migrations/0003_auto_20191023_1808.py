# Generated by Django 2.2.5 on 2019-10-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=555, unique=True),
        ),
    ]
