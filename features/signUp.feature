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


    #Spongebob is a student at farmingdale and he
    #he is currenlty struggling in his Java class
    #and he wants to use nectr for the first time to
    #find a tutor.

    Scenario: Spongebob tries to sign up for nectr account but does not fill in correct info
      Given Spongebob is on home page of nectr
      And Spongebob does not have nectR account
      When Spongebob clicks menu
      And Spongebob clicks "Sign Up" button
      Then Spongebob is redirected to "Sign up" page
      And title of the page is "Signup"
      And page contains an h1 whos text is "Sign up"
      When Spongebob clicks on username text field
      And Spongebob enters "BikiniBottoms"
      And Spongebob clicks on E-mail text field
      And Spongebob enters "ayouf@farmingdale.edu"
      And Spongebob clicks on password text field
      And Spongbob enters "CrabbyPatty2"
      And Spongebob cicks on Password (again) field
      And Spongbob leaves this text field blank
      And Spongebob clicks "Sign Up" button
      Then Spongebob gets "please fill out this field" alert in Password (again) field
      And Spongebob clicks on Password (again) field
      And Spongbob enters "CrabbyPatty2"
      And Spongebob clicks "Sign Up" button
      Then Spongebob is redirected to "Confirm email" page
      And title of the page is "Verify Your E-mail Address"
      And page contains an h1 whos text is "Verify Your E-mail Address"
      When Spongebob checks his email "ayouf@farmingdale.edu"
      And Spongebob opens "confirm account" email
      And Spongebob clicks account confirmation link
      Then Spongebob is redirected to "BikiniBottoms" dashboard page

    Scenario: Spongebob tries to sign up providing correct info
      Given Spongebob is on home page of nectr
      And Spongebob does not have nectR account
      When Spongebob clicks menu
      And Spongebob clicks "Sign Up" button
      Then Spongebob is redirected to "Sign up" page
      And title of the page is "Signup"
      And page contains an h1 whos text is "Sign up"
      When Spongebob clicks on username text field
      And Spongebob enters "BikiniBottoms"
      And Spongebob clicks on E-mail text field
      And Spongebob enters "ayouf@farmingdale.edu"
      And Spongebob clicks on password text field
      And Spongbob enters "CrabbyPatty2"
      And Spongebob cicks on Password (again) field
      And Spongbob enters "CrabbyPatty2"
      And Spongebob clicks "Sign Up" button
      Then Spongebob is redirected to "Confirm email" page
      And title of the page is "Verify Your E-mail Address"
      And page contains an h1 whos text is "Verify Your E-mail Address"
      When Spongebob checks his email "ayouf@farmingdale.edu"
      And Spongebob opens "confirm account" email
      And Spongebob clicks account confirmation link
      Then Spongebob is redirected to "BikiniBottoms" dashboard page
