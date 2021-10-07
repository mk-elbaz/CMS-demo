# Generated by Django 3.2.6 on 2021-09-23 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0015_auto_20210923_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentGrade', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjGrade', to='uni.subject'),
        ),
    ]