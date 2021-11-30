# Generated by Django 3.2.5 on 2021-11-30 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting', models.CharField(max_length=40)),
                ('ending', models.CharField(max_length=40)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=20)),
                ('train_number', models.IntegerField()),
                ('train_starting', models.CharField(max_length=40)),
                ('train_ending', models.CharField(max_length=40)),
            ],
        ),
    ]
