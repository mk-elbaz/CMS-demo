# Generated by Django 3.2.6 on 2021-09-18 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0005_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('students', models.ManyToManyField(blank=True, default=None, related_name='subjectStudents', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjectTutor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
