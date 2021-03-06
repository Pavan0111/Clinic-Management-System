# Generated by Django 3.1.7 on 2021-08-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practitioners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('position', models.CharField(choices=[('Nurse', 'Nurse'), ('Clinical Officer', 'Clinical Officer'), ('Public Health Officer', 'Public Health Officer'), ('Cleaner', 'Cleaner'), ('Security', 'Security'), ('Driver', 'Driver'), ('Counselor', 'Counselor'), ('Nutritionist', 'Nutritionist')], max_length=100)),
                ('employment_date', models.DateTimeField()),
                ('shift', models.CharField(choices=[('Day', 'Day'), ('Night', 'Night')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
