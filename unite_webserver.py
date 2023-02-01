from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests
from bs4 import BeautifulSoup
import datetime as dt
from datetime import timedelta

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Unite Last Logged</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        result = getTime_S(self.path[1:])
        self.wfile.write(bytes("<p>" + str(result) + "</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        
def getTime_S(names):
    UTC_offset = -6
    url = 'http://www.uniteapi.dev/p/'
    url2 = url + names
    r = requests.get(url2)
    val = BeautifulSoup(r.text, 'html.parser')
    i = 0        
    full = r.text.split('Last online:')
    full_s = full[1][0:50]
    temp2 = full_s.split('>')
    final = temp2[1][0:-3]
    now = dt.datetime.now()
    final_t = dt.datetime.strptime(final, '%d-%m-%Y %H:%M')
    final_t = final_t + timedelta(hours=UTC_offset)
    time_diff = now - final_t
    return 'Name: ' + str(names) +' -> Last online: ' + \
                 str(final_t) + " :: " + str(time_diff.days) + " days"

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
