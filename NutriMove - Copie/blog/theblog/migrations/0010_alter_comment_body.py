# Generated by Django 5.1.3 on 2024-11-11 13:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(500)]),
        ),
    ]