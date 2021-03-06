# Generated by Django 2.0.1 on 2018-03-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fec', '0013_auto_20180227_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filing',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('SUPERSEDED', 'superseded by amendment'), ('COVERED', 'covered by periodic'), ('MEMO', 'memo'), ('PROCESSING', 'processing'), ('FAILED', 'failed')], default='PROCESSING', max_length=50),
        ),
        migrations.AlterField(
            model_name='schedulea',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('SUPERSEDED', 'superseded by amendment'), ('COVERED', 'covered by periodic'), ('MEMO', 'memo'), ('PROCESSING', 'processing'), ('FAILED', 'failed')], default='ACTIVE', max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleb',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('SUPERSEDED', 'superseded by amendment'), ('COVERED', 'covered by periodic'), ('MEMO', 'memo'), ('PROCESSING', 'processing'), ('FAILED', 'failed')], default='ACTIVE', max_length=50),
        ),
        migrations.AlterField(
            model_name='schedulee',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('SUPERSEDED', 'superseded by amendment'), ('COVERED', 'covered by periodic'), ('MEMO', 'memo'), ('PROCESSING', 'processing'), ('FAILED', 'failed')], default='ACTIVE', max_length=50),
        ),
    ]
