from libprobe.asset import Asset
from . import get_conn


async def check_keyspace(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    conn = get_conn(asset, asset_config, check_config)

    data = await conn.info('keyspace')
    keyspace = [
        {
            'name': name,
            **stats
        }
        for name, stats in data.items()
        if isinstance(stats, dict)
    ]

    return {
        'keyspace': keyspace,
    }
