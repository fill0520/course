# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-14 05:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=100)),
                ('longtitude', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('imgpath', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(b'EMAIL', b'EMAIL'), (b'FACEBOOK', b'FACEBOOK'), (b'PHONE', b'PHONE')], default=b'PHONE', max_length=10)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='course',
            options={},
        ),
        migrations.RemoveField(
            model_name='course',
            name='created',
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='courses.Category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='logo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='courses.Course'),
        ),
        migrations.AddField(
            model_name='branch',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='courses.Course'),
        ),
    ]
