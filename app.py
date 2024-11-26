import disnake
from disnake.ext import commands
from disnake.ui import Button, View
import asyncio

intents = disnake.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Configuration
channel_id = 1234567890  # Replace with your channel ID
category_id = None  # Replace with your category ID (optional)
view_roles = None  # Replace with your role ID (optional)

@bot.event
async def on_ready():
    print("Boosty developer: https://boosty.to/mao-mao")
    print("GitHub: https://github.com/rinnyuwu")
    print("Donation Alerts: https://www.donationalerts.com/r/rinnyuwu")
    
    channel = bot.get_channel(channel_id)
    
    if channel:
        async for message in channel.history(limit=1):
            if message.author == bot.user and message.embeds:
                print(f"Ticket message already exists: {message.jump_url}")
                return
        
        embed = disnake.Embed(
            title="Tickets",
            description="To create a ticket, react with 📩",
            color=disnake.Color.blue()
        )
        embed.set_footer(
            text="Boosty developer: https://boosty.to/mao-mao\nGitHub: https://github.com/rinnyuwu\nDonation Alerts: https://www.donationalerts.com/r/rinnyuwu"
        )
        
        button = Button(style=disnake.ButtonStyle.primary, label="Create Ticket", emoji="📩")
        view = View()
        view.add_item(button)

        await channel.send(embed=embed, view=view)

@bot.event
async def on_button_click(interaction: disnake.MessageInteraction):
    if interaction.component.label == "Create Ticket":
        guild = interaction.guild
        member = interaction.user

        category = disnake.utils.get(guild.categories, id=category_id) if category_id else None

        roles_permissions = {}
        if isinstance(view_roles, list):
            roles = view_roles
        else:
            roles = [view_roles] if view_roles else []

        for role_id in roles:
            role = guild.get_role(role_id)
            if role:
                roles_permissions[role] = disnake.PermissionOverwrite(view_channel=True)

        ticket_channel_name = f"ticket-{member.name}"

        ticket_channel = await guild.create_text_channel(
            ticket_channel_name,
            overwrites={
                guild.default_role: disnake.PermissionOverwrite(view_channel=False),
                member: disnake.PermissionOverwrite(view_channel=True),
                **roles_permissions,
            },
            category=category
        )

        close_button = Button(style=disnake.ButtonStyle.danger, label="Close Ticket", emoji="🔒")
        close_view = View()
        close_view.add_item(close_button)

        await ticket_channel.send(
            f"<@{member.id}>, please describe your issue.",
            embed=disnake.Embed(
                description="Support will be with you shortly.\nTo close this ticket, react with 🔒",
                color=disnake.Color.blue()
            ),
            view=close_view
        )

        await interaction.response.send_message(f"Ticket created: {ticket_channel.mention}", ephemeral=True)

    elif interaction.component.label == "Close Ticket":
        ticket_channel = interaction.channel
        guild = interaction.guild

        roles_permissions = {}
        if isinstance(view_roles, list):
            roles = view_roles
        else:
            roles = [view_roles] if view_roles else []

        for role_id in roles:
            role = guild.get_role(role_id)
            if role:
                roles_permissions[role] = disnake.PermissionOverwrite(view_channel=True)

        await ticket_channel.edit(
            overwrites={
                guild.default_role: disnake.PermissionOverwrite(view_channel=False),
                **roles_permissions,
            }
        )

        await interaction.response.send_message("Ticket closed, only authorized roles can view this now.", ephemeral=True)

        delete_embed = disnake.Embed(
            title="Delete Ticket",
            description="Do you want to delete this ticket? React with the button below to delete it.",
            color=disnake.Color.red()
        )
        delete_button = Button(style=disnake.ButtonStyle.danger, label="Delete Ticket", emoji="🗑️")
        delete_view = View()
        delete_view.add_item(delete_button)

        await ticket_channel.send(embed=delete_embed, view=delete_view)

    elif interaction.component.label == "Delete Ticket":
        ticket_channel = interaction.channel

        await interaction.response.send_message("This ticket will be deleted in 5 seconds.", ephemeral=False)

        await asyncio.sleep(5)
        await ticket_channel.delete()

bot.run("INSERT-TOKEN") # To run the bot, you'll need a token which you get by creating an application in the Discord Developer Portal (https://discord.com/developers/)
                        # Replace INSERT-TOKEN with your token here
                        # Make sure the token remains confidential and is not published in public sources