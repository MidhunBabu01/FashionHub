from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0002_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]