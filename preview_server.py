"""Keep the local website review available until the server is stopped."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

root=Path(__file__).parent/'dist'
print('Montesinos Electric preview: http://127.0.0.1:4173/',flush=True)
ThreadingHTTPServer(('127.0.0.1',4173),partial(Handler,directory=str(root))).serve_forever()
