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
  And charlie clicks on nav_Login button
  Then charlie is redirected to Login page
  When Charlie enters his correct username
  And Charlie enters his correct password
  And Charlie clicks on the submit button
  Then charlie is redirected to dashboard

Scenario: Enoc enters incorrect credentials
  Given Enoc is registered to nectr
  Given enoc is on nectr site
  When enoc clicks on nav_Login button
#  And enoc is redirected to Login page
#  And enoc enters incorrect username or password
#  And enoc clicks the sign in button
#  Then enoc is given message that states "incorrect username or password"
#  And login form is reloaded with blank username and password fields

