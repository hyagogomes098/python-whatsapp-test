from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

response = supabase.table("Contatos").select("*").limit(3).execute()

def limpar_numero(numero):
    return "".join(filter(str.isdigit, numero))

for c in response.data:
    nome = c["Nome"]
    telefone = limpar_numero(c["Telefone"])

    print(nome, telefone)