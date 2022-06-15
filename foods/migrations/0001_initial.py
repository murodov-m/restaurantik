# Generated by Django 4.0.5 on 2022-06-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('views', models.IntegerField(default=0)),
                ('photo', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
            ],
        ),
    ]
