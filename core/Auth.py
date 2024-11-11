# -*- coding:utf-8 -*-
"""
@Time : 2024/11/11
@Author: mrccc
@Des: JWT鉴权
"""
from fastapi import Request
from fastapi.security import SecurityScopes


async def check_permissions(req: Request, security_scopes: SecurityScopes):
    """
    权限验证
    :param req:
    :param security_scopes:
    :return:
    """
    pass
