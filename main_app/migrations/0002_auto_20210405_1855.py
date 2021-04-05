# Generated by Django 3.1.7 on 2021-04-05 18:55

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='url',
            field=models.CharField(default='https://i.imgur.com/CMqTyEZs.jpg', max_length=250),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('prep_time', models.CharField(max_length=25)),
                ('cook_time', models.CharField(max_length=25)),
                ('servings', models.IntegerField()),
                ('ingredients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=25), size=None)),
                ('instructions', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=250), size=None)),
                ('url', models.CharField(default='https://i.imgur.com/RtCoQcll.jpg', max_length=250)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
