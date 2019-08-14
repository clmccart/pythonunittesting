import unittest

class HtmlPagesTest(unittest.TestCase):
    def test_inserts_br_tags_for_linebreaks(self):
        filename = os.path.join(tempfile.gettempdir(), "afile.txt")
        f = open(filename, "w", encoding="UTF-8")
        f.write("plain test\n")
        f.close()
        converter = HtmlPagesConverter(filename)
        new_test = converter.get_html_page(0)
        self.assertEqual("plain text<br />", new_test)