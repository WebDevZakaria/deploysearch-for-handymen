# Generated by Django 3.2.6 on 2023-05-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cenceled', 'Cenceled'), ('Accepted', 'accepted'), ('New', 'New'), ('Completed', 'Completed')], default='New', max_length=10),
        ),
    ]
