# Generated by Django 4.1.2 on 2022-11-08 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinic', '0003_remove_appointment_veterinary'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Veterinary',
        ),
        migrations.AddField(
            model_name='appointment',
            name='veterinary',
            field=models.ForeignKey(default='7aa46696-ae31-4756-b2af-6ae9409a8d58', on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL, verbose_name='Veterinário'),
            preserve_default=False,
        ),
    ]