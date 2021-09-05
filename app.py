import os

import django
from aiogram import executor

from loader import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def setup_django():
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'django_site.django_site.settings'
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': 'true'})
    django.setup()


async def on_startup(dispatcher):
    await setup_django()

    import middlewares, filters, handlers

    await set_default_commands(dispatcher)

    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
