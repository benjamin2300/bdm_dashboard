# Generated by Django 2.2.5 on 2019-10-25 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmucert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='cmucert.Employee'),
        ),
        migrations.AlterField(
            model_name='logon',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logons', to='cmucert.Employee'),
        ),
    ]
