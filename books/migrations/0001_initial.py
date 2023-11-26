# Generated by Django 4.2.7 on 2023-11-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=200)),
                ('publication_year', models.IntegerField()),
            ],
        ),
    ]