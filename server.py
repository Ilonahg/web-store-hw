from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open("contacts.html", "r", encoding="utf-8") as file:
                content = file.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))

        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run():
    server_address = ("", 8000)  # Сервер на порту 8000
    httpd = HTTPServer(server_address, MyHandler)
    print("Сервер запущен на http://localhost:8000 ...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
