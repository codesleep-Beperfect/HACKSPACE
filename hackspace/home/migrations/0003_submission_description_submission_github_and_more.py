# Generated by Django 4.1.3 on 2023-04-22 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_remove_submission_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="Description",
            field=models.TextField(blank=True, verbose_name="summary"),
        ),
        migrations.AddField(
            model_name="submission",
            name="Github",
            field=models.TextField(
                default=django.utils.timezone.now, verbose_name="github"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="submission",
            name="Hackathon_enddate",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="hackathonenddate"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="submission",
            name="Hackathon_name",
            field=models.TextField(
                default=django.utils.timezone.now, verbose_name="hackathonname"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="submission",
            name="Hackathon_startdate",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="hackathonstartdate"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="submission",
            name="Other",
            field=models.TextField(blank=True, verbose_name="others"),
        ),
        migrations.AddField(
            model_name="submission",
            name="Summary",
            field=models.TextField(blank=True, verbose_name="summary"),
        ),
        migrations.AddField(
            model_name="submission",
            name="Title",
            field=models.TextField(
                default=django.utils.timezone.now, verbose_name="title"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="submission",
            name="image",
            field=models.ImageField(default=None, upload_to=""),
        ),
        migrations.AddField(
            model_name="submission",
            name="last_edited",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="submission",
            name="pub_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
