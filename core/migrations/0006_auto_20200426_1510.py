# Generated by Django 2.2.10 on 2020-04-26 14:10

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200426_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='about_page_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='About Page: Name ex. Dr. Timileyin Adebayo'),
        ),
        migrations.AddField(
            model_name='setting',
            name='about_page_position',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='About Page: Position ex. CEO, Lead Engineer'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='about_page_photo',
            field=models.ImageField(blank=True, null=True, upload_to='settings/about/', verbose_name='About Page: Image'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='about_page_quote',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='About Page: Quote'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='about_page_text',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='About Page: Text'),
        ),
    ]
