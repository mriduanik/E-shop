# Generated by Django 4.0.4 on 2022-05-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.CharField(default='', max_length=1000),
        ),
    ]