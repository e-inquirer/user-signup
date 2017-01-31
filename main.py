import webapp2

def build_page(textarea_content):

    header = "<h2>Signup</h2>"

    return header

class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = build_page("")
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
#    ('/signup', Signup),
#    ('/welcome', Welcome),
], debug=True)
