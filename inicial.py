# Solución al “Challenge DEV #Caso Keyword en Gmail”

# El presente Código define la función por la cual
# ingresa a Gmail, filtra mails y los vuelca en una lista,
# la cual será importada en el archivo carga.py

import imaplib
import email
import traceback

usuario = "Colocar_Usuario"
contraseña = "Colocar_Contraseña"

resultado=[]
def leer_Gmail():

    try:

        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(usuario,contraseña)
        mail.select('inbox')
        typ, data = mail.search(None, 'ALL')
        for num in data[0].split():
            typ, data = mail.fetch(num, '(RFC822)')
            mensaje = email.message_from_bytes(data[0][1])

            if ('risk' in mensaje.__str__().lower()):
                subject = mensaje['subject']
                de = mensaje['from']
                fecha = mensaje['date']
                id_del_mensaje = mensaje['Message-ID']
                para = mensaje['to']
                vector = [id_del_mensaje,fecha,de,para,subject]
                resultado.append(vector)

        mail.close()
        mail.logout()

    except Exception as e:
        traceback.print_exc()
        print(str(e))
    return resultado
