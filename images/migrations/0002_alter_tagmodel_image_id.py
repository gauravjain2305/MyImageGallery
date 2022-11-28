# Generated by Django 4.1.3 on 2022-11-27 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagmodel',
            name='image_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='images.imagemodel'),
        ),
    ]