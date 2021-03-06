# Generated by Django 3.0.5 on 2020-04-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40)),
                ('image', models.ImageField(upload_to='media')),
                ('text', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галареи',
            },
        ),
    ]
