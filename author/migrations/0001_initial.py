# Generated by Django 5.1 on 2024-12-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='author_images/')),
                ('address', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, null=True)),
                ('total_borrowed', models.IntegerField(blank=True, default=0, null=True)),
                ('rank', models.IntegerField(blank=True, null=True, unique=True)),
                ('popularity', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
            ],
        ),
    ]
