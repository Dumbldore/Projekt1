# Generated by Django 2.1.3 on 2018-11-08 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20181108_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='patrol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Patrol'),
        ),
    ]
