# Generated by Django 5.0.7 on 2024-07-15 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-publish'], 'verbose_name_plural': 'Posts'},
        ),
    ]