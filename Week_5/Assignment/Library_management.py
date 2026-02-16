"""Question 1: Build a Barebone REST API

Create a simple REST API server without using any web framework (no Flask, FastAPI, Django, etc.) that manages a collection of books. Your API should:
Handle GET /books - Return all books as JSON
Handle GET /books/{id} - Return a specific book
Handle POST /books - Add a new book (accept JSON body with title, author, year)
Handle PUT /books/{id} - Update an existing book
Handle DELETE /books/{id} - Remove a book
Store data in memory (Python list/dict)
Parse HTTP requests manually and construct proper HTTP responses
Return appropriate status codes (200, 201, 404, 400, etc.)
"""

import http.server
import socketserver
import json

books = {
    "1": {"Title": "abc", "Author": "authorabc", "Year": "1234"},
    "2": {"Title": "bcd", "Author": "authorbcd", "Year": "4567"},
    "3": {"Title": "cde", "Author": "authorcde", "Year": "8764"},
    "4": {"Title": "efg", "Author": "authorefg", "Year": "3456"},
}


class Handler(http.server.BaseHTTPRequestHandler):

    def _send_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if self.path == "/books":
            self._send_response(200, books)

        elif self.path.startswith("/books/"):
            book_id = self.path.split("/")[-1]
            if book_id in books:
                self._send_response(200, books[book_id])
            else:
                self._send_response(404, {"error": "Book not found"})
        else:
            self._send_response(404, {"error": "Invalid endpoint"})

    def do_POST(self):
        if self.path == "/books":
            try:
                content_length = int(self.headers["Content-Length"])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data)

                new_id = str(len(books) + 1)
                books[new_id] = data

                self._send_response(201, {"message": "Book added", "id": new_id})

            except Exception as e:
                self._send_response(500, {"error": e})

    def do_PUT(self):
        if self.path.startswith("/books/"):
            try:
                book_id = self.path.split("/")[-1]

                if book_id not in books:
                    self._send_response(404, {"error": "Book not found"})
                    return

                content_length = int(self.headers["Content-Length"])
                put_data = self.rfile.read(content_length)
                data = json.loads(put_data)

                books[book_id] = data
                self._send_response(200, {"message": "Book updated"})

            except Exception as e:
                self._send_response(500, {"error": e})

    def do_DELETE(self):
        if self.path.startswith("/books/"):
            try:
                book_id = self.path.split("/")[-1]

                if book_id in books:
                    del books[book_id]
                    self._send_response(200, {"message": "Book deleted"})
                else:
                    self._send_response(404, {"error": "Book not found"})

            except Exception as e:
                self._send_response(500, {"error": e})


def run_server():
    with socketserver.ThreadingTCPServer(("", 8000), Handler) as httpd:
        print("Server running at http://localhost:8000")
        httpd.serve_forever()


if __name__ == "__main__":
    run_server()
