import discord
import os, random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def meme(ctx):
    lista = os.listdir('images')

    imagem = random.choice(lista)


    with open(f'images/{imagem}', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def reciclar(ctx, material):
    if material == 'plastico':

        await ctx.send('Adolescentes podem reutilizar garrafas e potes plásticos como organizadores ou vasos. Lave os plásticos antes de descartar e separe para reciclagem. Assim, é possível reduzir o lixo em casa de forma simples.')
    
    elif material == 'metal':
        await ctx.send('Adolescentes podem reutilizar latas como organizadores ou vasos, evitando jogar fora. Lave os metais antes de descartar e separe para reciclagem corretamente. Pequenas atitudes assim já ajudam a reduzir o lixo em casa.')
    elif material == 'papel':
        await ctx.send('Adolescentes podem reutilizar folhas de papel como rascunho ou para anotações. Caixas e embalagens podem virar organizadores ou materiais de estudo. Assim, é possível reduzir o lixo em casa de forma simples.')
    elif material == 'vidro':
        await ctx.send('Adolescentes podem reutilizar vidro, como potes e garrafas, para guardar alimentos ou organizar objetos. É importante lavar bem antes de reutilizar ou reciclar. Assim, dá pra reduzir o lixo em casa de forma prática e sustentável.')
    elif material == 'tecido':
        await ctx.send('Adolescentes podem reutilizar tecidos, como roupas antigas, para fazer panos de limpeza ou customizar peças. Também dá para transformar em bolsas ou capas de objetos. Assim, reduzem o lixo em casa de forma criativa e sustentável.')
    
bot.run("")

    

