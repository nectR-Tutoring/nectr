# Created by bfox at 3/11/17
@browser-grid
Feature: Connection to nectR
  As a nectR developer
  I want to be able to access the web app
  So I can use nectR

  Scenario: Connect to "/" using browser
    When I go to "/"
    Then I should see a page with title "Home"

  Scenario: Connect to "/" using browser to view menu
    When I go to "/"
    Then I should see a page with title "Home"
    When I press the "menu"
    Then There should be a "SIGN UP" link with name "nav_SignUp"
    Then There should be a "LOG IN" link with name "nav_Login"

