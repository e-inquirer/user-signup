import webapp2

class MainHandler(webapp2.RequestHandler):
    

    def get(self):
            self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', Signup)
    ('/welcome', Welcome),
], debug=True)