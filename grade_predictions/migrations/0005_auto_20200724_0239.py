# Generated by Django 3.0.8 on 2020-07-24 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_predictions', '0004_auto_20200723_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='teachers',
            field=models.ManyToManyField(to='grade_predictions.Teacher'),
        ),
    ]
