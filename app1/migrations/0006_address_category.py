# Generated by Django 5.1.3 on 2025-03-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_service_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='category',
            field=models.CharField(default='rumah', max_length=100),
            preserve_default=False,
        ),
    ]
