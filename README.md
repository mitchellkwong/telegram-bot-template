# telegram-bot-template
Boilerplate for a deployment ready telegram bot!

## Setup

1. Grab dependencies with `pip3 install -r requirements.txt`.
2. Add your telegram bot token as an environment variable (`TOKEN`).
3. (Optional) Add server details as environment variables (`HOST`, `PORT`) to enable webhooks.

Note: environment variables can be set through a `.env` file as well!

## Local testing

Use `python3 main.py` to run your bot locally!

## Deployment

The template currently includes a `Procfile` for easy deployment on heroku.
