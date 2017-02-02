import webapp2
import re


user_regEx = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and user_regEx.match(username)

pass_regEx = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and pass_regEx.match(password)

email_regEx = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or email_regEx.match(email)


def build_page(UN, PW, EM, MAIN):

    # form fields
    username_label = "<label>Username: </label>"
    username_input = "<input type='text' name='username' value=''/>"
    pw_label = "<label>Password: </label>"
    pw_input = "<input type='password' name='password' value='' />"
    pwVerify_label = "<label>Verify Password: </label>"
    pwVerify_input = "<input type='password' name='pwVerify' value='' />"
    email_label = "<label>Email (optional): </label>"
    email_input = "<input type='email' name='email' value='' />"

    if UN or MAIN:
        username_html = username_label + username_input + "<br>"
    else:
        username_html = username_label + username_input + "INVALID USERNAME" + "<br>"

    if PW or MAIN:
        pw_html = pw_label + pw_input + "<br>" 
    else:
        pw_html = pw_label + pw_input + "INVALID PASSWORD or VERIFICATION DOESN'T MATCH" + "<br>" 

    pw_verify_html = pwVerify_label + pwVerify_input + "<br>" 

    if EM or MAIN:
        email_html = email_label + email_input + "<br>"
    else:
        email_html = email_label + email_input + "INVALID EMAIL" + "<br>"

    # submit button
    submit_button = "<input type='submit' />"

    # signup form
    form = ("<form action=/welcome method='post'>" +
            username_html +
            pw_html +
            pw_verify_html +
            email_html +            
            submit_button + "<form/>")
    
    header = "<h2>Signup</h2>"

    return header + form 

class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = build_page(True, True, True, True)
        self.response.write(content)

    def post(self):
        userName = self.request.get('username')
        passWord = self.request.get('password')
        passVerify = self.request.get('pwVerify')
        eMail = self.request.get('email')

        # validation test stub
        self.response.write("<p>"+userName+"</p><p>"+passWord+"</p><p>"+passVerify+"</p><p>"+eMail+"</p>")
############


class Welcome(webapp2.RequestHandler):
    # validation test stub

    def post(self):
        userName = self.request.get('username')
        passWord = self.request.get('password')
        passVerify = self.request.get('pwVerify')
        eMail = self.request.get('email')

        if not valid_username(userName):
            content = build_page(userName, True, True, False)
            self.response.write(content)
        elif not valid_password(passWord) or (passWord != passVerify):
            content = build_page(True, passWord, True, False)
            self.response.write(content)
        elif not valid_email(eMail):
            content = build_page(True, True, eMail, False)
            self.response.write(content)
        else:
            self.response.write("Welcome, " + userName + "!")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
#    ('/signup', Signup),
    ('/welcome', Welcome)
], debug=True)
