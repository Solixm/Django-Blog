# Generated by Django 4.1.5 on 2023-02-10 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_alter_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created', '-updated')},
        ),
    ]
