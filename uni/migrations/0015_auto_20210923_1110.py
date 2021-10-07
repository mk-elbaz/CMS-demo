# Generated by Django 3.2.6 on 2021-09-23 11:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0014_auto_20210921_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='rate',
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='studentRating', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tutorRating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]