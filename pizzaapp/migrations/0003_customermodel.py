# Generated by Django 3.0.7 on 2020-08-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0002_pizzamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=10)),
                ('phoneno', models.CharField(max_length=10)),
            ],
        ),
    ]