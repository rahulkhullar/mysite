# Generated by Django 2.2.dev20180608160017 on 2018-06-14 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oms', '0004_auto_20180614_0520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='Category', max_length=200)),
                ('category_description', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AddField(
            model_name='item',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='oms.Category'),
        ),
    ]
