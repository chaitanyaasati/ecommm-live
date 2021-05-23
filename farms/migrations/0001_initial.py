# Generated by Django 3.2 on 2021-05-23 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.address')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.pincode')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.seller')),
            ],
        ),
    ]
