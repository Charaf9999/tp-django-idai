TP MI-GUIDE DJANGO - GUIDE D'UTILISATION ET DE SOUMISSION
========================================================

1) CONTENU DU DOSSIER
- rapport_TP_Django_IDAI.docx : rapport Word prêt à remettre (avec sections, explications et zones à compléter pour les captures)
- requirements.txt : dépendances Python
- .gitignore : fichiers à ignorer dans Git
- projet_django/ : projet Django complet

2) OUTILS NECESSAIRES
- Python 3 installé
- VS Code (recommandé)
- Terminal / Invite de commandes
- Connexion Internet uniquement pour installer Django si ce n'est pas déjà fait

3) ETAPES RAPIDES
A. Décompresser le fichier ZIP dans un seul dossier
B. Ouvrir le dossier projet_django dans VS Code
C. Ouvrir un terminal dans ce dossier
D. Créer l'environnement virtuel :
   python -m venv monenv
E. Activer l'environnement virtuel :
   - Windows : monenv\Scripts\activate
   - Linux/Mac : source monenv/bin/activate
F. Installer Django :
   pip install -r ../requirements.txt
G. Appliquer les migrations :
   python manage.py migrate
H. Lancer le serveur :
   python manage.py runserver
I. Ouvrir le navigateur à l'adresse : http://127.0.0.1:8000/

4) CREATION DU SUPER-UTILISATEUR
Pour accéder à l'interface admin :
python manage.py createsuperuser
Puis suivre les questions dans le terminal.
Ensuite ouvrir :
http://127.0.0.1:8000/admin/

5) CE QUE VOUS DEVEZ TESTER
- La page d'accueil s'affiche
- Le compteur de mots fonctionne
- L'inscription fonctionne
- La connexion fonctionne
- La déconnexion fonctionne
- L'admin fonctionne
- Le modèle Feature apparaît dans l'admin

6) CAPTURES D'ECRAN A PRENDRE
Prenez au minimum ces captures :
1. python --version
2. Activation de l'environnement virtuel
3. Installation de Django
4. Création du projet / structure du dossier dans VS Code
5. Page d'accueil Django locale
6. Page de votre projet personnalisé
7. Résultat du compteur de mots
8. Interface admin avec le modèle Feature
9. Formulaire Register
10. Formulaire Login

7) POUR GITHUB
Dans le dossier projet_django, exécuter :
   git init
   git add .
   git commit -m "TP Django"
   git branch -M main
   git remote add origin VOTRE_LIEN_GITHUB
   git push -u origin main

8) POUR L'ENVOI AU PROF
- Si Gmail accepte le ZIP, envoyez le ZIP + le rapport DOCX
- Si Gmail bloque le ZIP, envoyez seulement le rapport DOCX par mail
- Mettez le projet ZIP sur Google Drive et partagez le lien
- Gardez la structure du projet inchangée

9) IMPORTANT
- Remplacez dans le rapport le nom de l'ordinateur par le nom réel de votre machine
- Ajoutez vos propres captures locales dans le rapport avant l'envoi final
- Testez tout une dernière fois avant de soumettre
