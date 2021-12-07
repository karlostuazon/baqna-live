# Generated by Django 3.1.7 on 2021-11-06 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0033_patient_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='attending_doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='docpatient', to='tracker.physician'),
        ),
    ]