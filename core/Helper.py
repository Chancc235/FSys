# -*- coding:utf-8 -*-
"""
@Created on : 2024/11/3
@Author: mrccc
@Des: 工具函数
"""

import hashlib
import uuid


def random_str():
    """
    唯一随机字符串
    :return: str
    """
    only = hashlib.md5(str(uuid.uuid1()).encode(encoding='UTF-8')).hexdigest()
    return str(only)
