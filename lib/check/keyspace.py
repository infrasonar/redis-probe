from libprobe.asset import Asset
from libprobe.check import Check
from ..connection import get_conn


class CheckKeyspace(Check):
    key = 'keyspace'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        conn = await get_conn(asset, local_config, config)

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
