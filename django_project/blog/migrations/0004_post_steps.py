# Generated by Django 4.1 on 2022-08-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='steps',
            field=models.TextField(default='no steps provided'),
            preserve_default=False,
        ),
    ]
