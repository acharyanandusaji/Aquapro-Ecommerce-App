# Generated by Django 4.0.5 on 2022-07-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_categ_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='color',
            field=models.TextField(null=True),
        ),
    ]
