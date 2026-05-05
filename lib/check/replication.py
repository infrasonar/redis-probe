from libprobe.asset import Asset
from libprobe.check import Check
from ..connection import get_conn


class CheckReplication(Check):
    key = 'replication'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        conn = await get_conn(asset, local_config, config)

        data = await conn.info('replication')
        replication = [
            {
                'name': name,
                'role': stats.get('role'),
                'master_failover_state': stats.get('master_failover_state'),
                'master_replid': stats.get('master_replid'),
                'master_replid2': stats.get('master_replid2'),
                'master_repl_offset': stats.get('master_repl_offset'),
                'second_repl_offset': stats.get('second_repl_offset'),
                'repl_backlog_active': stats.get('repl_backlog_active'),
                'repl_backlog_size': stats.get('repl_backlog_size'),
                'repl_backlog_first_byte_offset':
                    stats.get('repl_backlog_first_byte_offset'),
                'repl_backlog_histlen': stats.get('repl_backlog_histlen'),

                # only for replica
                'master_host': stats.get('master_host'),
                'master_port': stats.get('master_port'),
                'master_link_status': stats.get('master_link_status'),
                'master_last_io_seconds_ago':
                    stats.get('master_last_io_seconds_ago'),
                'master_sync_in_progress':
                    stats.get('master_sync_in_progress'),
                'slave_read_repl_offset': stats.get('slave_read_repl_offset'),
                'slave_repl_offset': stats.get('slave_repl_offset'),
                'slave_priority': stats.get('slave_priority'),
                'slave_read_only': stats.get('slave_read_only'),
                'replica_announced': stats.get('replica_announced'),
            }
            for name, stats in data.items()
            if isinstance(stats, dict)
        ]

        return {
            'replication': replication,
        }
