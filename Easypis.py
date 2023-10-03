from .. import loader, utils


#  __ _                      _
# / _(_)                    | |
# | |_ ___  _____  _   _  ___| | __
# |  _| \ \/ / _ \| | | |/ __| |/ /
# | | | |>  < (_) | |_| | (__|   <
# |_| |_/_/\_\___/ \__,_|\___|_|\_\

# Licensed under the GNU GPLv3
# meta developer: @fix_mods

@loader.tds
class EasyPisMod(loader.Module):
    """Модуль который выводит аргумент 🎭"""

    strings = {'name': 'easypis'}

    async def txtcmd(self, message):
        """Любой текст"""
        args = utils.get_args_raw(message)

        if not args:
            await message.edit("❌ Ошибка: требуется аргумент после команды <code>j</code>")
            return

        await message.delete()
        await message.respond(args)

        @loader.tds
        async def fllcmd(self, message):
            """Отправляет файл в ответ на сообщение"""
            args = utils.get_args_raw(message)
            if message.is_reply:
                reply_message = await message.get_reply_message()
                if reply_message.media:
                    await message.client.send_file(message.to_id, reply_message.media, caption=args)
                else:
                    await message.respond(args)
            else:
                await message.respond(args)
                if not message.is_reply:
                    await message.edit("❌ Ошибка: требуется ответ на сообщение")
