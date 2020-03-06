if __name__ == '__main__':
    print("This script should not be executed by itself !")
    exit()

import discord

class Client(discord.Client):
    def __init__(self, token, prefix):
        discord.Client.__init__(self)
        self.prefix = prefix
        self.run(token)

    async def on_ready(self):
        print("Logged in as {} !".format(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith(self.prefix + 'ping'):
            await message.channel.send('Pong !')