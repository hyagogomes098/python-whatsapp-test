# Projeto WhatsApp Automation (Supabase + Z-API)

## 📌 Descrição
Este projeto automatiza o envio de mensagens via WhatsApp utilizando Python, Supabase e Z-API.

---

## 🚀 Fluxo do projeto

1. Leitura de contatos no Supabase  
2. Limpeza de números de telefone  
3. Geração de mensagem personalizada  
4. Envio via Z-API (WhatsApp)

---

## 🧠 Tecnologias utilizadas

- Python
- Supabase
- Z-API
- dotenv (variáveis de ambiente)
- requests

---

## ⚙️ Como executar o projeto

1. Instalar dependências: pip install supabase python-dotenv requests

2. Criar arquivo `.env`: SUPABASE_URL=sua_url
SUPABASE_KEY=sua_key

3. Rodar o projeto: python main.py

---

## 📊 Resultado esperado

O sistema:
- Busca contatos no banco
- Formata o número
- Envia mensagem personalizada via WhatsApp

---

## ✉️ Mensagem enviada
Olá, <nome> tudo bem com você?
## 👨‍💻 Autor

Hyago Gomes  
Desenvolvido como parte de um desafio de estágio em Python