@browser-grid
Feature: Login
  As a student
  I want to sign into my account
  So I can find a tutor


Scenario: Mike clicks login before creating account
  Given Mike is not registered to nectr
  Given mike is on nectr site
  When mike clicks on menu button
  And mike clicks on login button on menu
  Then mike is redirected to Login page
  When mike clicks on "sign_up_redirect"
  Then mike is redirected to Signup page

Scenario: Charlie enters correct credentials
  Given Charlie is registered to nectr
  Given charlie is on nectr site
  When charlie clicks on menu button
  And charlie clicks on login
  Then charlie is redirected to Login page
  When Charlie enters his correct username
  And Charlie enters his correct password
  And Charlie clicks on sign in


Scenario: Enoc enters incorrect credentials
  Given Enoc is registered to nectr
  Given enoc is on nectr site
  When enoc clicks on menu button
  And enoc clicks on nav_Login button
#  And enoc is redirected to Login page
#  And enoc enters incorrect username or password
#  And enoc clicks the sign in button
#  Then enoc is given message that states "incorrect username or password"
#  And login form is reloaded with blank username and password fields

Scenario: Brandon enters correct credentials
  Given Brandon is registered to nectr
  And Brandon is on home page of nectr
  When Brandon clicks "Menu"
  And Brandon clicks "Log In" button
  Then Brandon is redirected to "Sign In" page
  When Brandon clicks on username text field
  And Brandon enters "Cashmeousside"
  And Brandon clicks on password text field
  And Brandon enters "Howboudat"
  And Brandon cicks "Sign In" button
  Then Brandon is redirected to "Dashboard" page

  #Brandon is a student at Farmingdale and currently
  #taking Math and Android Programming courses.
  #Brandon is struggling in his math class and needs tutoring
  #ASAP to prepare for his exam in a few days
  #Brandon has already created a nectr account but has never used it
  #Brandons tells his friend Mike about nectr and mike is
  #intereseted too because he is struggling in his java class

Scenario: Brandon enters correct credentials
  Given Brandon is registered to nectr
  And Brandon is on home page of nectr
  And Brandon is not signed in
  When Brandon clicks "Menu"
  And Brandon clicks "Log In" button
  Then Brandon is redirected to "Sign In" page
  When Brandon clicks on username text field
  And Brandon enters "Cashmeousside"
  And Brandon clicks on password text field
  And Brandon enters "Howboudat"
  And Brandon cicks "Sign In" button
  Then Brandon is redirected to "Dashboard" page

Scenario: Brandon tries to sign in again but enters incorrect credentials
  Given Brandon's registered to nectR with username is "Cashmeousside"
  And Brandon's password is Howboudat
  And Brandon is on home page of nectr
  And Brandon is not signed in
  When Brandon clicks "Menu"
  And Brandon clicks "Log In" button
  Then Brandon is redirected to "Login" page
  And title of the page is "Login"
  And page contains an h1 whos text is "Sign In"
  When Brandon clicks on username text field
  And Brandon enters "Cashmeousside"
  And Brandon clicks on password text field
  And Brandon enters "Howboudatt"
  And Brandon cicks "Sign In" button
  Then Brandon is presented with an alert
  And username text field is cleared
  And password text field is cleared

#Scenario: Mike goes to sign in page but does not have account
