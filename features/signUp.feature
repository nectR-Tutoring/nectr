@future
Feature: Signup from Website
As a visitor
I want to sign up for an account
So I can find a tutor


Background:
  Given Charlie is not yet registered
  Given Mike is not yet registered
  Given Enoc is not yet registered
  Given Brandon is not yet registered
  Given Juan is not yet registered

Scenario: Charlie is not a student at farmingdale
  Given Charlie is on the homepage
  When Charlie clicks on sign up link
  And is asked "are you a farmingdale student"
  And he says no
  Then he is redirected to the "not a farmingdale student" page

Scenario: Mike is a student at farmingdale
  Given Mike is on the homepage
  When mike clicks on sign up link
  And is asked "are you a farmingdale student"
  And he says yes
  Then he is redirected to the "sign up form"

  Scenario: Enoc is a student at farmingdale
    Given Enoc is on the seacrch the hive page
    When enoc clicks on sign up link
    And is asked "are you a farmingdale student"
    And he says yes
    Then is redirected to the "sign up" form

  Scenario: Brandon is a student at farmingdale
    Given brandon is on the about nectr page
    When brandon clicks on sign up link
    And is asked "are you a farmingdale student"
    And he says yes
    Then is redirected to the "sign up" form

  Scenario: Juan is a student at farmingdale
    Given juan is on the how it works page
    When juan clicks on sign up link
    And is asked "are you a farmingdale student"
    And he says yes
    Then is redirected to the "sign up" form








