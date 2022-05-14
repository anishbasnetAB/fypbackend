# Generated by Django 4.0.4 on 2022-05-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0005_alter_trekguides_guide_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='destination_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='destination_latitude',
            field=models.FloatField(default=1, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='destination_longitude',
            field=models.FloatField(default=1, max_length=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destination',
            name='destination_distance',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='destination',
            name='destination_equipment',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='destination',
            name='destination_medicalNeeds',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='destination',
            name='destination_scams',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
