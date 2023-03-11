![](https://github.com/LemurDev/CozyBot/blob/main/CozyBot.png) 

# What is CozyBot?

CozyBot is a Twitch bot based on **COZINESS**!! This bot is mainly being developed by Lemur and Billy. But, we are more than happy to see the community join in!

# Setup

Install requirements via requirements.txt
```bash
pip install -r requirements.txt
```

Create a `.env` file. In this file, you need two variables:
- TWITCH_ACCESS_TOKEN
- TWITCH_CHANNEL_NAME

Token can be generated from [Token Generator](https://twitchtokengenerator.com/) **BUT ONLY FOR TESTING PURPOSES**

If you would like to use this bot in production then click [here](https://dev.twitch.tv/docs/authentication/) which will give you a tutorial on how to do so.

Next, assign a channel name you want the bot to start in

# Running the Bot

## Windows

**Currently being worked on.**

## Linux

```bash
./run_liunx
```
This will run the Twitch bot for you. Make sure you follow the setup instructions!

# Display on Stream

CozyBot will output to a file named `cozy.txt`. The value will only change **IF** the coziness is higher than before. You could then read from this text file to display the highest coziness. Once someone reaches 100% coziness, it will reset once another person has run the command.

It will also output to a file named `100_cozy.txt`. This will display the username who got 100% cozy. The file will then clear its contents so it "disappears".

All these files can then be viewed as text file on OBS, for example.
