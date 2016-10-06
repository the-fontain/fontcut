#!/usr/bin/python2
import fontforge
import base64
import tornado.gen as gen
import cStringIO

from collections import deque
from tornado.web import HTTPError
from tempfile import NamedTemporaryFile

@gen.coroutine
def get_font(application, font_url):
    font_response = yield application.client.fetch(font_url)
    raise gen.Return(font_response)


@gen.coroutine
def compress(application, text, font_url):

    try:
        font_response = yield get_font(application, font_url)
    except HTTPError as e:
        raise e

    with NamedTemporaryFile() as input_font:
        input_font.write(font_response.body)
        input_font.flush()
        font = fontforge.open(input_font.name)

    for i in set([i.lower() for i in deque(text.decode("UTF-8"))]):
        font.selection[ord(i)] = True

    font.selection.invert()

    for i in font.selection.byGlyphs:

        font.removeGlyph(i)

    with NamedTemporaryFile() as output_font:
        font.generate(output_font.name)
        output_font.flush()
        with open(output_font.name, 'r') as font:
            b64_font = base64.b64encode(font.read())

    raise gen.Return(b64_font)
