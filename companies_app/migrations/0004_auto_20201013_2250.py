# Generated by Django 3.1.2 on 2020-10-13 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies_app', '0003_auto_20201013_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='title_cat',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='title',
            new_name='title_com',
        ),
    ]
