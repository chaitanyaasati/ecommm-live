# Generated by Django 3.2 on 2021-04-26 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.address')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.authentication')),
            ],
        ),
    ]
