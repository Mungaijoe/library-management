# Generated by Django 5.0.6 on 2024-06-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0010_bookinstance_reader_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='outstanding_debt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]