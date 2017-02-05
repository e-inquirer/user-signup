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


def build_page(UN, PW, EM, errFlag):

    # form fields
    username_label = "<label>Username: </label>"
    username_input = "<input type='text' name='username' />"
    pw_label = "<label>Password: </label>"
    pw_input = "<input type='password' name='password'  />"
    pwVerify_label = "<label>Verify Password: </label>"
    pwVerify_input = "<input type='password' name='pwVerify'  />"
    email_label = "<label>Email (optional): </label>"
    email_input = "<input type='email' name='email'  />"
  
    username_html = username_label + username_input + "<br>"
    pw_html = pw_label + pw_input + "<br>" 
    pw_verify_html = pwVerify_label + pwVerify_input + "<br>" 
    email_html = email_label + email_input + "<br>"
#    form_tag = "<form action=/welcome method='post'>"
    form_tag = "<form action=/signup method='post'>"
    
    if errFlag:
        username_input = "<input type='text' name='username' value='" + str(UN) + "' />"
        email_input = "<input type='email' name='email' value='" + str(EM) + "' />"
        if not valid_username(UN):
            username_html = username_label + username_input + "INVALID USERNAME" + "<br>"           
            form_tag = "<form action=/signup method='post'>"
#        else:
#            form_tag = "<form action=/welcome method='post'>"

        if not valid_password(PW):
            pw_html = pw_label + pw_input + "INVALID PASSWORD or VERIFICATION DOESN'T MATCH" + "<br>" 
            form_tag = "<form action=/signup method='post'>"
#        else:
#            form_tag = "<form action=/welcome method='post'>"
        
        if not valid_email(EM):
            email_html = email_label + email_input + "INVALID EMAIL" + "<br>"
            form_tag = "<form action=/signup method='post'>"
#    else:
#        form_tag = "<form action=/welcome method='post'>"

    # submit button
    submit_button = "<input type='submit' />"

    # signup form
    form = (form_tag +
            username_html +
            pw_html +
            pw_verify_html +
            email_html +            
            submit_button + "<form/>")
    
    header = "<h2>Signup</h2>"

    return header + form 

class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = build_page("", "", "", False)
        self.response.write(content)

    def post(self):
        userName = self.request.get('username')
        passWord = self.request.get('password')
        passVerify = self.request.get('pwVerify')
        eMail = self.request.get('email')

        if valid_username(userName) and valid_password(passWord) and passWord != passVerify and valid_email(eMail):
            error_flag = False
            self.redirect('/welcome')
        else:
            error_flag = True
            self.redirect('/signup')
    
        content = build_page(userName, passWord, eMail, error_flag)
        self.response.write(content)


#
#        # validation test stub
#        self.response.write("<p>"+userName+"</p><p>"+passWord+"</p><p>"+passVerify+"</p><p>"+eMail+"</p>")
############

class Signup(webapp2.RequestHandler):

    def post(self):
        userName = self.request.get('username')
        passWord = self.request.get('password')
        passVerify = self.request.get('pwVerify')
        eMail = self.request.get('email')
        
        if valid_username(userName) and valid_password(passWord) and passWord != passVerify and valid_email(eMail):
            error_flag = False
            self.redirect('/welcome')
        else:
            error_flag = True
#            self.redirect('/signup')
    
        content = build_page(userName, passWord, eMail, error_flag)
        self.response.write(content)


class Welcome(webapp2.RequestHandler):
    # validation test stub

    def post(self):
        userName = self.request.get('username')
#        passWord = self.request.get('password')
#        passVerify = self.request.get('pwVerify')
#        eMail = self.request.get('email')
#
#        if valid_username(userName) and valid_password(passWord) and passWord != passVerify and valid_email(eMail):
#            error_flag = False
#            self.redirect('/welcome')
#        else:
#            error_flag = True
#            self.redirect('/signup')

        self.response.write("Welcome, " + userName + "!")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', Signup),
    ('/welcome', Welcome)
], debug=True)
