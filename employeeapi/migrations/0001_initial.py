# Generated by Django 5.1 on 2024-08-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=10)),
                ('manager', models.CharField(max_length=50)),
                ('mob_no', models.CharField(max_length=15)),
                ('role', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
            ],
        ),
    ]
