# -*- coding: utf-8 -*-
# @Author : feier
# @File : yaml_demo.py

import yaml

data = {  #定义 python 对象
    "client": {"default-character-set": "utf8"},
    "mysql": {"user": 'root', "password": 123},
    "custom": {
        "user1": {"user": "张三", "pwd": 666},
        "user2": {"user": "李四", "pwd": 999},
    }
}

with open('./my.yaml', 'w', encoding='utf-8') as f: # 用 dump 方法把 python 对象转为 yaml 文档

    yaml.dump(data, f, allow_unicode=True)  # 如果写入内容包含中文，allow_unicode=True

with open('./my.yaml', 'r', encoding='utf-8') as f:  # 读取 yaml 文件中的内容，转化为 python 对象
    data = yaml.safe_load(f)
print(data)
print(type(data))

user1_name = data['custom']['user1']['user']  # 取 user1 的姓名
print(user1_name)
