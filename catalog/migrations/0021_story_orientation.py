# Generated by Django 2.0.1 on 2018-05-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_story_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='orientation',
            field=models.CharField(default=0, help_text='photo orientation', max_length=2),
            preserve_default=False,
        ),
    ]
