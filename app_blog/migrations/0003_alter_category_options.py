# Generated by Django 4.2.5 on 2024-01-04 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_category_slug_alter_article_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія для публікації', 'verbose_name_plural': 'Категорії для публікацій'},
        ),
    ]
