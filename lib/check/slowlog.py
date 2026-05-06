from libprobe.asset import Asset
from libprobe.check import Check
from ..connection import get_conn
from .utils import usec_to_seconds_as_int


class CheckSlowlog(Check):
    key = 'slowlog'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        conn = await get_conn(asset, local_config, config)

        def parse_slowlog_get(response, **_):
            return [{
                'name': str(item[0]),
                'start_time': item[1],  # int
                'duration': usec_to_seconds_as_int(item[2]),
                # Redis Enterprise injects another entry at index [3], which
                # has the complexity info (i.e. the value N in case the command
                # has an O(N) complexity) instead of the command.
                'complexity': item[3] if isinstance(item[3], int) else None,
                'command': [a.decode() for a in item[-3]],
                'client_addr': item[-2].decode(),
                'client_name': item[-1].decode(),
            } for item in response]

        conf = await conn.config_get('slowlog-max-len')
        slowlog_max_len = int(conf['slowlog-max-len'])
        conn.set_response_callback(
            'SLOWLOG GET', parse_slowlog_get)  # type: ignore
        slowlog = await conn.slowlog_get(slowlog_max_len)

        return {
            'slowlog': slowlog,
        }
