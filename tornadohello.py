# WebSocket test

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.websocket

class MainHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.write_message("Hello, world")
    
    def check_origin(self, origin):
        return True

    def on_message(self, message):
        print message
    
    def on_close(self):
        pass


application = tornado.web.Application([
        (r"/", MainHandler),
])

http_server = tornado.httpserver.HTTPServer(application)

if __name__ == "__main__":
                                                
    #application.listen(8888)
    http_server.listen(8888) 
    tornado.ioloop.IOLoop.instance().start()
