# Generated by Django 5.1.3 on 2024-11-14 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_client_age_alter_client_goal_weight_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='sexe',
            field=models.CharField(default='homme', max_length=50),
            preserve_default=False,
        ),
    ]
