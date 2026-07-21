# Movie Request Bot 🎬

A simple Telegram bot that lets users request movies by messaging it directly. Every request is automatically posted to your Telegram channel.

## How it works

1. A user sends `/start` to the bot and gets a welcome message.
2. The user types the name of a movie they want.
3. The bot posts the request to your channel, formatted with the movie title and who requested it.
4. The user gets a confirmation reply.

## Requirements

- Python 3.9+
- A Telegram bot token (from [@BotFather](https://t.me/BotFather))
- A Telegram channel with the bot added as an **admin** (with "Post Messages" permission)

## Setup

1. **Clone this repo** and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Create your bot**:
   - Message [@BotFather](https://t.me/BotFather) → `/newbot` → follow the prompts → copy the token.

3. **Add the bot to your channel**:
   - Go to your channel's settings → Administrators → Add Admin → search for your bot → grant "Post Messages" permission.

4. **Get your channel ID**:
   - If your channel has a public username, just use `@yourchannelname`.
   - If it's private, forward any message from the channel to [@userinfobot](https://t.me/userinfobot) to get the numeric ID (e.g. `-1001234567890`).

5. **Set environment variables**:
   ```bash
   export BOT_TOKEN="your-bot-token-here"
   export CHANNEL_ID="@yourchannelname"
   ```
   (On Windows: use `set` instead of `export`, or add them in your hosting platform's dashboard.)

6. **Run the bot**:
   ```bash
   python bot.py
   ```

## Deployment

This bot uses long polling, so it needs to run continuously. Free hosting options include PythonAnywhere, Fly.io, and Oracle Cloud's Always Free tier. See the project chat/notes for a comparison.

## Files

| File | Purpose |
|---|---|
| `bot.py` | Main bot logic |
| `requirements.txt` | Python dependencies |

## Roadmap / possible additions

- [ ] Duplicate request detection
- [ ] Admin approval step before posting to the channel
- [ ] Rate limiting per user
- [ ] Persistent storage (database) for request history

## License

Add your preferred license here (e.g. MIT).
