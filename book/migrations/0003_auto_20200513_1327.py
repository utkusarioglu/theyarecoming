# Generated by Django 2.2.12 on 2020-05-13 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200513_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='story_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Choice', to='book.Story'),
        ),
    ]
