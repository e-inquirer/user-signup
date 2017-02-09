import webapp2
import re


dictionary = {'UN':'', 'PW':'', 'PV':'', 'EM':'', 'counter':0}

user_regEx = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and user_regEx.match(username)

pass_regEx = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and pass_regEx.match(password)

email_regEx = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or email_regEx.match(email)


def build_page(DICT):

    # form fields
    username_label = "<label>Username: </label>"
    username_input = "<input type='text' value='{UN}' name='username' />".format(**DICT)
    pw_label = "<label>Password: </label>"
    pw_input = "<input type='password' value='' name='password'  />"
    pwVerify_label = "<label>Verify Password: </label>"
    pwVerify_input = "<input type='password' value='' name='pwVerify'  />"
    email_label = "<label>Email (optional): </label>"
    email_input = "<input type='email' value='{EM}' name='email' />".format(**DICT)
  
    username_html = username_label + username_input + "<br>"
    pw_html = pw_label + pw_input + "<br>" 
    pw_verify_html = pwVerify_label + pwVerify_input + "<br>" 
    email_html = email_label + email_input + "<br>"
    form_tag = "<form action=/ method='post'>"
    
    if dictionary['counter'] > 0:
        if not valid_username(DICT['UN']):
            username_html = username_label + username_input + "INVALID USERNAME" + "<br>"           

        if not valid_password(DICT['PW']):
            pw_html = pw_label + pw_input + "INVALID PASSWORD" + "<br>" 

        if DICT['PV'] != DICT['PW'] or DICT['PV'] == '':
            pw_verify_html = pwVerify_label + pwVerify_input + "VERIFICATION DOES NOT MATCH" + "<br>"
        
        if not valid_email(DICT['EM']):
            email_html = email_label + email_input + "INVALID EMAIL" + "<br>"

    dictionary['counter'] += 1

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
        content = build_page(dictionary)
        self.response.write(content)

    def post(self):
        dictionary.update({'UN':self.request.get('username')})
        dictionary.update({'PW':self.request.get('password')})
        dictionary.update({'PV':self.request.get('pwVerify')})
        dictionary.update({'EM':self.request.get('email')})

        if valid_username(dictionary['UN']) and valid_password(dictionary['PW']) and dictionary['PW'] == dictionary['PV'] and valid_email(dictionary['EM']):
            self.redirect('/welcome')
        else:
            content = build_page(dictionary)
            self.response.write(content)

class Welcome(webapp2.RequestHandler):

    def get(self):
        userName = dictionary['UN']

        self.response.write("Welcome, " + userName + "!")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
