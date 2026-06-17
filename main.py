from supabase import create_client
import os
from dotenv import load_dotenv
import requests  # 👈 ADICIONADO

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

response = supabase.table("Contatos").select("*").limit(3).execute()

def limpar_numero(numero):
    return "".join(filter(str.isdigit, numero))

# 👇 ADICIONADO (Z-API CONFIG)
ZAPI_INSTANCE = "3F4CA7130ED582061A328645B9B7D1FC"
ZAPI_TOKEN = "8C5E1AA0EB3CF94AD292768A"

# 👇 ADICIONADO (FUNÇÃO DE ENVIO)
def enviar_whatsapp(numero, mensagem):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-text"

    payload = {
        "phone": numero,
        "message": mensagem
    }

    response = requests.post(url, json=payload)

    print("Enviado para:", numero)
    print(response.text)

for c in response.data:
    nome = c["Nome"]
    telefone = limpar_numero(c["Telefone"])

    mensagem = f"Olá, {nome} tudo bem com você?"

    print(nome, telefone)
    print(mensagem)

    # 👇 ADICIONADO (ENVIO REAL)
    enviar_whatsapp(telefone, mensagem)