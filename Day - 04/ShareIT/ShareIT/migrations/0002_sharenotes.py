# Generated by Django 5.2.1 on 2025-05-28 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShareIT', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sharenotes',
            fields=[
                ('dcid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('fiename', models.CharField(max_length=100)),
                ('uid', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=50)),
            ],
        ),
    ]
