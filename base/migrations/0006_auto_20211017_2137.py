# Generated by Django 3.1.4 on 2021-10-17 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_message_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
