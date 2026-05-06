from libprobe.asset import Asset
from libprobe.check import Check
from ..connection import get_conn
from .utils import usec_to_seconds


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
                'sec': usec_to_seconds(stats.pop('usec', None)),
                'sec_per_call':
                    usec_to_seconds(stats.pop('usec_per_call', None)),
            }
            for command, stats in commandstats.items()
        ]

        return {
            'commandstats': commandstats,
        }
