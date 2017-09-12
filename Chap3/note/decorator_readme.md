路径：
1. 从route开始一直往前找，最后在conf.py中找到
old_update_wrapper和update_wrapper 2个函数。从代码上看，old_update_wrapper和update_wrapper 2个函数与我们最终的目的无关。
old_update_wrapper = functools.update_wrapper
    def update_wrapper(wrapper, wrapped, *a, **kw):
        rv = old_update_wrapper(wrapper, wrapped, *a, **kw)
        rv._original_function = wrapped
        return rv
    functools.update_wrapper = update_wrapper


route -> add_url_rule -> setupmethod  -> update_wrapper  -> functools.update_wrapper -> unwrap_decorators
在zeal 10.2. functools — Higher-order functions and operations on callable objects 
```
functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
Update a wrapper function to look like the wrapped function. 
The optional arguments are tuples to specify which attributes of the original function are assigned directly to the matching attributes 
on the wrapper function and which attributes of the wrapper function are updated with the corresponding attributes 
from the original function.                                                                           
```                 

2. route -> add_url_rule -> url-route-registrations
在doc/api.rst中对url-route-registrations描述如下，和我们最终的目的也不相关
URL Route Registrations
-----------------------
Generally there are three ways to define rules for the routing system:

1.  You can use the :meth:`flask.Flask.route` decorator.
2.  You can use the :meth:`flask.Flask.add_url_rule` function.
3.  You can directly access the underlying Werkzeug routing system
    which is exposed as :attr:`flask.Flask.url_map`.

Variable parts in the route can be specified with angular brackets
(``/user/<username>``).  By default a variable part in the URL accepts any
string without a slash however a different converter can be specified as
well by using ``<converter:name>``.

Variable parts are passed to the view function as keyword arguments.
-----------------------
3. 最终目标锁定在add_url_rule
add_url_rule参数如下
def add_url_rule(self, rule, endpoint=None, view_func=None, provide_automatic_options=None, **options):

:param rule: the URL rule as string
:param endpoint: the endpoint for the registered URL rule.  Flask
itself assumes the name of the view function as endpoint
:param view_func: the function to call when serving a request to the provided endpoint
:param provide_automatic_options: controls whether the ``OPTIONS``
            method should be added automatically. This can also be controlled
            by setting the ``view_func.provide_automatic_options = False``
            before adding the rule.

在add_url_rule中有一段解释
Basically this example::
    @app.route('/')
    def index():
        pass

Is equivalent to the following::
    def index():
        pass
    app.add_url_rule('/', 'index', index)           

这段代码就能够解释，route运行原理
@app.route('/')
def hello_world():
    return 'Hello World!'
