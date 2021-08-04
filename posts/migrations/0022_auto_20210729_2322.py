# Generated by Django 3.2.5 on 2021-07-30 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_auto_20210729_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7fe8823a3ee0>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7fe8823a3ee0>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7fe8823a3ee0>'),
        ),
        migrations.AlterField(
            model_name='scrapuser',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pic/<function user_profilepic_path at 0x7fe882f60040>'),
        ),
    ]