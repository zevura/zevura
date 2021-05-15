import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='!', description="This is a Helper Bot")


@bot.command()
async def machdichnützlich(ctx):
    await ctx.send('Nutzlos bist du! Ich Mach mich jetzt nützlich.')


@bot.command()
async def terraria(ctx):
    await ctx.send('Jemand wartet bis der Terraria Server startet')

@bot.command(pass_context=True)
async def setrole(ctx):
    guild = ctx.guild
    await guild.create_role(name="Schimmel", colour=discord.Colour(0x1CF110))


@bot.command(pass_context=True)
async def schimmelvernichtung(ctx, user: discord.Member):
    await ctx.send('Schimmelvernichtung gestartet')
    role = discord.utils.get(ctx.guild.roles, name="Schimmel")
    await user.add_roles(role)
    await ctx.send(f"Schimmelvernichtung erfolgreich durchgeführt! {user} hat die Rolle >Schimmel< erhalten.")

@bot.command(pass_context=True)
async def nutzlos(ctx, user: discord.Member):
    await ctx.send(f"Mach dich nützlich {user}")


@bot.command()
async def startterraria(ctx):
    await ctx.send('@Yyhra#3346 Starte den Terraria Server!')


@bot.command()
async def sendhelp(ctx):
    await ctx.send('Hier sind alle Commands:')
    await ctx.send('!sendhelp  >>  Zeigt alle Commands')
    await ctx.send('!machdichnützlich  >>  Ich mach mich Nützlich')
    await ctx.send('!terraria  >>  Terraria Gameplay')
    await ctx.send('!startterraria  >>  fordert den Hoster auf das Spiel zu starten')
    await ctx.send('```css\n !schimmelvernichtung @user  >>  Vernichtet Schimmel ```')
    await ctx.send('```css\n !nutzlos @user  >>  Der Nutzer soll sich nützlich machen ```')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Egg Shooter",url="https://www.crazygames.com/game/shellshockersio"))
    print('My Ready is Body')


@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/accountname')
        await bot.process_commands(message)


bot.run('ODQyNzkwNTUyMjU2NjQzMDc5.YJ6b3Q.n92yW3qEL_2u5YOiV7MZoXO5afA')


