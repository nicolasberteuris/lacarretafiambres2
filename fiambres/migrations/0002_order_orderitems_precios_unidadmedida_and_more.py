# Generated by Django 4.0.4 on 2022-07-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiambres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amt', models.FloatField()),
                ('fecha_order', models.DateField(auto_now_add=True)),
                ('estado_orden', models.BooleanField(default=False, verbose_name='Iniciado')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'db_table': 'order',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
            ],
            options={
                'verbose_name': 'orderitem',
                'verbose_name_plural': 'orderitems',
                'db_table': 'orderitem',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Precios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Precio',
                'verbose_name_plural': 'Precios',
                'db_table': 'precios',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'unidadmedida',
                'verbose_name_plural': 'unidadmedidas',
                'db_table': 'unidadmedida',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]