# Generated by Django 4.1.7 on 2023-03-01 08:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_rename_session_medicsappointment_appointment_session_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="medicsappointment",
            old_name="appointment_staus",
            new_name="appointment_status",
        ),
    ]
