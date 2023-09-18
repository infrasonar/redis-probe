import os
from libprobe.asset import Asset
from redis import asyncio as aioredis


REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))


def get_conn(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> aioredis.Redis:

    # username and password can both be empty
    username = asset_config.get('username')
    password = asset_config.get('password')

    address = check_config['address']
    port = check_config.get('port', REDIS_PORT)
    redis_url = f'redis://{address}'
    return aioredis.from_url(
        redis_url,
        port=port,
        username=username,
        password=password
    )
