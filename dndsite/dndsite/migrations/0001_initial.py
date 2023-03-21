# Generated by Django 4.1.7 on 2023-03-21 16:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WildMagicTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dice_value', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('effect', models.TextField()),
                ('enabled', models.BooleanField(default=True)),
                ('urls', models.URLField(null=True)),
            ],
        ),
    ]
