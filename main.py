from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = "SET PATH HERE!"
        return super().do_GET()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        password = self.rfile.read(content_length).decode('utf-8')

        if password == "67611":
            response = "success"
        else:
            response = "failure"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Content-length', len(response))
        self.end_headers()
        self.wfile.write(response.encode())


def start_http_server():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, CustomHandler)
        print(f"Server started on {httpd.server_address}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("Server stopped")

if __name__ == "__main__":
    start_http_server()
