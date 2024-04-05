import string
import secrets

characters = string.ascii_letters + string.punctuation  + string.digits

password_length = secrets.choice(range(10, 17))
password = ''.join(secrets.choice(characters) for x in range(password_length))

# Dopo aver raccolto i dati dell'account e generato la password
account = input('Tipo di account: ')
mail = input("Inserisci mail: ")

with open(account + ".txt", "w") as text_file:
    text_file.write(f"--- {account} ---\n\n")
    text_file.write(f"Mail: {mail}\n")
    text_file.write(f"Password: {password}\n")
exit
