# Generated by Django 3.2.16 on 2022-11-26 16:47

from django.db import migrations, models
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_order_pick_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pick_up',
            field=models.DateTimeField(validators=[order.models.validate_date]),
        ),
    ]
