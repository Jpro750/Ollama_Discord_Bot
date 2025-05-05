from discord.ext.commands import Bot
from ollama import AsyncClient
from discord import Intents

class MyBot(Bot):
    def __init__(self) -> None:
        intents = Intents.default()
        intents.message_content = True  
        super().__init__(command_prefix="!", intents=intents)

    async def ollama_chat(self, prompt: str) -> str:
        client = AsyncClient()

        payload = {'role': 'user', 'content': prompt}

        response = await client.chat(
            model = 'gemma3:1b',
            messages = [payload]
        )

        return response.message.content or "No response given."

bot = MyBot()

@bot.command()
async def prompt(ctx, text: str):
    reply = await bot.ollama_chat(text)

    await ctx.reply(reply)

bot.run('')
