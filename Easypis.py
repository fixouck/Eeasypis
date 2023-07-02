from .. import loader, utils
 #  __ _                      _    
#  / _(_)                    | |   
# | |_ ___  _____  _   _  ___| | __
# |  _| \ \/ / _ \| | | |/ __| |/ /
# | | | |>  < (_) | |_| | (__|   < 
# |_| |_/_/\_\___/ \__,_|\___|_|\_\
                                  
# Licensed under the GNU GPLv3
#meta developer: @fixouck_qq

class EasyPisMod(loader.Module):
    """залупа"""
    strings = {'name': 'easypis'}

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def jcmd(self, message):
        """Любой текст"""
        args = utils.get_args_raw(message)

        if not args:
            await message.edit("Ошибка: требуется текст после команды 'j'.")
            return

        await message.delete()
        await message.respond(args)
