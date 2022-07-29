# Generated by Django 4.0.6 on 2022-07-28 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precioUnidad', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('cantidadExistencia', models.IntegerField(default=0)),
                ('IVAproducto', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidadesVendidas', models.IntegerField(default=1)),
                ('fecha', models.DateTimeField(verbose_name='fecha de venta')),
                ('tipoPago', models.CharField(choices=[('EF', 'Efectivo'), ('TA', 'Tarjeta')], default='EF', max_length=200)),
                ('subTotal', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('vendedor', models.CharField(max_length=200)),
                ('IVAtotal', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('id_producto', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
        ),
    ]
