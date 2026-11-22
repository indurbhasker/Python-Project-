# Python Discord Bot

A starter Discord bot using `discord.py` with slash commands.

## Commands

- `/ping` — check whether the bot is responding
- `/hello [member]` — greet yourself or another member
- `/info` — show basic information about the current server

## Setup

1. Create a Discord application and bot at the [Discord Developer Portal](https://discord.com/developers/applications).
2. Enable the **Server Members Intent** only if you need member-specific features beyond this starter.
3. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env`, then add your bot token:

   ```text
   DISCORD_TOKEN=your-token-here
   ```

5. Invite the bot to a server with the `bot` and `applications.commands` scopes, then run:

   ```powershell
   python bot.py
   ```
