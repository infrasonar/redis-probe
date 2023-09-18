from libprobe.probe import Probe
from lib.check.clients import check_clients
from lib.check.commandstats import check_commandstats
from lib.check.keyspace import check_keyspace
from lib.check.redis import check_redis
from lib.check.replication import check_replication
from lib.check.slowlog import check_slowlog
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'clients': check_clients,
        'commandstats': check_commandstats,
        'keyspace': check_keyspace,
        'redis': check_redis,
        'replication': check_replication,
        'slowlog': check_slowlog,
    }

    probe = Probe("redis", version, checks)

    probe.start()
