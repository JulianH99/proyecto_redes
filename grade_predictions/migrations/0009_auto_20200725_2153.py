# Generated by Django 3.0.8 on 2020-07-25 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_predictions', '0008_auto_20200725_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grade',
            name='status_text',
            field=models.CharField(default='', max_length=50),
        ),
    ]
