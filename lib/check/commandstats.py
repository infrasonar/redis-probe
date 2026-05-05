from libprobe.asset import Asset
from libprobe.check import Check
from ..connection import get_conn


class CheckCommandstats(Check):
    key = 'commandstats'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        conn = await get_conn(asset, local_config, config)

        commandstats = await conn.info('commandstats')
        commandstats = [
            {
                'name': command,
                'calls': stats.get('calls'),  # int
                'failed_calls': stats.get('failed_calls'),  # int
                'rejected_calls': stats.get('rejected_calls'),  # int
                'usec': stats.get('usec'),  # int
                'usec_per_call': stats.get('usec_per_call'),  # float
            }
            for command, stats in commandstats.items()
        ]

        return {
            'commandstats': commandstats,
        }
