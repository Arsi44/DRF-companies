# Generated by Django 3.1.2 on 2020-10-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default='None', max_length=50, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='title',
            field=models.CharField(default='None', max_length=50, verbose_name='Название'),
        ),
    ]