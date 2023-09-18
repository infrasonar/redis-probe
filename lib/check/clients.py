from collections import Counter
from libprobe.asset import Asset
from . import get_conn


async def check_clients(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    conn = get_conn(asset, asset_config, check_config)

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
