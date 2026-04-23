from libprobe.probe import Probe
from lib.check.clients import CheckClients
from lib.check.commandstats import CheckCommandstats
from lib.check.keyspace import CheckKeyspace
from lib.check.redis import CheckRedis
from lib.check.replication import CheckReplication
from lib.check.slowlog import CheckSlowlog
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckClients,
        CheckCommandstats,
        CheckKeyspace,
        CheckRedis,
        CheckReplication,
        CheckSlowlog,
    )

    probe = Probe("redis", version, checks)

    probe.start()
