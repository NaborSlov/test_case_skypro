# Generated by Django 4.1.5 on 2023-01-20 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('type', models.PositiveIntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')])),
                ('indebtedness', models.DecimalField(decimal_places=2, default=0.0, max_digits=25)),
                ('hierarchy', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('vendor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vendors', to='network.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='network.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('house_number', models.SmallIntegerField()),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='network.vendor')),
            ],
        ),
    ]
