# Generated by Django 3.0.3 on 2020-02-21 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20200216_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='电影名')),
                ('type', models.CharField(max_length=20, verbose_name='职位')),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('pic', models.CharField(max_length=100, verbose_name='照片')),
            ],
        ),
    ]