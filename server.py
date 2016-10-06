import tornado.ioloop
import tornado.web
import tornado.httpclient

from tornado.httpserver import HTTPServer
from os import environ
from handler import MainHandler


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    tornado.httpclient.AsyncHTTPClient.configure(
        'tornado.curl_httpclient.CurlAsyncHTTPClient',
    )
    app.client = tornado.httpclient.AsyncHTTPClient()
    server = HTTPServer(app)
    server.bind(int(environ.get('port', 8888)), environ.get('ip', '0.0.0.0'))
    server.start()
    tornado.ioloop.IOLoop.current().start()
