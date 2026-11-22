import os

import discord
from discord import app_commands
from dotenv import load_dotenv


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready() -> None:
    await tree.sync()
    print(f"Logged in as {client.user}")


@tree.command(name="ping", description="Check whether the bot is responding")
async def ping(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("Pong!")


@tree.command(name="hello", description="Greet a Discord member")
@app_commands.describe(member="The member to greet")
async def hello(interaction: discord.Interaction, member: discord.Member | None = None) -> None:
    target = member or interaction.user
    await interaction.response.send_message(f"Hello, {target.mention}! 👋")


@tree.command(name="info", description="Show basic server information")
async def info(interaction: discord.Interaction) -> None:
    guild = interaction.guild
    if guild is None:
        await interaction.response.send_message("This command can only be used in a server.")
        return

    await interaction.response.send_message(
        f"**Server:** {guild.name}\n"
        f"**Members:** {guild.member_count}\n"
        f"**Server ID:** {guild.id}"
    )


def main() -> None:
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN is not set. Copy .env.example to .env and add your bot token.")

    client.run(token)


if __name__ == "__main__":
    main()
