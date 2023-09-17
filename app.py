# app.py 通常是整个应用的入口点，负责启动应用。
# 在 app.py 中，你可能会有类似于 app.run() 的代码来启动开发服务器。

# from app import app

# # 在开发过程中，你可以在应用实例上调用 app.run() 来启动 Flask 开发服务器。这会让你的应用监听特定的主机和端口，以便接受来自客户端的请求。
# if __name__ == '__main__':
#    app.run()


from flask import Flask
import os

# 创建一个 flask 应用的实例
app = Flask(__name__)
port = int(os.environ.get('PORT', 33507))








# if app.config["ENV"] == "production":
if os.environ.get("FLASK_ENV") == "production":
    app.config.from_object("config.DevelopmentConfig")
elif os.environ.get("FLASK_ENV") == "testing":
    print('*********** testing environment ***********')
    app.config.from_object("config.TestingConfig")
else:
    print('*********** Production environment ***********')
    app.config.from_object("config.ProductionConfig")

# from app import views

# 这行代码 from app import views 在 Flask 应用中有着重要的作用。让我解释一下它的作用：

# 导入 Flask 应用对象：通常，一个 Flask 应用是由多个模块组成的，其中包括应用的主要逻辑、路由、视图函数等。在 Flask 中，每个模块都可以包含应用的一部分功能。在这里，from app import views 是在应用的入口文件（通常是 app.py 或 run.py）中导入了一个名为 app 的 Flask 应用对象。

# 导入视图函数：views 是一个 Python 模块，它包含了一组视图函数。视图函数是处理 HTTP 请求并生成 HTTP 响应的函数，它们定义了不同路由上的行为。通过导入 views 模块，你可以访问这些视图函数，以便在应用中定义路由和处理请求。

# 将视图函数与路由关联：通常，views 模块中的视图函数会使用 Flask 的装饰器（如 @app.route()）来关联特定的路由。这些装饰器告诉 Flask 在哪个 URL 上调用哪个视图函数。例如

# @app.route('/home')
# def home():
#     return 'Welcome to the home page!'

# 这个代码片段将 /home 路径映射到了 home 视图函数上。


if __name__ == '__main__':
   app.run(debug=False, host='0.0.0.0', port=port)

