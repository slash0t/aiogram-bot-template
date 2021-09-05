from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start dialogue"),
            types.BotCommand("help", "Get references"),
        ]
    )
