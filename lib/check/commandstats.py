from libprobe.asset import Asset
from . import get_conn


async def check_commandstats(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    conn = get_conn(asset, asset_config, check_config)

    commandstats = await conn.info('commandstats')
    commandstats = [
        {
            'name': command,
            **stats
        }
        for command, stats in commandstats.items()
    ]

    return {
        'commandstats': commandstats,
    }
