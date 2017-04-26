@future
Feature: Student profile
  As a student
  I want a profile
  So tutors can see my information

Background:
  Given Mike has nectr account

Scenario: Mike wants to create profile
  Given Mike is signed into his nectr account
  When Mike clicks on "My Profile"
  And Mike is redirected to nectr profile
  Then "Hello <Mike's username>" is shown
  And Mike can add information to profile

Scenario: Mike wants to update personal information on profile page
  Given Mike is on his profile page
  When Mike clicks on "Edit" button on "personal information" section of profile
  Then Mike can edit or add information to "personal information"

Scenario: Mike wants to update contact information on profile page
  Given Mike is on his profile page
  When Mike clicks on "Edit" button on "contact information" section of profile
  Then Mike can edit or add information to "contact information"

Scenario: Mike wants to update communication preferences on profile page
  Given Mike is on his profile page
  When Mike clicks on "Edit" button on "communication preferences" section of profile
  Then Mike can edit or add information to "communication preferences"


#Mike is a student at Farmingdale and just created a brand new nectr
#account and wants to add information to his profile

Scenario: Mike goes to his profile page
  Given Mike is signed into nectr
  And Mike's username is MikeAyoub
  And Mike's password is JavaSucks123
  And Mike is on his "Dashboard" page
  And title of page is "MikeAyoub" dashboard
  When Mike clicks on "My Profile" link
  Then Mike is redirected to "MikeAyoub" private profile page
  And "Hello <Mike's username>" is shown

Scenario: Mike updates personal information on profile page
  Given Mike is on his profile page
  When Mike clicks on "Edit" button on "personal information" section of his profile
  And Mike clicks on "name" text field
  And Mike enters "Mike Ayoub"
  And Mike clicks on "Student Class Level" text field
  And Mike enters "Senior"
  And Mike clicks "Save" button
  Then Mike's personal information is saved to his profile

Scenario: Mike updates contact information on profile page
  Given Mike is on his profile page
  When Mike clicks on "Edit" button on "contact information" section of his profile
  And Mike clicks on "Email" text field
  And Mike enters "ayouf@farmingdale.edu"
  And Mike clicks on "Phone number" text field
  And Mike enters "6318735489"
  And Mike clicks "Save" button
  Then Mike's contact information is saved to his profile
