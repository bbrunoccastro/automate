import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

# Configuração do Twilio (substitua com suas credenciais)
account_sid = 'sua account id'
auth_token = 'seu auth token'
phone_number = 'whatsapp:numero twillio'
whatsapp_recipient = 'whatsapp:seu whatsappPP'

# URL do site a ser verificado
site_url = ('https://www.terra.com.br')

# Palavras-chave a serem procuradas
palavras_chave = ['antony', 'declaração', 'Americano', 'Pastor', 'bruno']


# Função para verificar o site e enviar mensagem no WhatsApp
def verificar_site_e_enviar_mensagem():
    # Faz a solicitação HTTP para o site
    response = requests.get(site_url)

    if response.status_code == 200:
        # Analisa o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extrai o texto do site
        texto_do_site = soup.get_text()

        # Verifica se alguma das palavras-chave está no texto
        for palavra_chave in palavras_chave:
            if palavra_chave.lower() or palavra_chave.upper() in texto_do_site:
                # Envia mensagem no WhatsApp usando o Twilio
                client = Client(account_sid, auth_token)
                mensagem = "A palavra-chave " + palavra_chave + " foi encontrada no site: " + site_url
                message = client.messages.create(
                    body=mensagem,
                    from_=phone_number,
                    to=whatsapp_recipient
                )
                print("Mensagem enviada para {whatsapp_recipient}: {message.sid}")
            elif palavra_chave not in texto_do_site:
                # Envia mensagem no WhatsApp usando o Twilio
                client = Client(account_sid, auth_token)
                mensagem = "A palavra-chave " + palavra_chave + " NÃO foi encontrada no site: " + site_url
                messages = client.messages.create(
                    body=mensagem,
                    from_=phone_number,
                    to=whatsapp_recipient
                )
    else:
        print("Não foi possível acessar o site. Código de status: {response.status_code}")


if __name__ == "__main__":
    verificar_site_e_enviar_mensagem()
