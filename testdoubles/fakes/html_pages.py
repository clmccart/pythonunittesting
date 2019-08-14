import html as html_converter

class FileAccessWrapper:
    def __init__(self, filename):
        self.filename = filename

    def open(self):
        return open(self.filename, "r", encoding="UTF-8")
        
class HtmlPagesConverter:
    def __init__(self, file_access):
        """Read the file and note the positions of the page breaks so we can access them..."""
        self.breaks = [0]
        self.file_access = file_access
        with self.file_access.open() as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.rstrip()
                if "PAGE_BREAK" in line:
                    page_break_position = f.tell()
                    self.breaks.append(f.tell())
            self.breaks.append(f.tell())

    def get_html_page(self, page):
        """Return html page with the given number (zero indexed)"""
        page_start, page_end = self.get_page_bookends(page)
        
        with self.file_access.open() as f: 
            f.seek(page_start)
            while f.tell() != page_end:
                line = f.readline()
                line = line.rstrip()
                if "PAGE_BREAK" in line:
                    continue
                html = self.convert_to_html(line)

        return html

    def get_page_bookends(self, page):
        page_start = self.breaks[page]
        page_end = self.breaks[page+1]
        
        return (page_start, page_end)

    def convert_to_html(self, line):
        html = ""
        html += html_converter.escape(line, quote=True)
        html += "<br />"
        
        return html
   