import webapp2

def build_page(textarea_content):
    username_label = "<label>Username: </label>"
    username_input = "<input type='text' name='username' />"
    pw_label = "<label>Password: </label>"
    pw_input = "<input type='password' name='password' />"




    # submit button
    submit_button = "<input type='submit' />"

    # signup form
    form = ("<form method='post'>" +
            username_label + username_input + "<br>" +
            pw_label + pw_input + "<br>" +
            submit_button + "<form/")
    
    header = "<h2>Signup</h2>"

    return header + form 

class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = build_page("")
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
#    ('/signup', Signup),
#    ('/welcome', Welcome),
], debug=True)
