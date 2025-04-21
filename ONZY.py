import pandas as pd
from datetime import datetime
import smtplib
from email.message import EmailMessage

print("📥 Lecture du fichier anniv.csv...")
try:
    df = pd.read_csv("anniv.csv")
    print("✅ Fichier chargé avec succès.")
except FileNotFoundError:
    print("❌ ERREUR : Le fichier 'anniv.csv' est introuvable.")
    exit()


today = datetime.now().strftime('%m-%d')
print(f"📅 Date du jour : {today}")

anniversaire_trouve = False

for index, row in df.iterrows():
    anniversaire = datetime.strptime(row['date_naissance'], '%Y-%m-%d').strftime('%m-%d')
    print(f"🔍 Vérifie : {row['prenom']} ({row['date_naissance']})")

    if anniversaire == today:
        anniversaire_trouve = True
        print(f"🎉 C'est l'anniversaire de {row['prenom']} ! Envoi du message...")

        msg = EmailMessage()
        msg['Subject'] = "🎉 Joyeux anniversaire !"
        msg['From'] = "sakinewissal652@gmail.com"
        msg['To'] = row['email']
        msg.set_content(f"Salut {row['prenom']},\n\nJoyeux anniversaire ! 🎂🎈\n\nPasse une excellente journée !")

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login("sakinewissal652@gmail.com", "00000")
                smtp.send_message(msg)
                print(f"✅ Message envoyé à {row['prenom']} ({row['email']})")
        except Exception as e:
            print(f"❌ Erreur lors de l'envoi à {row['email']} : {e}")

if not anniversaire_trouve:
    print("📭 Aucun anniversaire aujourd'hui.")
