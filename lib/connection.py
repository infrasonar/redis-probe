import os
from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from redis.asyncio import Redis, from_url
from redis.exceptions import AuthenticationError
from redis.exceptions import ConnectionError
from .connection_cache import ConnectionCache


REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))


async def get_conn(
        asset: Asset,
        local_config: dict,
        config: dict) -> Redis:

    # username and password can both be empty
    username = local_config.get('username')
    password = local_config.get('password')

    address = config.get('address')
    if not address:
        address = asset.name
    port = config.get('port', REDIS_PORT)
    redis_url = f'redis://{address}'

    key = (address, port, username, password)
    prev = ConnectionCache.get_value(key)
    if prev:
        return prev

    try:
        conn = from_url(
            redis_url,
            port=port,
        )
        await conn.initialize()
        if password:
            await conn.auth(password=password, username=username or None)
    except AuthenticationError:
        raise CheckException('Failed to authenticate')
    except ConnectionError:
        raise CheckException('Failed to connect')
    except Exception as e:
        msg = str(e) or type(e).__name__
        raise CheckException(msg)
    else:
        # when connection is older than 3600 we request new 'connection'
        max_age = 3600
        ConnectionCache.set_value(
            key,
            conn,
            max_age)
    return conn
