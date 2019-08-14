import unittest
import os 
import tempfile
from testdoubles.fakes.html_pages import HtmlPagesConverter, FileAccessWrapper 

import io

class HtmlPagesTest(unittest.TestCase):
    def test_inserts_br_tags_for_linebreaks(self):
        converter = HtmlPagesConverter(FakeFileWrapper("plain text\n"))
        new_test = converter.get_html_page(0)
        self.assertEqual("plain text<br />", new_test)

    def test_quotes_escaped(self):
        converter = HtmlPagesConverter(FakeFileWrapper("text with 'quotes'"))
        new_text = converter.get_html_page(0)
        self.assertEqual("text with &#x27;quotes&#x27;<br />", new_text)

    def test_random_access_pages(self):
        converter = HtmlPagesConverter(FakeFileWrapper("page one\nPAGE_BREAK\npage two\nPAGE_BREAK\n"))
        page_two = converter.get_html_page(1)
        self.assertEqual("page two<br />", page_two)
    
    def test_html_conversion(self):
        converter = HtmlPagesConverter(FakeFileWrapper("page one\nPAGE_BREAK\npage two\nPAGE_BREAK\n")) 
        line = "page two"
        html = converter.convert_to_html(line)
        self.assertEqual("page two<br />", html)

class FakeFileWrapper:
    def __init__(self, text):
        self.text = text
    
    def open(self):
        return io.StringIO(self.text)