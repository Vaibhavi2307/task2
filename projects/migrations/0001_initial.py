# Generated by Django 4.2.4 on 2023-08-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_description', models.TextField()),
                ('project_lead', models.CharField(max_length=20)),
                ('team_size', models.IntegerField()),
                ('programming_language', models.CharField(max_length=20)),
                ('project_start_date', models.DateField()),
                ('project_delivery_date', models.DateField()),
            ],
        ),
    ]
