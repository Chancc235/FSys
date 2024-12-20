# -*- coding:utf-8 -*-
"""
@Created on : 2024/10/31
@Author: mrccc
@Des: fastapi事件监听
"""
from typing import Callable
from fastapi import FastAPI
from database.mysql import register_mysql
from database.redis import sys_cache
from aioredis import Redis

def startup(app: FastAPI) -> Callable:
    """
    FastApi 启动完成事件
    :param app: FastAPI
    :return: start_app
    """
    async def app_start() -> None:
        # APP启动完成后触发
        print("fastapi已启动")
        await register_mysql(app)
        app.state.cache = await sys_cache()
        pass
    return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastApi 停止事件
    :param app: FastAPI
    :return: stop_app
    """
    async def stop_app() -> None:
        # APP停止时触发
        print("fastapi已停止")
        cache: Redis = await app.state.cache
        await cache.close()
    return stop_app
