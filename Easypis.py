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

    async def jcmd(self, message):
        """Любой текст"""
        args = utils.get_args_raw(message)

        if not args:
            await message.edit("❌ Ошибка: требуется аргумент после команды <code>j</code>")
            return

        await message.delete()
        await message.respond(args)

