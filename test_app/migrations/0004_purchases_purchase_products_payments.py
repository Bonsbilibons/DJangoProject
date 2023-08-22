# Generated by Django 4.2.2 on 2023-07-25 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purch_id', models.CharField(max_length=50, verbose_name='purch_id')),
                ('total_sum', models.PositiveIntegerField(verbose_name='total_sum')),
                ('payment_id', models.CharField(max_length=50, verbose_name='payment_id')),
                ('status', models.PositiveSmallIntegerField(verbose_name='status')),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
                ('updated_at', models.DateTimeField(verbose_name='updated_at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'purchases',
            },
        ),
        migrations.CreateModel(
            name='Purchase_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='amount')),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
                ('updated_at', models.DateTimeField(verbose_name='updated_at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.products')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.purchases')),
            ],
            options={
                'db_table': 'purchase_products',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.PositiveBigIntegerField(verbose_name='card')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
                ('updated_at', models.DateTimeField(verbose_name='updated_at')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.purchases')),
            ],
            options={
                'db_table': 'payments',
            },
        ),
    ]