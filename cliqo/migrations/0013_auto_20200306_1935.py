# Generated by Django 3.0.2 on 2020-03-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliqo', '0012_auto_20200306_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='newmatter',
            name='client_type',
            field=models.CharField(choices=[('Person', 'Person'), ('Business', 'Business')], default='Person', max_length=8),
        ),
        migrations.AlterField(
            model_name='newmatter',
            name='client_name',
            field=models.CharField(default='Client Name', max_length=250),
        ),
    ]
