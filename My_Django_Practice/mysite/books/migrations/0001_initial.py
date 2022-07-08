# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('authors', models.ManyToManyField(to='books.Authors')),
            ],
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
                ('website', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='publishers',
            field=models.ForeignKey(to='books.Publishers'),
        ),
    ]
