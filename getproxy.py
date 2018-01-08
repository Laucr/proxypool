import requests
import scissor


class ProxyGetter:
    def __init__(self, _proxy_host, _xpath, _sel):
        self.proxy_host = _proxy_host
        self.__xpath__ = _xpath
        self.__sel__ = _sel
        self._e_ = None

    @staticmethod
    def _proxy_compose_(_proxy_nodes):
        # Calculate delay to the proxy
        _proxy_nodes[-1] = list(map(lambda x: int(float(x[:-1]) * 1000), _proxy_nodes[-1]))

        _proxy_amt = len(_proxy_nodes[0])
        _proxies = []
        for iter_i in range(_proxy_amt):
            _proxy = []
            for iter_j in _proxy_nodes:
                _proxy.append(iter_j[iter_i])
            _proxies.append(_proxy)
        return _proxies

    def get_proxy(self):
        try:
            resp = str(requests.request('GET', self.proxy_host).content,
                       encoding='utf-8')
            # xp = scissor.XpathPicker(resp, self.__xpath__)
            # return self._proxy_compose_(xp.parse())
            css = scissor.CssSelector(resp, self.__sel__)
            return css
        except Exception as e:
            self._e_ = e
            return None

    def get_exception(self):
        return self._e_
