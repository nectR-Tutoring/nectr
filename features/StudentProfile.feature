@browser-grid
Feature: Student profile
  As a student
  I want a profile
  So tutors can see my information

Background:
  Given Mike has nectr account

Scenario: Mike wants to create profile
  Given Mike is signed into nectr
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
