import discord
from discord.ext import commands
from main import * 

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    #Create role
    @commands.has_permissions(administrator = True)
    @commands.command(aliases = ['make_role', 'cr'])
    @commands.Cog.listener()
    async def create_role(self, ctx, name):
        guild = ctx.guild
        await guild.create_role(name = name)
        await ctx.send(f"Role **{name}** was successfully created")


    @commands.command(aliases = ['delrole', 'dr'], pass_context = True)
    @commands.has_permissions(administrator = True)
    @commands.Cog.listener()
    async def delete_role(self, ctx, name):
        role_object = discord.utils.get(ctx.message.guild.roles, name = name)
        await role_object.delete()
        await ctx.send(f"Role **{name}** was successfully deleted")
    
    #Getting Roles List with Embed 
    @commands.command(aliases = ['rl'], pass_context = True)
    @commands.has_permissions(administrator = True)
    @commands.Cog.listener()
    async def roles_list(self, ctx):
        
        roles_name = []
        roles_id = []

        for role in ctx.guild.roles:
            roles_name.append(role.name)
            roles_id.append(role.id)
        
        roles_id_str = [str(int) for int in roles_id]
       
            
        embed = discord.Embed(title = "πππ Roles List πππ", color = discord.Color.purple())
        
        embed.add_field(name = "Roles Name: ", value = "\n".join(roles_name[1::]), inline = True)
        embed.add_field(name = "Roles ID: ", value = "\n".join(roles_id_str[1::]), inline = True)
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        
        await ctx.send(embed = embed)
        
        
    
    #Role claim messages
    @commands.has_permissions(administrator = True)
    @commands.command(aliases = ['rcm'])
    async def roles_claim_message(self, ctx):
        embed = discord.Embed(title = f"π¦Hi. Here you can get roleπ¦", description = """
                            
    **Here you can choose a role based on your interests and skills. Just click on the reaction, and the role will appear for you.π

    In addition, new features and chats will open up for you, of course, both text and voice. I would also like to add that with the number of messages you send on our server, your level increases, which also gives you some rights.π

    Of course, firstly you will have to complete a survey with the bot so that we can be sure of your adequacy.π

    It is worth mentioning that in this way you can even get the role of a moderator.π**

                            
                            """,  color = discord.Color.orange())
        
        embed.set_author(name = "Universal Creator", icon_url = ctx.author.avatar_url)
        
        talant_embed = discord.Embed(title = f"Talant roles", description = f"""
                                    
    **Dev**: ***π»***
    **Gamer**: ***π?***
    **Musicant**: ***π΅***
    **Doctor**: ***π©Ί***
    **Artist**: ***π¨***
    **Writer**: ***π***
    **Trader**: ***π***
    **Businessman**: ***π₯***
    **Photographer**: ***πΈ***
    **Movie**: ***π₯***
    **NFT Collector**: ***πΈ***
                                    
                                    
                                    """, color = discord.Color.purple())
        
        await ctx.send(embed = embed)
        
        message = await ctx.send(embed = talant_embed)
        
        await message.add_reaction("π»")
        await message.add_reaction("π?")
        await message.add_reaction("π΅")
        await message.add_reaction("π©Ί")
        await message.add_reaction("π¨")
        await message.add_reaction("π")
        await message.add_reaction("π")
        await message.add_reaction("π₯")
        await message.add_reaction("πΈ")
        await message.add_reaction("π₯")
        await message.add_reaction("πΈ")
        
        
    #Getting role on reaction press
    @bot.event
    async def on_raw_reaction_add(payload):
        
        guild = bot.get_guild(payload.guild_id)
        member = payload.member
        emoji = payload.emoji.name
        
        if emoji == "π»":
            role = discord.utils.get(guild.roles, name = "Dev")
        elif emoji == 'π?':
            role = discord.utils.get(guild.roles, name = "Gamer")
        elif emoji == "π΅":
            role = discord.utils.get(guild.roles, name = "Musicant")
        elif emoji == "π©Ί":
            role = discord.utils.get(guild.roles, name = "Doctor")
        elif emoji == "π¨":
            role = discord.utils.get(guild.roles, name = "Artist")
        elif emoji == "π":
            role = discord.utils.get(guild.roles, name = "Writer")
        elif emoji == "π":
            role = discord.utils.get(guild.roles, name = "Trader")
        elif emoji == "π₯":
            role = discord.utils.get(guild.roles, name = "Businessman")
        elif emoji == "πΈ":
            role = discord.utils.get(guild.roles, name = "Photographer")
        elif emoji == "π₯":
            role = discord.utils.get(guild.roles, name = "Movie")
        elif emoji == "πΈ":
            role = discord.utils.get(guild.roles, name = "NFT Collector")
        
        await member.add_roles(role)

    #Deleting role on reaction repress    
    @bot.event
    async def on_raw_reaction_remove(payload):
        guild = bot.get_guild(payload.guild_id)
        member = payload.member
        emoji = payload.emoji.name
        
        if emoji == "π»":
            role = discord.utils.get(guild.roles, name = "Dev")
        elif emoji == 'π?':
            role = discord.utils.get(guild.roles, name = "Gamer")
        elif emoji == "π΅":
            role = discord.utils.get(guild.roles, name = "Musicant")
        elif emoji == "π©Ί":
            role = discord.utils.get(guild.roles, name = "Doctor")
        elif emoji == "π¨":
            role = discord.utils.get(guild.roles, name = "Artist")
        elif emoji == "π":
            role = discord.utils.get(guild.roles, name = "Writer")
        elif emoji == "π":
            role = discord.utils.get(guild.roles, name = "Trader")
        elif emoji == "π₯":
            role = discord.utils.get(guild.roles, name = "Businessman")
        elif emoji == "πΈ":
            role = discord.utils.get(guild.roles, name = "Photographer")
        elif emoji == "π₯":
            role = discord.utils.get(guild.roles, name = "Movie")
        elif emoji == "πΈ":
            role = discord.utils.get(guild.roles, name = "NFT Collector")
            
            
        if role is not None: 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None: 
                await member.remove_roles(role)
            else: 
                print("Member not found")
        else: 
            print("Role not found")
        
      
def setup(bot):
  bot.add_cog(Roles(bot))