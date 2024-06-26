# Generated by Django 4.1.13 on 2024-05-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ltos", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lecture",
            name="lecture_name",
        ),
        migrations.RemoveField(
            model_name="lecture",
            name="user",
        ),
        migrations.RemoveField(
            model_name="short",
            name="semi_title",
        ),
        migrations.AddField(
            model_name="short",
            name="keyword1",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="short",
            name="keyword2",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="short",
            name="keyword3",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="short",
            name="reason",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="short",
            name="segment",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
