import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")
if __name__ == "__main__":
    app = tornado.web.Application(handlers=[
        (r"/", MainHandler),
    ]) 
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
