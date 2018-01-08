import getproxy

host = 'https://www.kuaidaili.com/free/inha/'
xpath = ['//*[@id="list"]/table/tbody/tr/td[1]/text()',
         '//*[@id="list"]/table/tbody/tr/td[2]/text()',
         '//*[@id="list"]/table/tbody/tr/td[7]/text()',
         '//*[@id="list"]/table/tbody/tr/td[6]/text()']
sel = ['.table > tbody:nth-child(2) > tr > td:nth-child(1)']

# for x in range(1, 11):
#     getter = getproxy.ProxyGetter(host + str(x) + '/', xpath, sel)
#     proxies = getter.get_proxy()
#     print(proxies)
    # if proxies is not None:
    #     # for p in proxies:
    #     #     print(p)
    #     if len(proxies) == 0:
    #         print(x)
    # else:
    #     print(getter.get_exception())
    # del getter
getter = getproxy.ProxyGetter(host + '01/', xpath, sel)
proxies = getter.get_proxy()
print(type(proxies))