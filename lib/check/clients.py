from libprobe.asset import Asset
from libprobe.check import Check
from ..connection import get_conn


class CheckClients(Check):
    key = 'clients'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        conn = await get_conn(asset, local_config, config)

        client_list = await conn.client_list()
        clients = [
            {
                'name': client['id'],
                'addr': client.get('addr'),  # str
                'flags': client.get('flags'),  # str
                'client_name': client.get('name'),  # str
            }
            for client in client_list
        ]

        return {
            'clients': clients,
        }
