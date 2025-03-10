# Generated by Django 5.1 on 2024-12-27 09:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookShopAccount',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='account', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('user_badge', models.IntegerField(choices=[(1, 'Bronze'), (2, 'Silver'), (3, 'Gold'), (4, 'Diamond'), (5, 'Platinum')], default=1)),
                ('coins', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='DepositMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
