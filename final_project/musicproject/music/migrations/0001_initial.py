# Generated by Django 4.2.5 on 2023-09-16 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albumName', models.CharField(max_length=50, verbose_name='Album Name')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Album created date')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Latest album update')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=50, verbose_name='Artist Name')),
                ('create', models.DateTimeField(auto_now=True, verbose_name='Artist create date')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Lastest artist last_update')),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artist',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SongThumbnail', models.ImageField(help_text='.jpg, png, .jpeg, .svg supported', upload_to='thumbnail/', verbose_name='Song Thumbnail')),
                ('Song', models.FileField(help_text=' .mp3 supported only', upload_to='song/', verbose_name='Song')),
                ('songName', models.CharField(max_length=50, verbose_name='Song Name')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Song created date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Latest song update')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album', verbose_name='Song Album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='Artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist', verbose_name='Artrist Album'),
        ),
    ]
