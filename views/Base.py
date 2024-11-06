# -*- coding:utf-8 -*-
"""
@Created on : 2024/11/3
@Author: mrccc
@Des: 视图路由
"""

from fastapi import APIRouter
from starlette.responses import HTMLResponse
from views.home import home

views_router = APIRouter()


views_router.get("/items/{id}", response_class=HTMLResponse)(home)


# async def read_item():
#     # return templates.get_template("index.html").render({"request": request, "id": id})
#     # print(request.app.state.views)

