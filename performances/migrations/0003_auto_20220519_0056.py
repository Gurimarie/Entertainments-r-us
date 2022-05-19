# Generated by Django 3.2 on 2022-05-19 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0002_auto_20220508_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='artist_name',
            field=models.CharField(default='Missing', max_length=254),
        ),
        migrations.AddField(
            model_name='performance',
            name='composer',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='performance',
            name='performance_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='performance',
            name='performance_title',
            field=models.CharField(default='Missing', max_length=254),
        ),
        migrations.AlterField(
            model_name='performance',
            name='artist_id',
            field=models.ForeignKey(default='Missing', null=True, on_delete=django.db.models.deletion.SET_NULL, to='performances.artist'),
        ),
    ]
