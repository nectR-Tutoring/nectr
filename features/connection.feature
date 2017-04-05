# Created by bfox at 3/11/17
Feature: Connection to nectR
  As a nectR visitor
  I want to be able to access the web app
  So I can use nectR

  Scenario: Visitor goes to "/"
    Given I go to "/"
    Then I should see the "Home Page"
    And There should be a "Sign In" link
    And There should be a "Sign Up" link
