# Generated by Django 3.2 on 2023-03-19 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_auto_20230319_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('Gray', 'Серый'), ('Black', 'Чёрный'), ('White', 'Белый'), ('Ginger', 'Рыжий'), ('Mixed', 'Смешанный')], max_length=16),
        ),
    ]
