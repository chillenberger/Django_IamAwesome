# Generated by Django 2.0.1 on 2018-04-08 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180408_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='checkout_button',
            field=models.CharField(help_text='variable to hold paypal button', max_length=40, null=True),
        ),
    ]
