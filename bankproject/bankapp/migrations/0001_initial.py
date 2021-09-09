# Generated by Django 3.2.5 on 2021-07-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('acno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('dob', models.CharField(max_length=30)),
                ('contactno', models.IntegerField()),
                ('emailaddress', models.EmailField(max_length=50)),
                ('panno', models.CharField(max_length=10)),
                ('aadharno', models.CharField(max_length=12)),
                ('balance', models.IntegerField()),
                ('openingdate', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
