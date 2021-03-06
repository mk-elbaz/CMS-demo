# Generated by Django 3.2.6 on 2021-09-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('birthDate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('grade', models.CharField(max_length=2)),
                ('faculty', models.CharField(choices=[('a', 'None'), ('b', 'Computer Science'), ('c', 'Business'), ('d', 'Engineering'), ('e', 'Design'), ('f', 'Medicine'), ('g', 'Applied Arts')], default='None', max_length=1)),
                ('nationality', models.CharField(max_length=20)),
            ],
        ),
    ]
