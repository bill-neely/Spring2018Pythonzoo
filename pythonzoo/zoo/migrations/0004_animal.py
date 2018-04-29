# Generated by Django 2.0.4 on 2018-04-28 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0003_zoo_logofilename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Exhbit Name', max_length=200)),
                ('imageFileName', models.CharField(help_text='Enter logo file name', max_length=200, null=True)),
                ('soundFileName', models.CharField(help_text='Enter sound file name', max_length=200, null=True)),
                ('habitatDescription', models.TextField(help_text='Enter a description of the habitat', max_length=1000)),
                ('dietDescription', models.TextField(help_text='Enter a description of the diet', max_length=1000)),
                ('exhibit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zoo.Exhibit')),
            ],
        ),
    ]
