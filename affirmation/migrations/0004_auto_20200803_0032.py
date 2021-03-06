# Generated by Django 3.0.8 on 2020-08-03 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('affirmation', '0003_auto_20200803_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affirmation',
            name='user',
            field=models.ForeignKey(help_text='The user that posted this article.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
