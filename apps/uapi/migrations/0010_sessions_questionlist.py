# Generated by Django 3.2.11 on 2022-03-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uapi', '0009_alter_sessions_timelimit'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessions',
            name='questionList',
            field=models.TextField(null=True),
        ),
    ]
