# Generated by Django 4.1.2 on 2022-10-28 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slackUsername', models.CharField(max_length=50, null=True)),
                ('backend', models.BooleanField(default=True)),
                ('age', models.IntegerField(null=True)),
                ('bio', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
