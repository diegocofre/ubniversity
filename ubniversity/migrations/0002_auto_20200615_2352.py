# Generated by Django 3.0.6 on 2020-06-16 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ubniversity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='id_teacher',
            new_name='teacher',
        ),
        migrations.RenameField(
            model_name='courseclass',
            old_name='id_course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='courseday',
            old_name='id_course',
            new_name='course',
        ),
        migrations.AlterField(
            model_name='courseclass',
            name='attendant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='courseday',
            name='week_day',
            field=models.SmallIntegerField(choices=[(0, 'None'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday'), (8, 'Mon/Fri')]),
        ),
    ]