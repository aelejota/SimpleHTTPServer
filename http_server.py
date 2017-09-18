import SimpleHTTPServer
import SocketServer
import sys
import json, datetime

PORT = 8080

message = {}

class MyHTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        message['@timestamp'] = '%s%s' % (datetime.datetime.now().isoformat()[:-3], 'Z')
        message['severity'] = 'info'
        message['description'] = format%args
        print json.dumps(message)

Handler = MyHTTPHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
#print "serving at port", PORT
httpd.serve_forever()
