from libprobe.asset import Asset
from libprobe.check import Check
from ..connection import get_conn


class CheckCommandstats(Check):
    key = 'commandstats'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        conn = get_conn(asset, local_config, config)

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
