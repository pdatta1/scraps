# Generated by Django 3.2.5 on 2021-08-02 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0033_auto_20210802_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7f5d9bc504c0>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7f5d9bc504c0>'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/<function user_directory_path at 0x7f5d9bc504c0>'),
        ),
    ]
