# Generated by Django 5.0.4 on 2024-04-30 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ARFood', '0004_alter_food_gltf'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='card_tracker',
            field=models.FileField(blank=True, null=True, upload_to='card/'),
        ),
    ]
