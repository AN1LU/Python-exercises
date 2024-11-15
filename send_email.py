import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

import pandas as pd
from credentials import *

def send_email (destinatario, usuario, asunto, mensaje): 
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(USER_MAIL, PASSWORD)

        msg = MIMEMultipart()
        msg['From'] = usuario
        msg['Subject'] = asunto
        msg['To'] = ', '.join(destinatario)
        msg['Bcc'] = ', '.join(CCO_EMAIL)
        msg.attach(MIMEText(mensaje))

        with open('happy face.png', 'rb') as archivo_firma:
            firma_imagen = MIMEImage(archivo_firma.read())
            firma_imagen.add_header('Content-Disposition', 'attachment', filename='happy face.png')
            msg.attach(firma_imagen)

        server.sendmail(USER_MAIL, destinatario ,msg.as_string())
if __name__ == '__main__':
    df = pd.read_csv('info.csv', delimiter=',')
    for indice, fila in df.iterrows():
        nombre = fila.loc['nombre']
        correo = fila.loc['correo'] 
        id = fila.loc['ID']
        print(nombre, correo, id)

        send_email(
            usuario="Premiador",
            destinatario=[correo],
            asunto="Ya tenemos su registro ",
            mensaje=f"Estimado {nombre}, \n\nPor medio de la presente le comunicamos que su registro es ID:{id}.",
        )
