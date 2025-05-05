import discord
from discord.ext import commands
from functions import generate_answer
import asyncio 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def gemma(ctx):
    if ctx.author == bot.user:
        return
    async with ctx.typing(): 
        text = ctx.message.content[7:]
        if len(text) > 0:
            
            loop = asyncio.get_running_loop()
            answer =  await loop.run_in_executor(None, generate_answer, text)
            
            if len(answer) > 2000:
                inital = 2000
                legth = len(answer)
                
                await ctx.send(answer[:2000])
                while True:
                    send_message = answer[inital:inital+2000]
                    await ctx.send(send_message)
                    inital += 2000
                    # si lo que falta  es menor a 2000 , envimaos el mensaje desde intial hasta el final
                    if legth - inital < 2000:
                        break
                is_missing = answer[inital:]
                if  len(is_missing) > 0:
                    await ctx.send(is_missing)

            else:
                await ctx.send(answer)
        else:
            await ctx.send("Porfavor escriba un mensaje.")
                
            
 
 
            
            
                

    



bot.run("")