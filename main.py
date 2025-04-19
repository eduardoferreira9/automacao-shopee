from shopee.api import buscar_produtos
from telegram.bot import enviar_produto

def main():
    produtos = buscar_produtos()
    for produto in produtos:
        enviar_produto(produto)

if __name__ == "__main__":
    main()
