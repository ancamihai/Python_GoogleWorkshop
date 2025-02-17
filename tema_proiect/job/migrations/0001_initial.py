# Generated by Django 4.1.5 on 2023-01-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=1)),
            ],
        ),
    ]
