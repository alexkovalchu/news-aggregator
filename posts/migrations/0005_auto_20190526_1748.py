# Generated by Django 2.2 on 2019-05-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190526_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedlyapisettings',
            name='api_requests_max',
            field=models.IntegerField(default=250),
        ),
        migrations.AlterField(
            model_name='feedlyapisettings',
            name='api_requests_remained',
            field=models.IntegerField(default=250),
        ),
    ]