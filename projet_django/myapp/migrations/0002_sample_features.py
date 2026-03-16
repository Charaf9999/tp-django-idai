from django.db import migrations


def create_features(apps, schema_editor):
    Feature = apps.get_model('myapp', 'Feature')
    Feature.objects.create(name='Architecture Django', details='Organisation simple du projet avec urls, vues et templates.')
    Feature.objects.create(name='Compteur de mots', details='Formulaire permettant de compter les mots saisis par l\'utilisateur.')
    Feature.objects.create(name='Authentification', details='Inscription, connexion et déconnexion avec le système Django.')


def delete_features(apps, schema_editor):
    Feature = apps.get_model('myapp', 'Feature')
    Feature.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_features, delete_features),
    ]
