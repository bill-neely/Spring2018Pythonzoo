# Generated by Django 2.0.4 on 2018-04-28 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0006_auto_20180428_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExhibitNeighbors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('n', 'North'), ('s', 'South'), ('e', 'East'), ('w', 'West'), ('nw', 'Northwest'), ('sw', 'Southwest'), ('ne', 'Norteast'), ('nw', 'Northwest')], help_text='Enter cardinal travel direction.', max_length=2)),
                ('fromExhibit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zoo.Exhibit')),
                ('toExhibit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='toExhibit', to='zoo.Exhibit')),
            ],
        ),
    ]
