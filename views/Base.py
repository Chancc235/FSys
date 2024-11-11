# -*- coding:utf-8 -*-
"""
@Created on : 2024/11/3
@Author: mrccc
@Des: 视图路由
"""

from fastapi import APIRouter
from starlette.responses import HTMLResponse
from views.home import home, reg_page, result_page

views_router = APIRouter()


views_router.get("/home", response_class=HTMLResponse)(home)
views_router.get("/reg", response_class=HTMLResponse)(reg_page)
views_router.post("/reg/result", response_class=HTMLResponse)(result_page)

# async def read_item():
#     # return templates.get_template("index.html").render({"request": request, "id": id})
#     # print(request.app.state.views)

