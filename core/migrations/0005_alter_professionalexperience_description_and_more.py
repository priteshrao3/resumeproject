# Generated by Django 4.2.13 on 2024-06-18 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_projectdetail_conclusion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalexperience',
            name='description',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='career_objective',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
    ]
