#!/usr/bin/env python
#
# Copyright 2009 Facebookw
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

# 定义 http 服务基本信息
define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    """
    1. Handler 类似于 JAVA 中的 Controller
    2. tornado.web.RequestHandler 是处理 http 请求的基类
    """

    def get(self):
        """定义了一个 get 请求服务，并返回 "Hello，world" 字符串

        :return:
        """
        self.write("Hello, world")


def main():
    """main() 函数，一般为启动的入口

    :return:
    """
    # 解析命令行参数
    tornado.options.parse_command_line()
    # 定义请求路径和 Handler 之间的映射关系
    application = tornado.web.Application(
        [
            (r"/", MainHandler)
        ]
    )
    # 定义一个 HTTPSERVER
    http_server = tornado.httpserver.HTTPServer(application)
    # HTTPSERVER 监听端口
    http_server.listen(options.port)
    # 启动 HTTPSERVER 服务
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
