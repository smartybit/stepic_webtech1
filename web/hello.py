#!/usr/bin/python


def app(environ, start_response):
      request = environ['QUERY_STRING']

      start_response("200 OK", [
          ("Content-Type", "text/plain"),
      ])
      return [request.replace('&','\n') ]
