# В файле миграции (например, spotify/migrations/0005_update_refresh_token_values.py)
from django.db import migrations

def update_refresh_token(apps, schema_editor):
    SpotifyToken = apps.get_model('spotify', 'SpotifyToken')
    SpotifyToken.objects.filter(refresh_token__isnull=True).update(refresh_token='default_refresh_token')

class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0004_alter_spotifytoken_refresh_token_vote'),
    ]

    operations = [
        migrations.RunPython(update_refresh_token),
    ]
