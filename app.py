# app.py 通常是整个应用的入口点，负责启动应用。
# 在 app.py 中，你可能会有类似于 app.run() 的代码来启动开发服务器。

from app import app

# 在开发过程中，你可以在应用实例上调用 app.run() 来启动 Flask 开发服务器。这会让你的应用监听特定的主机和端口，以便接受来自客户端的请求。
if __name__ == '__main__':
   app.run()