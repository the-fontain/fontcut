import tornado.web
import tornado.gen as gen
import json

from forge import compress


class MainHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def post(self):
        data = json.loads(self.request.body)
        if data.get('font_url') and data.get('text'):
            b64font = yield compress(self.application, **data)
            self.write(b64font)
        else:
            self.set_status(404)
