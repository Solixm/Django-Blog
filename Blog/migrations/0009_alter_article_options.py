# Generated by Django 4.1.5 on 2023-02-17 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_alter_article_options_alter_article_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created', '-updated')},
        ),
    ]