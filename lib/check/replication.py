from libprobe.asset import Asset
from libprobe.check import Check
from ..connection import get_conn


class CheckReplication(Check):
    key = 'replication'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        conn = get_conn(asset, local_config, config)

        data = await conn.info('replication')
        replication = [
            {
                'name': name,
                **stats
            }
            for name, stats in data.items()
            if isinstance(stats, dict)
        ]

        return {
            'replication': replication,
        }
