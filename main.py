import os
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

facts = ["Машинное масло – как инвокер на шорте. 4 литра масла достаточно для того, чтобы отравить 4 млн литров жидкости.(и пуджей...) Кстати, такой объём воды используют всего 50 человек за 1 год.", "Пляжи Калифорнии зафиксированы, как одни из наиболее чистых на планете. Но уборка территории позволила выявить проблему и тут: найдено до 330 000 окурков.", "Ежегодно до 5 тонн косметических средств попадает в реки, моря и океаны.(и на мидл)", "20 лет назад Швеция отказалась от мусорных полигонов и внедрила по всей стране раздельный сбор мусора.", "Загрязнение воды становится причиной смерти людей и пуджей: каждый день на планете из-за этого погибает 14 000 человеко-пуджей."]
d = ['Не покупать пакеты.', 'Используйте экологические средства гигиены.', 'Сортируйте мусор.', 'Высаживайте деревья и кустарники.']

@bot.command
async def factos(ctx):
    await ctx.send(random.choice(facts))

@bot.command
async def defend(ctx):
    await ctx.send(random.choice(d))

@bot.command
async def vict(ctx):
    await ctx.send("Ты сортируешь мусор? $q1yes = Да $q1no = Нет")

@bot.command
async def q1yes(ctx):
    await ctx.send("Круто!")

@bot.command
async def q1no(ctx):
    await ctx.send("Хай пудж...")

@bot.command
async def econews(ctx):
    await ctx.send("Две тысячи деревьев высадят в Ингушетии в рамках акции 'Сохраним лес' - https://ria.ru/20240924/ingushetiya-1974485829.html")
    await ctx.send("Айтишники и экологи? Кто еще нужен стране - https://radiosputnik.ru/20240916/karera-1972003943.html")

@bot.command
async def dexi(ctx):
    await ctx.send("Пластик                от 6 месяцев до 700 лет")
    await ctx.send("Пластиковые бутылки	   более 100 лет")
    await ctx.send("Стекло                 более 1000 лет")
    await ctx.send("Влажные салфетки       от 100 лет")

@bot.command()
async def memscatsanddogs(ctx):
    img_name = random.choice(os.listdir('img'))
    with open(f'img/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

bot.run('MTI4MTk3MDg2NzQyNDg1ODIwMw.Gf6ZqW.dFXGX5AE5q1mSxLw_S_lsI3PHgbH39xQOlG0GA')
