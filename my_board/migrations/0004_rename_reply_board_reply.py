# Generated by Django 4.0 on 2021-12-30 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('my_board', '0003_reply'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='reply',
            new_name='board_reply',
        ),
    ]
