import os
from libprobe.asset import Asset
from redis import asyncio as aioredis


REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))


def get_conn(
        asset: Asset,
        local_config: dict,
        config: dict) -> aioredis.Redis:

    # username and password can both be empty
    username = local_config.get('username')
    password = local_config.get('password')

    address = config.get('address')
    if not address:
        address = asset.name
    port = config.get('port', REDIS_PORT)
    redis_url = f'redis://{address}'
    return aioredis.from_url(
        redis_url,
        port=port,
        username=username,
        password=password
    )
