#!/usr/bin/env python3
"""
Simple HTTP server for Effective Mobile test task.
Responds with "Hello from Effective Mobile!" on GET / request.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import sys
import signal


class SimpleHandler(BaseHTTPRequestHandler):
    """HTTP request handler with custom responses."""
    
    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(b'"Hello from Effective Mobile!"')
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'Not Found')

    def log_message(self, format, *args):
        """Custom logging format."""
        print(f"[Backend] {self.client_address[0]} - {format % args}", flush=True)


class GracefulServer:
    """Server wrapper with graceful shutdown."""
    
    def __init__(self, port=8080):
        self.port = port
        self.server = HTTPServer(('0.0.0.0', port), SimpleHandler)
        
    def handle_signal(self, signum, frame):
        """Handle shutdown signals."""
        print(f"\n[Backend] Received signal {signum}, shutting down...", flush=True)
        self.server.server_close()
        sys.exit(0)
        
    def run(self):
        """Start the server."""
        # Register signal handlers
        signal.signal(signal.SIGTERM, self.handle_signal)
        signal.signal(signal.SIGINT, self.handle_signal)
        
        print(f'[Backend] Starting server on 0.0.0.0:{self.port}', flush=True)
        print(f'[Backend] Press Ctrl+C to stop', flush=True)
        
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            print("\n[Backend] Keyboard interrupt received", flush=True)
        finally:
            self.server.server_close()
            print("[Backend] Server stopped", flush=True)


def main():
    """Main entry point."""
    port = int(os.environ.get('PORT', 8080))
    
    try:
        server = GracefulServer(port)
        server.run()
    except Exception as e:
        print(f"[Backend] Fatal error: {e}", file=sys.stderr, flush=True)
        sys.exit(1)


if __name__ == '__main__':
    main()