1. 简单路由
@app.route('/')
def hello_user():
    return 'hello world'

2. 参数路由
@app.route('/users/<id>')
def users_id(id):
  return 'hello user:' + id

@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return 'query_user' + id

3. @app.route('....')出发的函数，在HTML上会显示return的内容



#### 那些坑
1. @app.route 触发函数之后，函数返回值会显示在html上
2. <form>表单中的action属性对应相对地址
<form action="/user_input">对应http://127.0.0.1:5000/user_input地址
3. 使用request.args.get('key')可以获得URL中关键字key对应的信息