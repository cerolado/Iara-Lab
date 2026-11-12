from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

with open("prompt.txt","r", encoding="utf-8") as arquivo:
    prompt_texto= arquivo.read()

modelo = ChatOpenAI(model="gpt-4o-mini")

def criar_mensagens_iniciais():
    mensagens = [SystemMessage(prompt_texto)]
    return mensagens

if __name__ == "__main__":
    mensagens = criar_mensagens_iniciais()

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair","exit","quit"]:
            print("até mais!")
            break
        mensagens.append(HumanMessage(pergunta))
        resposta = modelo.invoke(mensagens)
        print(f"Luan: {resposta.content}")
        mensagens.append(resposta)
        