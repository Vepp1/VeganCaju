# Generated by Django 3.2.16 on 2022-11-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=200, unique=True)),
                ('flavor', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('pick_up', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(0, 'Waiting for Approval'), (1, 'Approved'), (2, 'Cancelled')], default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]