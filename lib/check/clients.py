from collections import Counter
from libprobe.asset import Asset
from libprobe.check import Check
from ..connection import get_conn


class CheckClients(Check):
    key = 'clients'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        conn = await get_conn(asset, local_config, config)

        client_list = await conn.client_list()
        ct = Counter(cl['name'] for cl in client_list)
        clients = [
            {
                'name': name,
                'connections': connections
            }
            for name, connections in ct.items()
        ]

        return {
            'clients': clients,
        }
