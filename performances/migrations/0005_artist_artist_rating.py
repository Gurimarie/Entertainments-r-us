# Generated by Django 3.2 on 2022-05-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0004_auto_20220519_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]