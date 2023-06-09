# Generated by Django 4.1.7 on 2023-05-17 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=64)),
                ('eno', models.IntegerField()),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=130)),
            ],
        ),
        migrations.CreateModel(
            name='proxyEmployee1',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.employee')),
            ],
            bases=('testapp.employee',),
        ),
        migrations.CreateModel(
            name='proxyEmployee2',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.employee')),
            ],
            bases=('testapp.employee',),
        ),
    ]
