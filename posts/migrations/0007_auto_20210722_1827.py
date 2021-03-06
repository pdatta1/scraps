# Generated by Django 3.2.5 on 2021-07-22 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20210720_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7f67df5e5d30>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7f67df5e5d30>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7f67df5e5d30>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30, unique=True, verbose_name='Title'),
        ),
    ]
