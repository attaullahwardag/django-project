# Generated by Django 2.2.5 on 2019-10-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=555)),
                ('post', models.TextField()),
            ],
        ),
    ]
