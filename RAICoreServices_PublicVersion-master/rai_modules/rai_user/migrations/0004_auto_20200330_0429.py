# Generated by Django 2.2.3 on 2020-03-30 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rai_user', '0003_raiuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiuser',
            name='image',
            field=models.ImageField(default=0, upload_to='rai_user/image'),
        ),
    ]