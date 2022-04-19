# Generated by Django 4.0.3 on 2022-04-19 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, unique=True)),
                ('slug', models.SlugField(max_length=225, unique=True)),
                ('details', models.CharField(max_length=225)),
                ('completed', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_list', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='todo_list', to='todo.tag')),
            ],
        ),
    ]
