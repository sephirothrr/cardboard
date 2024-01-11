# Generated by Django 4.1.13 on 2024-01-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hunts", "0015_alter_hunt_id_alter_huntsettings_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="huntsettings",
            name="create_channel_by_default",
            field=models.BooleanField(
                default=True,
                help_text="Toggles whether puzzles should have chat channels created by default",
            ),
        ),
        migrations.AlterField(
            model_name="huntsettings",
            name="discord_archive_category",
            field=models.CharField(
                blank=True,
                default="archive",
                help_text="The category name to archive all Discord channels for solved puzzles in",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="huntsettings",
            name="discord_devs_role",
            field=models.CharField(
                blank=True,
                default="dev",
                help_text="The Discord role for the people maintaining the Cardboard instance, in case of problems",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="huntsettings",
            name="discord_guild_id",
            field=models.CharField(
                blank=True,
                help_text='The id of your Discord server. This can be found on the "Widget" page in the Server Settings',
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="huntsettings",
            name="discord_metas_category",
            field=models.CharField(
                blank=True,
                default="metas",
                help_text="The category name to create all metas in",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="huntsettings",
            name="discord_puzzle_announcements_channel_id",
            field=models.CharField(
                blank=True,
                help_text="The id of the Discord channel to make puzzle announcements in.\n        This channel can get noisy and is recommended to be its own separate channel.\n        This ID can be found by enabling Developer Mode in Discord and right-clicking on the channel",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="huntsettings",
            name="discord_unassigned_text_category",
            field=models.CharField(
                blank=True,
                default="text [unassigned]",
                help_text="The category name to create all unassigned Discord text channels in",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="huntsettings",
            name="discord_unassigned_voice_category",
            field=models.CharField(
                blank=True,
                default="voice [unassigned]",
                help_text="The category name to create all unassigned Discord voice channels in",
                max_length=128,
            ),
        ),
    ]
