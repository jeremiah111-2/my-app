# Generated by Django 5.0.1 on 2024-01-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_to_be_saved', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(max_length=1000000)),
            ],
        ),
    ]
