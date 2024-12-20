# -*- coding:utf-8 -*-
"""
@Time : 2024/11/11
@Author: mrccc
@Des: 用户验证模型
"""
from pydantic import Field, BaseModel


class CreateUser(BaseModel):
    username: str = Field(min_length=3, max_length=10)
    password: str = Field(min_length=8, max_length=12)
    user_type: bool = Field(default=False)
