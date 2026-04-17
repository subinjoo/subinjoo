#!/usr/bin/env python3
"""
serve.py — local HTTP server for KimmBot demo
Usage:  python3 serve.py
Then open: http://localhost:8080
"""
import http.server, socketserver, webbrowser, os, sys

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # silence request logs

print(f"KimmBot Demo  →  http://localhost:{PORT}")
print("Press Ctrl+C to stop.\n")
webbrowser.open(f"http://localhost:{PORT}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
