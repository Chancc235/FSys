from fastapi import Request, Form, Cookie
from models.base import User
from typing import Optional

async def home(request: Request, session_id: Optional[str] = Cookie(None)):
    cookie = session_id
    session = request.session.get("session")
    page_data = {
        "cookie": cookie,
        "session": session
    }
    # request.session.setdefault("55555", "hdaldais")
    return request.app.state.views.TemplateResponse("index.html", {"request": request, **page_data})


async def reg_page(request: Request):
    """
    注册页面
    :param request:
    :return: html
    """
    return request.app.state.views.TemplateResponse("reg_page.html", {"request": request})

async def result_page(request: Request, username:str = Form(...), password:str = Form(...)):
    """
    注册结果
    :param request:
    :return: html
    """
    add_user = await User().create(username=username, password=password)
    user_list = await User().all().values()
    for u in user_list:
        print(f"{u.get('username')}: {u.get('id')}")

    # 获取当前创建的用户
    get_user = await User().get_or_none(username=username)
    if not get_user:
        print("")
        return {"info": "没有查询到用户"}

    return request.app.state.views.TemplateResponse(
        "reg_result.html", {"request": request, "username": username, "password": password})

