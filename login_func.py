def login_check(username=None,password=None):
     if username!=None and password!=None:
         if username=="python35" and password=="lemonban":
             return {"code" : 0, "msg" : "登录成功"}
         else:
             return {"code" : 1, "msg" : "账号或密码不正确"}

     else:
         return {"code": 1, "msg": "所有参数都不能为空"}



if __name__ == '__main__':
    #1、账号密码正确
    res = login_check("python35","lemonban")
    expected = {"code" : 0, "msg" : "登录成功"}
    assert res == expected
    print("测试用例执行通过---1")
    #2、密码不正确
    res = login_check("python35", "lemonban1")
    expected = {"code" : 1, "msg" : "账号或密码不正确1"}
    assert res == expected
    print("测试用例执行通过---2")
