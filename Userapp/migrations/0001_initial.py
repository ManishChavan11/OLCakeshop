# Generated by Django 3.2.2 on 2021-08-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'UserMaster',
            },
        ),
    ]
