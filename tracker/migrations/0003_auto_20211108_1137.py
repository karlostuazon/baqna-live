# Generated by Django 3.2.4 on 2021-11-08 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20211108_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='bcg_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='dt1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='dt2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='dt3_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='dtbooster1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='dtbooster2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hepb1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hepb2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hepb3_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hi1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hi2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hi3_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hibooster1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hpv1of2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hpv1of3_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hpv2of2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hpv2of3_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hpv3of3_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='inacthepa1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='inacthepa2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='influ1of2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='influ2of2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ip1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ip2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ip3_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ipbooster1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ipbooster2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='jap1of2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='jap2of2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='measles_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mening_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mmr1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mmr2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='pcv1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='pcv2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='pcv3_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='pcvbooster1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='rota1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='rota2_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='rota3_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='tdbooster3_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='typhoid_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='vari1_brand',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='vari2_brand',
        ),
        migrations.CreateModel(
            name='PatientVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bcg_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('hepb1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('hepb2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('dt1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('ip1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('hi1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('pcv1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('rota1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('dt2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('ip2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('hi2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('pcv2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('rota2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('hepb3_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('dt3_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('ip3_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('hi3_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('pcv3_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('rota3_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('influ1of2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('measles_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('jap1of2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('influ2of2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('mmr1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('vari1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('dtbooster1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('ipbooster1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('hibooster1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('pcvbooster1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('inacthepa1_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('inacthepa2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('mening_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('typhoid_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('jap2of2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('dtbooster2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('ipbooster2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('mmr2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('vari2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('tdbooster3_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('hpv1of2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('hpv2of2_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('hpv1of3_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('hpv2of3_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('hpv3of3_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('bcg_date', models.DateField(blank=True, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.patient')),
            ],
        ),
    ]
