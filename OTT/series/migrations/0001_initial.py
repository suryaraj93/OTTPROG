# Generated by Django 3.1 on 2020-10-06 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=120, unique=True)),
                ('genre', models.CharField(max_length=120)),
                ('starring', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='images')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.language')),
            ],
        ),
    ]
