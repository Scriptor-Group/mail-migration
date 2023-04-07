import argparse
import imaplib
import email
import getpass

# Configuration des arguments
parser = argparse.ArgumentParser(
    description="Migrer les e-mails entre deux serveurs IMAP.")
parser.add_argument("--src_server", type=str, required=True,
                    help="Adresse du serveur source.")
parser.add_argument("--src_username", type=str, required=True,
                    help="Nom d'utilisateur du serveur source.")
parser.add_argument("--dest_server", type=str, required=True,
                    help="Adresse du serveur de destination.")
parser.add_argument("--dest_username", type=str, required=True,
                    help="Nom d'utilisateur du serveur de destination.")

args = parser.parse_args()

# Récupération des mots de passe
src_password = getpass.getpass("Saisissez le mot de passe du serveur source: ")
dest_password = getpass.getpass(
    "Saisissez le mot de passe du serveur de destination: ")

# Connexion aux serveurs de messagerie
src_conn = imaplib.IMAP4_SSL(args.src_server)
src_conn.login(args.src_username, src_password)

dest_conn = imaplib.IMAP4_SSL(args.dest_server)
dest_conn.login(args.dest_username, dest_password)

# Récupérer la liste des dossiers sur le serveur source
_, folders = src_conn.list()

# Fonction pour transférer les e-mails


def transfer_emails(src_conn, dest_conn, folder):
    src_conn.select(folder, readonly=True)
    dest_conn.select(folder, readonly=False)

    _, src_msg_ids = src_conn.search(None, "ALL")
    src_msg_ids = src_msg_ids[0].split()

    for msg_id in src_msg_ids:
        _, msg_data = src_conn.fetch(msg_id, "(RFC822 FLAGS)")
        msg_raw = msg_data[0][1]
        msg_flags = msg_data[1].decode("utf-8").split("FLAGS")[1].strip()[1:-1]

        msg = email.message_from_bytes(msg_raw)
        dest_conn.append(folder, msg_flags, imaplib.Time2Internaldate(
            email.utils.parsedate(msg['date'])), msg_raw)


# Transfert des e-mails pour chaque dossier
for folder in folders:
    folder_name = folder.decode().split(' "/" ')[1]

    # Création du dossier sur le serveur de destination s'il n'existe pas
    dest_conn.create(folder_name)

    try:
        transfer_emails(src_conn, dest_conn, folder_name)
        print(f"Migration du dossier {folder_name} terminée.")
    except Exception as e:
        print(f"Erreur lors de la migration du dossier {folder_name}: {e}")

# Déconnexion des serveurs de messagerie
src_conn.logout()
dest_conn.logout()

print("Migration des e-mails terminée.")
