# Generated by Django 2.0.6 on 2018-07-01 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a/the category/categories this Parliament Record falls under', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ParliamentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('category', models.ManyToManyField(help_text='Select a/the category/categories for this Parliament Record', to='records.Category')),
            ],
        ),
        migrations.CreateModel(
            name='SittingDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='parliamentrecord',
            name='sitting_date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.SittingDate'),
        ),
    ]
