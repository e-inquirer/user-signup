import webapp2

def build_page(textarea_content):
    username_label = "<label>Username: </label>"
    username_input = "<input type='text' name='username' />"

    # submit button
    submit = "<input type='submit' />"

    # signup form
    ###
    
    header = "<h2>Signup</h2>"

    return (header + username_label + username_input)

class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = build_page("")
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
#    ('/signup', Signup),
#    ('/welcome', Welcome),
], debug=True)
