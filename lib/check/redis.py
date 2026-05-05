import asyncio
from libprobe.asset import Asset
from libprobe.check import Check
from ..connection import get_conn


METRICS = {
    'active_defrag_hits',  # int
    'active_defrag_key_hits',  # int
    'active_defrag_key_misses',  # int
    'active_defrag_misses',  # int
    'active_defrag_running',  # int
    # 'allocator_active',  # int
    # 'allocator_allocated',  # int
    # 'allocator_frag_bytes',  # int
    # 'allocator_frag_ratio',  # float
    # 'allocator_resident',  # int
    # 'allocator_rss_bytes',  # int
    # 'allocator_rss_ratio',  # float
    'aof_buffer_length',  # int/optional
    # 'aof_current_rewrite_time_sec',  # int
    'aof_current_size',  # int/optional
    # 'aof_enabled',  # int
    # 'aof_last_bgrewrite_status',  # str
    # 'aof_last_cow_size',  # int
    'aof_last_rewrite_time_sec',  # int
    # 'aof_last_write_status',  # str
    'aof_rewrite_in_progress',  # int
    # 'aof_rewrite_scheduled',  # int
    # 'aof_rewrites',  # int
    # 'aof_rewrites_consecutive_failures',  # int
    # 'arch_bits',  # int
    # 'async_loading',  # int
    # 'atomicvar_api',  # str
    'blocked_clients',  # int
    'client_recent_max_input_buffer',  # int
    'client_recent_max_output_buffer',  # int
    # 'clients_in_timeout_table',  # int
    # 'cluster_connections',  # int
    # 'cluster_enabled',  # int
    # 'config_file',  # str
    # 'configured_hz',  # int
    'connected_clients',  # int
    'connected_slaves',  # int
    # 'current_active_defrag_time',  # int
    # 'current_cow_peak',  # int
    # 'current_cow_size',  # int
    # 'current_cow_size_age',  # int
    # 'current_eviction_exceeded_time',  # int
    # 'current_fork_perc',  # float
    # 'current_save_keys_processed',  # int
    # 'current_save_keys_total',  # int
    # 'dump_payload_sanitizations',  # int
    # 'errorstat_NOAUTH',  # str
    # 'errorstat_WRONGPASS',  # str
    # 'evicted_clients',  # int
    'evicted_keys',  # int
    # 'executable',  # str
    # 'expire_cycle_cpu_milliseconds',  # int
    'expired_keys',  # int
    # 'expired_stale_perc',  # float
    # 'expired_time_cap_reached_count',  # int
    # 'gcc_version',  # str
    # 'hz',  # int
    'instantaneous_input_kbps',  # float
    # 'instantaneous_input_repl_kbps',  # float
    'instantaneous_ops_per_sec',  # int
    'instantaneous_output_kbps',  # float
    # 'instantaneous_output_repl_kbps',  # float
    'io_threaded_reads_processed',  # int
    'io_threaded_writes_processed',  # int
    'io_threads_active',  # int
    'keyspace_hits',  # int
    'keyspace_misses',  # int
    'latest_fork_usec',  # int
    # 'lazyfree_pending_objects',  # int
    # 'lazyfreed_objects',  # int
    # 'loading',  # int
    'loading_total_bytes',  # int/optional
    'loading_loaded_bytes',  # int/optional
    'loading_loaded_perc',  # float/optional
    'loading_eta_seconds',  # int/optional
    # 'lru_clock',  # int
    # 'master_failover_state',  # str
    'master_link_down_since_seconds',  # int/optional
    'master_repl_offset',  # int
    # 'master_replid',  # str
    # 'master_replid2',  # int
    'master_sync_last_io_seconds_ago',  # int/optional
    'master_sync_left_bytes',  # int/optional
    'master_sync_in_progress',  # int/optional
    'maxclients',  # int
    'maxmemory',  # int
    # 'maxmemory_human',  # str
    # 'maxmemory_policy',  # str
    # 'mem_allocator',  # str
    # 'mem_aof_buffer',  # int
    # 'mem_clients_normal',  # int
    # 'mem_clients_slaves',  # int
    # 'mem_cluster_links',  # int
    # 'mem_fragmentation_bytes',  # int
    'mem_fragmentation_ratio',  # float
    # 'mem_not_counted_for_evict',  # int
    # 'mem_replication_backlog',  # int
    # 'mem_total_replication_buffers',  # int
    # 'migrate_cached_sockets',  # int
    # 'module_fork_in_progress',  # int
    # 'module_fork_last_cow_size',  # int
    # 'monotonic_clock',  # str
    # 'multiplexing_api',  # str
    # 'number_of_cached_scripts',  # int
    # 'number_of_functions',  # int
    # 'number_of_libraries',  # int
    # 'os',  # str
    # 'process_id',  # int
    # 'process_supervised',  # str
    'pubsub_channels',  # int
    'pubsub_patterns',  # int
    # 'pubsubshard_channels',  # int
    'rdb_bgsave_in_progress',  # int
    'rdb_changes_since_last_save',  # int
    # 'rdb_current_bgsave_time_sec',  # int
    # 'rdb_last_bgsave_status',  # str
    'rdb_last_bgsave_time_sec',  # int
    # 'rdb_last_cow_size',  # int
    # 'rdb_last_load_keys_expired',  # int
    # 'rdb_last_load_keys_loaded',  # int
    # 'rdb_last_save_time',  # int
    # 'rdb_saves',  # int
    # 'redis_build_id',  # str
    # 'redis_git_dirty',  # int
    # 'redis_git_sha1',  # int
    # 'redis_mode',  # str
    'redis_version',  # str
    'rejected_connections',  # int
    # 'repl_backlog_active',  # int
    # 'repl_backlog_first_byte_offset',  # int
    'repl_backlog_histlen',  # int
    # 'repl_backlog_size',  # int
    # 'reply_buffer_expands',  # int
    # 'reply_buffer_shrinks',  # int
    # 'role',  # str
    # 'rss_overhead_bytes',  # int
    # 'rss_overhead_ratio',  # float
    # 'run_id',  # str
    # 'second_repl_offset',  # int
    # 'server_time_usec',  # int
    # 'slave_expires_tracked_keys',  # int
    'slave_repl_offset',  # int/optional
    # 'sync_full',  # int
    # 'sync_partial_err',  # int
    # 'sync_partial_ok',  # int
    # 'tcp_port',  # int
    # 'total_active_defrag_time',  # int
    'total_commands_processed',  # int
    'total_connections_received',  # int
    # 'total_error_replies',  # int
    # 'total_eviction_exceeded_time',  # int
    # 'total_forks',  # int
    # 'total_net_input_bytes',  # int
    # 'total_net_output_bytes',  # int
    # 'total_net_repl_input_bytes',  # int
    # 'total_net_repl_output_bytes',  # int
    # 'total_reads_processed',  # int
    # 'total_system_memory',  # int
    # 'total_system_memory_human',  # str
    # 'total_writes_processed',  # int
    # 'tracking_clients',  # int
    # 'tracking_total_items',  # int
    # 'tracking_total_keys',  # int
    # 'tracking_total_prefixes',  # int
    # 'unexpected_error_replies',  # int
    # 'uptime_in_days',  # int
    'uptime_in_seconds',  # int
    'used_cpu_sys',  # float
    'used_cpu_sys_children',  # float
    'used_cpu_sys_main_thread',  # float
    'used_cpu_user',  # float
    'used_cpu_user_children',  # float
    'used_cpu_user_main_thread',  # float
    'used_memory',  # int
    # 'used_memory_dataset',  # int
    # 'used_memory_dataset_perc',  # str
    # 'used_memory_functions',  # int
    # 'used_memory_human',  # str
    'used_memory_lua',  # int
    # 'used_memory_lua_human',  # str
    'used_memory_overhead',  # int
    'used_memory_peak',  # int
    # 'used_memory_peak_human',  # str
    # 'used_memory_peak_perc',  # str
    'used_memory_rss',  # int
    # 'used_memory_rss_human',  # str
    # 'used_memory_scripts',  # int
    # 'used_memory_scripts_eval',  # int
    # 'used_memory_scripts_human',  # str
    'used_memory_startup',  # int
    # 'used_memory_vm_eval',  # int
    # 'used_memory_vm_functions',  # int
    # 'used_memory_vm_total',  # int
    # 'used_memory_vm_total_human',  # str
}


class CheckRedis(Check):
    key = 'redis'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        conn = get_conn(asset, local_config, config)

        loop = asyncio.get_running_loop()

        # TODO cache connection, so first ping is not needed
        await conn.ping()  # type: ingore

        start = loop.time()
        await conn.ping()  # type: ingore
        ping_timeit = loop.time() - start

        start = loop.time()
        info = await conn.info()
        info_timeit = loop.time() - start

        item = {
            m: info.get(m) for m in METRICS
        }
        item['name'] = 'redis'
        item['info_timeit'] = info_timeit
        item['ping_timeit'] = ping_timeit

        return {
            'redis': [item],
        }
