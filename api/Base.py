from fastapi import Request, APIRouter

from fastapi import APIRouter, Security
from core.Auth import check_permissions
from api.user import user_info, user_add, user_del, get_user_rules

api_router = APIRouter(prefix="/v1", tags=["api路由"])

api_router.get("/admin/user/info",
              tags=["用户管理"],
              summary="获取用户信息",
              dependencies=[Security(check_permissions, scopes=["user_info"])]
              )(user_info)
api_router.delete("/admin/user/del",
                 tags=["用户管理"],
                 summary="用户删除",
                 dependencies=[Security(check_permissions, scopes=["user_delete"])]
                 )(user_del)
api_router.post("/admin/user/add",
               tags=["用户管理"],
               summary="用户添加",
               # dependencies=[Security(check_permissions, scopes=["user_add"])]
               )(user_add)
api_router.get("/admin/user/rules",
              tags=["用户管理"],
              summary="查询用户权限",
              # dependencies=[Security(check_permissions, scopes=["user_add"])]
              )(get_user_rules)