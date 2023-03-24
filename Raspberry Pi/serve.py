from http.server import HTTPServer, SimpleHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        output = open('T_log.json', "r")
        data = json.load(output)
        data = json.dumps(data)
        print(str(data))

        self.wfile.write(bytes(str(data), 'UTF-8'))
        output.close()


httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
