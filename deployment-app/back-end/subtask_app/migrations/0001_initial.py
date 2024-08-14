# Generated by Django 5.0.3 on 2024-03-28 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('completed', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('parent_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='task_app.task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]