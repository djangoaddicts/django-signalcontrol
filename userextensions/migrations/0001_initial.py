
from django.conf import settings
from django.db import migrations, models
from django.apps import apps
import django.db.models.deletion


def add_user_preferences(apps, schema_editor):
    """ add UserPreference entry for each existing user """
    User = apps.get_model('auth', 'User')
    UserPreference = apps.get_model('userextensions', 'UserPreference')
    for user in User.objects.all():
        UserPreference.objects.create(user=user)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='date/time when this row was first created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='date/time this row was last updated')),
                ('name', models.CharField(help_text='name of theme', max_length=32, unique=True)),
                ('css_file', models.CharField(blank=True, help_text='path to css file for theme', max_length=32, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='date/time when this row was first created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='date/time this row was last updated')),
                ('name', models.CharField(blank=True, help_text='name/label/reference for this favorite', max_length=32, null=True)),
                ('url', models.URLField(help_text='url endpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='date/time when this row was first created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='date/time this row was last updated')),
                ('recents_count', models.IntegerField(blank=True, default=25, help_text='number of recents to keep a record of', null=True)),
                ('page_refresh_time', models.IntegerField(blank=True, default=5, help_text='time, in minutes, to auto-refresh a page (where applicable', null=True)),
                ('theme', models.ForeignKey(blank=True, help_text='theme to use for web pages', null=True, on_delete=django.db.models.deletion.CASCADE, to='userextensions.Theme')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preference', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserRecent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='date/time when this row was first created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='date/time this row was last updated')),
                ('url', models.URLField(help_text='url endpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userrecent',
            unique_together={('url', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='userfavorite',
            unique_together={('url', 'user')},
        ),

        migrations.RunPython(add_user_preferences)
    ]
