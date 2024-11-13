

import random as rand
import discord
from discord.ext import commands
TOKEN = "Put your bot token here"
PREFIX = "."

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
def main():
    print(TOKEN)
    if TOKEN is None:

        return ("no token provided.")
    try:


        bot.run(TOKEN)
    except discord.PrivilegedIntentsRequired as error:
        print("Invalid token")
        print(error)
        return error
client = discord.Client(intents=discord.Intents.all())


@bot.command(name="SecretSanta" , aliases=['S'])
async def santa(ctx: commands.Context, *args):

    user = discord.ext.commands.UserConverter()
    users = []
    for arg in args:
        users.append(await user.convert(ctx,arg))
    rand.shuffle(users)
    users.append(users[0])
    for i in range(len(users) - 1):
        try:



            query = "!this might be real, ask Aaron!\nYou need to give presents to " + users[i + 1].name + " this secret santa"
            await users[i].send(query)
            await ctx.send(f':white_check_mark: Your message/s has been sent')
        except Exception as e:
            print(e)
            await ctx.send('fuck you im killing myself')


main()
