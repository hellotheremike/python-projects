import httplib
def main():
    checkWebServer('www.python.org',80,'/')
    
def checkWebServer(host, port, path):
    h = httplib.HTTPConnection(host, port)
    h.request('GET', path)
    resp = h.getresponse()
    print 'HTTP response'
    print 'status = ', resp.status
    print 'reason = ', resp.reason
    print 'HTTP Headers'
    for hdr in resp.getheaders():
        print '\t%s: %s' % hdr

main()
