# Generated by Django 4.0 on 2022-06-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mazmuni',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
    ]