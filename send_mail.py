import smtplib
import numpy as np
import pandas as pd
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from soup import crypto, dolar, lista


def main():
    data_blue = dolar(lista[0])
    data_oficial = dolar(lista[1])
    data_bolsa = dolar(lista[2])
    crypto_usdc = crypto(lista[3], "usd-coin")
    crypto_usdd = crypto(lista[3], "usdd")
    crypto_usdt = crypto(lista[3], "true-usd")

    remitente = "srvn.23.03@gmail.com"
    destinatario = "santinoquiroga1432@gmail.com"

    mensaje = f'''
    <html>
    <head>
        <title>Cotización de Dólar - Precios Actualizados</title>
    </head>
    <body>
        <h1>Asunto: Cotización de Dólar - Precios Actualizados</h1>
        <p>Estimado destinatario,</p>
        <p>Quería proporcionarte la información actualizada sobre los precios de distintas modalidades de dólar:</p>

        <h2>Precio Dólar Blue</h2>
        <p>Compra: {data_blue["compra"]}</p>
        <p>Venta: {data_blue["venta"]}</p>

        <h2>Precio Dólar Oficial</h2>
        <p>Compra: {data_oficial["compra"]}</p>
        <p>Venta: {data_oficial["venta"]}</p>

        <h2>Precio Dólar Bolsa</h2>
        <p>Compra: {data_bolsa["compra"]}</p>
        <p>Venta: {data_bolsa["venta"]}</p>

        <h2>Precio Dólar Crypto</h2>
        <p>Valor USDC: {crypto_usdc["usd-coin"]["ars"]}</p>
        <p>Valor USDD: {crypto_usdd["usdd"]["ars"]}</p>
        <p>Valor USDT: {crypto_usdt["true-usd"]["ars"]}</p>


        <p>Espero que esta información te sea útil. Si tienes alguna pregunta o necesitas más detalles, duda en contactarme, no lo hagas.</p>

    </body>
    </html>

    '''

    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Dolar Hoy"
    email.set_content(mensaje, subtype="html")

    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remitente, "nkleydrdnakrmstf")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()


if __name__ == '__main__':
    main()
