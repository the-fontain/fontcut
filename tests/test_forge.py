import tornado
import server
import base64

from tornado.concurrent import Future
from tornado.testing import AsyncHTTPTestCase
from mock import patch
from fontcut.forge import compress
from tornado.httpclient import HTTPResponse, HTTPRequest
from cStringIO import StringIO

class ForgeTestCase(AsyncHTTPTestCase):

    def setUp(self):
        super(ForgeTestCase, self).setUp()
        self.app = self.get_app()
        self.app.client = tornado.httpclient.AsyncHTTPClient()

    def get_app(self):
        return server.make_app()

    @tornado.testing.gen_test
    def test_forge_compress(self):
        font_url = "http://google.com/font.woff"
        future = Future()
        with patch.object(self.app.client, 'fetch') as fetch_mock:
            with open('tests/data/font.woff') as font_body:
                request = HTTPRequest(font_url)
                response = HTTPResponse(
                    request,
                    200,
                    buffer=StringIO(font_body.read())
                )
                future.set_result(response)
                fetch_mock.side_effect = lambda x: future
            b64 = yield compress(self.app, "A", font_url)
            with open('tests/data/base64') as b64_file:
                self.assertAlmostEqual(172, int(len(b64)/10.0))
                try:
                    base64.b64decode(b64_file.read())
                except TypeError:
                    self.fail('base64 wrong format')
