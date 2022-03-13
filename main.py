# Standard library imports
import logging
import os

# 3rd party imports
from dotenv import load_dotenv
from telegram.ext import Updater, PicklePersistence

# Local imports
from bot.base import Start, About, Help

# Configure logging
logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
	level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Load secrets
load_dotenv()
TOKEN = os.getenv('TOKEN')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

# Collate features and connect to necessary databases etc.
FEATURES = [
	Start(), 
	About(),
	Help(),
]

# The updater primarily gets telegram updates from telegram servers
updater = Updater(TOKEN, persistence=PicklePersistence('db.pickle'), use_context=True)

# The dispatcher routes updates to the first matching handler
for feature in FEATURES:
	updater.dispatcher.add_handler(feature.handler)

# Store data for /help and /help <feature> in the bot
updater.dispatcher.bot_data['help_text'] = dict()
updater.dispatcher.bot_data['help_full'] = dict()
for feature in FEATURES:
	updater.dispatcher.bot_data['help_text'][feature.command] = feature.help_text
	updater.dispatcher.bot_data['help_full'][feature.command] = feature.help_full

# Register webhook with telegram server and start listening
try:
	updater.bot.set_webhook(f'{HOST}/{TOKEN}')
	updater.start_webhook(listen='0.0.0.0', port=int(PORT), url_path=TOKEN)
	logger.info(f'Deployed with webhook!')

# Fallback to polling
except Exception as e:
	logger.info(f'Failed to deploy webhook: {e}')
	updater.start_polling()
	logger.info(f'Deployed with polling!')

updater.idle()
