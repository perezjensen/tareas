# Generated by Django 4.1.3 on 2022-11-27 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kanban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.TextField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'kanban',
                'verbose_name_plural': 'kanbans',
                'db_table': 'kanban',
                'ordering': ['id'],
            },
        ),
    ]
