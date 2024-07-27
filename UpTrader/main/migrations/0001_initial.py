# Generated by Django 5.0.7 on 2024-07-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.TextField()),
                ('lvl_1', models.TextField()),
                ('lvl_2', models.TextField()),
                ('lvl_2_ref', models.TextField()),
            ],
            options={
                'db_table': 'Menu',
            },
        ),
    ]
