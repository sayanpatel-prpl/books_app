# Generated by Django 4.1 on 2024-04-07 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="member",
            old_name="MemberID",
            new_name="memberid",
        ),
    ]
