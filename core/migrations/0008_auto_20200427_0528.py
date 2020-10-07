# Generated by Django 2.2.10 on 2020-04-27 04:28

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200427_0457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title of the project')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='Do not edit, value is automatic')),
                ('image', models.ImageField(upload_to='projects/')),
                ('content', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Project Page Content')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'project',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='setting',
            name='portfolio_page_text',
            field=models.TextField(blank=True, null=True, verbose_name='Portfolio Page: Top Text'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, unique=True, verbose_name='Do not edit, value is automatic'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='services_page_text',
            field=models.TextField(blank=True, null=True, verbose_name='Services Page: Top Text'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True, verbose_name='Do not edit, value is automatic'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='url',
            field=models.URLField(blank=True, editable=False, null=True, verbose_name='Do not edit, value is automatic'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='core.Category'),
        ),
    ]
