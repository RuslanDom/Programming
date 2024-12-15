from telebot.types import BotCommand


def set_commands(bot):
    bot.set_my_commands([BotCommand(command='start',
                                    description='Запуск бота'),
                         BotCommand(command='help',
                                    description='Основные команды'),
                         BotCommand(command='sign_in',
                                    description='Войти в систему')
                         ])


