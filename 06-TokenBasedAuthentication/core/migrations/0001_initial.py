# Generated by Django 3.2.10 on 2021-12-10 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JiraToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='jira_token', to=settings.AUTH_USER_MODEL, verbose_name='Jira User')),
            ],
        ),
    ]
