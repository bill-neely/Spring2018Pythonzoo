# Generated by Django 2.0.4 on 2018-04-28 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0008_auto_20180428_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitneighbor',
            name='direction',
            field=models.CharField(choices=[('n', 'North'), ('s', 'South'), ('e', 'East'), ('w', 'West'), ('nw', 'Northwest'), ('sw', 'Southwest'), ('ne', 'Norteast'), ('se', 'Southeast')], help_text='Enter cardinal travel direction.', max_length=2),
        ),
    ]
