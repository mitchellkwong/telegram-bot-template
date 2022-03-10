from telegram import Update, ParseMode
from telegram.ext import CallbackContext

from bot.utils import Command


class Start(Command):
    command = 'start'
    help_text = 'Reset me!'
    help_full = '/start restarts your session with me.'
    
    def callback(self, update: Update, context: CallbackContext):
        name = update.message.from_user.first_name
        text = '\n'.join([
            f'Hello {name}!',
        ])
        update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)

    
class About(Command):
    command = 'about'
    help_text = 'Learn more about me!'
    help_full = '/about to contact my creator (:'

    def callback(self, update: Update, context: CallbackContext):
        text = '\n'.join([
            'Hi! I make telebots fairly frequently and this bot is a holding ground for some boilerplate I like to use (:',
            'Github: https://github.com/mitchellkwong/telegram-bot-template',
        ])
        update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)


class Help(Command):
    command = 'help'
    help_text = 'Let me help you!'
    help_full = 'Use /help <feature name> for more information!'

    def callback(self, update: Update, context: CallbackContext):
        # Default help text 
        help_dict = context.bot_data['help_text']
        help_text = [f'/{function}: {help}' for function, help in help_dict.items()]
        text = '\n'.join([
			*help_text,
            '',
            'Use /help <feature name> for more information!',
        ])

        # Return full user guide if user wants help for a specific function
        if len(context.args) > 0:
            func_name = context.args[0]
            help_dict = context.bot_data['help_full']
            
            # Overwrite reply text with specific help text
            if func_name in help_dict:
                text = help_dict[func_name]
            
            # Add an error message before the default help text
            else:
                text = '\n'.join([
                    f'{func_name} is not a feature!',
                    '',
                    text,
                ])
        
        update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)