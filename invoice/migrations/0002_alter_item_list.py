# Generated by Django 4.0.4 on 2022-05-01 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.list'),
        ),
    ]