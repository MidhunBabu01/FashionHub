# Generated by Django 3.1.7 on 2021-07-23 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fashion_hub_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('img1', models.ImageField(upload_to='pictures')),
                ('img2', models.ImageField(upload_to='pictures')),
                ('img3', models.ImageField(upload_to='pictures')),
                ('desc', models.TextField()),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fashion_hub_app.category')),
            ],
        ),
    ]
