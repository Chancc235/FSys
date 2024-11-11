# -*- coding:utf-8 -*-
"""
@Time : 2024/11/6
@Author: mrccc
@Des: mysql数据库
"""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import os


# -----------------------数据库配置-----------------------------------
DB_ORM_CONFIG = {
    "connections": {
        "base": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': os.getenv('BASE_HOST', '127.0.0.1'),
                'user': os.getenv('BASE_USER', 'root'),
                'password': os.getenv('BASE_PASSWORD', 'Cc123456'),
                'port': int(os.getenv('BASE_PORT', 3306)),
                'database': os.getenv('BASE_DB', 'base'),
            }
        },

    },
    "apps": {
        "base": {"models": ["models.base"], "default_connection": "base"},
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}


async def register_mysql(app: FastAPI):
    # 注册数据库
    register_tortoise(
        app,
        config=DB_ORM_CONFIG,
        generate_schemas=False,
        add_exception_handlers=True,
    )
