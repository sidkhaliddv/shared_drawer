# Generated by Django 5.0.7 on 2024-07-27 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawers', '0001_initial'),
        ('items', '0002_alter_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='drawer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drawers.drawer'),
        ),
    ]