# Generated by Django 4.1.6 on 2023-02-26 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vehicles", "0002_vehicle_currency"),
        ("units", "0001_initial"),
        ("currency", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Grade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Fill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qty", models.DecimalField(decimal_places=3, max_digits=8)),
                ("station", models.CharField(max_length=50)),
                ("full", models.BooleanField(default=True)),
                (
                    "local_price_per_unit",
                    models.DecimalField(decimal_places=3, max_digits=7),
                ),
                (
                    "account_price_per_unit",
                    models.DecimalField(decimal_places=3, max_digits=7),
                ),
                (
                    "fuel_grade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="fuel.grade"
                    ),
                ),
                (
                    "local_currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="currency.currency",
                    ),
                ),
                (
                    "local_unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="units.unit"
                    ),
                ),
                (
                    "meter_reading",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicles.meterreading",
                    ),
                ),
            ],
        ),
    ]
