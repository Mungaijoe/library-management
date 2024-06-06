# Generated by Django 5.0.6 on 2024-05-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.CharField(max_length=200)),
                ('reader_name', models.CharField(max_length=200)),
                ('reader_contact', models.CharField(max_length=200)),
                ('reader_address', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]