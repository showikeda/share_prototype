# Generated by Django 3.0.6 on 2020-07-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0005_auto_20200716_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='ファイル'),
        ),
    ]