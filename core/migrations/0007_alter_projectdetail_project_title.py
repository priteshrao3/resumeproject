# Generated by Django 4.2.13 on 2024-06-20 06:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_professionalexperience_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='project_title',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]