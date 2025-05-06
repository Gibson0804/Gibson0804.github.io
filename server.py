import http.server
import socketserver
import argparse

parser = argparse.ArgumentParser(description="Simple static file server")
parser.add_argument("--port", type=int, default=8000, help="Port to serve on (default: 8000)")
args = parser.parse_args()
PORT = args.port

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
