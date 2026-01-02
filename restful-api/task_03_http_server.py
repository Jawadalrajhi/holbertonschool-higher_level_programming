#!/usr/bin/python3

"""
Set up a basic web server using the http.server module.
Handle different types of HTTP requests (GET, POST, etc.).
Serve JSON data in response to specific endpoints.
"""

import http.server
import socketserver
import json

# Define the port to run the server on
PORT = 8000


class BasicHttpServer(http.server.BaseHTTPRequestHandler):
    """
    BasicHttpServer

    Set up the HTTP server to handle GET requests and respond with a simple
    message.

    Args:
        http (_type_): The HTTP request handler class that will process
        incoming requests
    """
    def do_GET(self):
        """
        do_GET
        Handle GET requests to the server. Respond with a simple message.
        """

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/data":
            data_set = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Convert python dict into JSON and send it
            self.wfile.write(json.dumps(data_set).encode('utf-8'))

        elif self.path == "/info":
            data_set = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Convert python dict into JSON and send it
            self.wfile.write(json.dumps(data_set).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


# Set up the server to listen on the specified port
with socketserver.TCPServer(("", PORT), BasicHttpServer) as httpd:
    httpd.serve_forever()
