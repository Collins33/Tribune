# Generated by Django 2.0 on 2018-02-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20180201_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='language',
            field=models.CharField(default='python-django', max_length=20),
        ),
    ]
