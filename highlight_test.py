(((())))
{([([])])}
a: list = [ # 代码注释
    (1, 2), 3, # 括号内代码注释
    # 括号内注释
    ]
for i, j in enumerate(a):
    print(f"a的第{i}项是{j}")
path = r"C:\Users\Administrator\Desktop\test.py"
with open(path, 'w') as f:
    f.write(a)
# URL: https://github.com/z7572
# 字符串前缀
s =  "\u0000 \n \0 \7 \9 \77 \777 \778 \997 \() * {a}"
u = u"\u0000" # 与不加前缀相同
b = b"\u0000" # 无Unicode字符串转义,其余同上
f = f"\u0000 \n \0 \7 \9 \77 \777 \778 \997 \() * {a}"
r = r"\u0000 \n \0 \7 \9 \78 \777 \778 \997 \() * {a}"
fr=fr"\u0000 \n \0 \7 \9 \77 \777 \778 \997 \() * {a}"

class Test(xx.xx):
    def __init__(self):
        try:
            exec(str(a))
        except Exception as e:
            return e
    def BAR(a,b):
        def wrapper(func):
            func()
            return None
        return wrapper
    @BAR(a=1,b=1) # 装饰器
    def foo():
        pass
    def bar: # 错误：未加括号
        ())) # 错误：括号不匹配
        (    # 只支持后括号,前括号会把后文全部变色

import asyncio
async def main(): # async在def前变色
    while True:
        try:
            async with AsyncClient() as client:
                ...
        except:
            ...
        await ...
asyncio.run(main())
