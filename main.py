import atexit
import grpc
import logging
import os
import typing
from typing import Dict
from typing import List

import server_pb2
import server_pb2_grpc


name: str = 'Friendship'

port: str = None
pg_port: str = None
pg_host: str = None
pg_user: str = None
pg_pass: str = None


sessfile: str = os.path.abspath('./.duo.sess')


def init_env() -> None:
    global port
    port = os.environ['PORT']
    logging.info('Found PORT = %s', port)

    global pg_port
    pg_port = os.environ['PG_PORT']
    logging.info('Found PG_PORT = %s', pg_port)

    global pg_hostname
    pg_hostname = os.environ['PG_HOST']
    logging.info('Found PG_HOST = %s', pg_host)

    global pg_user
    pg_user = os.environ['PG_USER']
    logging.info('Found PG_USER = %s', pg_user)


def init_atexit() -> None:
    def end():
        logging.info('bye')

    atexit.register(end)


def init_logging() -> None:
    logging.basicConfig(
        format=f'{name} %(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    logging.info('hi')


def init() -> None:
    init_logging()
    init_atexit()
    init_env()


def main() -> None:
    init()


if __name__ == '__main__':
    main()
