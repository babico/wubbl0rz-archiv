# Generated by Django 4.0.2 on 2022-02-03 17:33

import clips.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_id', models.PositiveIntegerField()),
                ('name', models.SlugField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.PositiveIntegerField()),
                ('name', models.CharField(default='Unknown', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('uuid', models.SlugField(default=clips.models.gen_id, editable=False, primary_key=True, serialize=False, unique=True)),
                ('clip_id', models.SlugField(max_length=100)),
                ('title', models.CharField(max_length=150)),
                ('view_count', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('duration', models.PositiveIntegerField(blank=True, null=True)),
                ('resolution', models.TextField(blank=True, null=True)),
                ('size', models.PositiveBigIntegerField(blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clips.creator')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clips.game')),
                ('vod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vods.vod')),
            ],
        ),
    ]