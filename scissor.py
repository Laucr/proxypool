from lxml import etree


class XpathPicker:
    def __init__(self, html_file, xpath):
        self.html = html_file
        self.xpath = xpath

    def parse(self):
        tree = etree.HTML(self.html)
        nodes = [tree.xpath(self.xpath[iter_i]) for iter_i in range(len(self.xpath))]
        return nodes


class CssSelector:
    def __init__(self, html_file, sel):
        self.html = html_file
        self.sel = sel

    def parse(self):
        tree = etree.HTML(self.html)
        nodes = [tree.cssselect(self.sel[iter_i]) for iter_i in range(len(self.sel))]
        return nodes
