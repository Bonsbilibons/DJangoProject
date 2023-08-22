# Generated by Django 4.2.2 on 2023-07-08 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_delete_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=120, verbose_name='title')),
                ('comment', models.TextField(max_length=1250, verbose_name='comment')),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.products')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
