# Generated by Django 3.1.2 on 2020-10-12 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music_db',
            name='codes',
        ),
        migrations.RemoveField(
            model_name='music_db',
            name='sesac',
        ),
        migrations.RemoveField(
            model_name='music_db',
            name='track',
        ),
        migrations.AddField(
            model_name='music_db',
            name='ascap_id',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='ascap_ipi',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='ascap_pub',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='bmi_id',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='bmi_pub',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='gmr_id',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='gmr_ipi',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='gmr_pub',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='ipi',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='isni',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='isrc',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='othername',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='sesac_id',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='sesac_pub',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='title',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='music_db',
            name='writer',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='music_db',
            name='album',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='music_db',
            name='artist',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
