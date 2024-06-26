# Generated by Django 4.2.13 on 2024-06-18 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_summary_sort_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='conclusion',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='project_description',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='project_title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='short_summary',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='technologies_and_tools_used',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
    ]
