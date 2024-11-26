# Discord Ticketing Bot

This bot provides a ticketing system for your Discord server. It allows users to create tickets by clicking a button. Each ticket is created as a separate text channel that is only accessible by the user who created it and certain specified roles. Once an issue is resolved, the user can close the ticket using a button, and administrators can delete the ticket after it's closed.

## Features
- Create tickets: Users can create a ticket by clicking a button.
- Role-based access: Assign roles that can view the ticket channel.
- Close and delete tickets: Users can close the ticket, and administrators can delete it after closure.
![uBQXOMh](https://github.com/user-attachments/assets/964492d0-acc4-4b75-b45e-d1090844f1e6)
![lNaJ3wU](https://github.com/user-attachments/assets/912fa46b-3c77-470c-8863-884f88d808f1)

## Requirements
- Programming Language: Python
- Required Libraries: disnake (for interacting with Discord's API)

Install the required libraries using pip:
```
pip install disnake
```

## Setup
1. Create a bot on Discord:
- Go to the [Discord Developer Portal](https://discord.com/developers/).
- Create a new application, then a bot, and obtain the bot token.
- Replace the placeholder `INSERT-TOKEN` in the code with your bot token.

2. Configure the bot:
- Set the `channel_id` to the ID of the channel where the bot should send the ticket creation message.
- Optionally, set `category_id` to the ID of the category under which the tickets should be created (this step is optional and can be skipped).
- Optionally, set `view_roles` to a list of role IDs that should have access to the ticket channels (this step is also optional).

3. Install Dependencies:
- On your Linux machine, make sure Python 3.8+ is installed. You can check this by running:
```
python3 --version
```
- Install pip if it’s not installed:
```
sudo apt install python3-pip
```
- Install the required libraries with pip:
```
pip3 install disnake
```

4. Run the bot:
- You can run the bot on Linux using the following command:
```
python3 app.py
```

Make sure you are in the same directory where the `app.py` file is located or provide the full path to it.

## How to Use
1. Deploy: Clone the repository and configure your bot.
2. Run: Launch the bot on your server.
3. Interaction: Users will be able to create tickets, and close them when finished. Admins can delete closed tickets.

## Links
[Boosty developer](https://boosty.to/mao-mao)

[GitHub](https://github.com/rinnyuwu)

[Donation Alerts](https://www.donationalerts.com/r/rinnyuwu)
