# -*- coding:utf-8 -*-
"""
@Created on : 2024/11/3
@Author: mrccc
@Des: 路由集合
"""
from fastapi import APIRouter
from api.Base import api_router
from views.Base import views_router
from api.Login import index, login


All_ROUTER = APIRouter()

All_ROUTER.include_router(api_router)

All_ROUTER.include_router(views_router)

All_ROUTER.get("/index", tags=["api路由"], summary="注册")(index)
All_ROUTER.post("/login", tags=["api路由"], summary="登录")(login)