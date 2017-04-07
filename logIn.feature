Feature: Login  
  As a student
  I want to sign into my account
  So I can find a tutor 
  
Background:
  Given mike is not registered to nectr
  Given charlie is registered to nectr
  Given enoc is registered to nectr
  
  
Scenario: Mike clicks login before creating account
  Given mike is on nectr site
  When mike clicks on login button
  And is redirected to login page 
  And mike clicks on "don't have account"
  Then mike is redirected to signup form
  
Scenario: Charlie enters correct credentials
  Given charlie is on nectr site
  When charlie clicks on login button
  And is redirected to login page 
  And charlie enters correct username and password
  And clicks on the sign in button
  Then charlie is redirected to dashboard
  
Scenario: Enoc enters incorrect credentials
  Given enoc is on nectr site
  When enoc clicks on login button
  And is redirected to login page 
  And enoc enters incorrect username or password
  And enoc clicks the sign in button
  Then enoc is given message that states "incorrect username or password"
  And login form is reloaded with blank username and password fields
  
