# Generated by Django 3.1.7 on 2021-03-04 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0002_auto_20210304_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snacks',
            name='purchaser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='snacks.snacks'),
        ),
    ]