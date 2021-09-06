# Generated by Django 3.1.7 on 2021-09-06 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0008_billingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Cart.billingaddress'),
        ),
    ]
