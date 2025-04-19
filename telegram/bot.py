from telegram import Bot
from config import settings

bot = Bot(token=settings.TELEGRAM_TOKEN)

def enviar_produto(produto):
    mensagem = f"*{produto['product_title']}*\nPreço: R${produto['price']/100000:.2f}\n[Compre aqui]({produto['short_url']})"
    bot.send_photo(
        chat_id=settings.TELEGRAM_CHAT_ID,
        photo=produto['product_image'],
        caption=mensagem,
        parse_mode='Markdown'
    )
