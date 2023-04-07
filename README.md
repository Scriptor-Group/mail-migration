# Email Migration Tool

Cet outil permet de migrer facilement des e-mails entre deux serveurs de messagerie IMAP. Il gère la migration des dossiers, des flags (étiquettes) et des erreurs lors du transfert des e-mails.

## Prérequis
- Python 3.6 ou ultérieur
- Les bibliothèques Python suivantes sont requises :
  - imaplib
  - email


## Installation
1. Clonez ce dépôt ou téléchargez le fichier email_migration.py sur votre ordinateur.
2. Assurez-vous que Python 3.6 ou ultérieur est installé sur votre système.
3. Aucune dépendance externe n'est requise.
  
## Utilisation

1. Ouvrez un terminal ou un invite de commande.
2. Naviguez jusqu'au répertoire où se trouve le fichier email_migration.py.
3. Exécutez le script avec les arguments appropriés pour les serveurs de messagerie source et de destination, comme suit :
```bash
python email_migration.py --src_server imap.source.com --src_username source_user --dest_server imap.destination.com --dest_username destination_user
```
4. Lorsque vous êtes invité, saisissez les mots de passe pour les comptes de messagerie source et de destination.
5. Le script migrera les e-mails entre les serveurs de messagerie et affichera l'état de la migration.

## Remarques
- Assurez-vous d'avoir les identifiants et les mots de passe corrects pour les comptes de messagerie source et de destination.
- Ce script ne supprime pas les e-mails du serveur source. Si vous souhaitez supprimer les e-mails après la migration, faites-le manuellement ou ajoutez cette fonctionnalité au script.
- Le script ne gère pas la migration des contacts, des calendriers ou d'autres données non liées aux e-mails.
- Testez d'abord la migration avec un petit nombre d'e-mails pour vous assurer que tout fonctionne correctement.

## Support
Si vous rencontrez des problèmes ou avez des questions, veuillez ouvrir une issue sur la page du projet.

## Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.