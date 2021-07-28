# Generated by Django 3.2.4 on 2021-07-28 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20210728_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='city_name',
        ),
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7f458f35ab80>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7f458f35ab80>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7f458f35ab80>'),
        ),
    ]
