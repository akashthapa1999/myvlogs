# Generated by Django 4.2.2 on 2023-10-06 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.CharField(max_length=50000)),
                ('date', models.DateTimeField(null=True)),
            ],
        ),
    ]
