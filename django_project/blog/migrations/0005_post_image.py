# Generated by Django 4.1 on 2022-08-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_steps'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='food.jpg', upload_to='recipe_pics'),
        ),
    ]
