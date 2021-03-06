# Generated by Django 3.2.5 on 2021-08-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0036_auto_20210802_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcomment',
            options={'ordering': ['date_created'], 'verbose_name': 'sub_comment', 'verbose_name_plural': 'sub_comments'},
        ),
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7fdb5437f5e0>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7fdb5437f5e0>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7fdb5437f5e0>'),
        ),
    ]
