Feature: Join the hive

As a student
I want to become a tutor
So I can tutor other students

Background:
  Given mike does not have a nectr account
  Given charlie has a nectr student account
  Given brandon has a nectr student account 
  Given Juan has a nectr student account

Scenario: Mike tries to join the hive
  Given mike is not signed in
  And mike clicks on join the hive
  Then mike is redirected to login page

Scenario: Charlie tries to join the hive
  Given charlie is signed in
  And charlie clicks on join the hive page
  Then charlie is redirected to join the hive page
  And presented with join the hive application

Scenario: Brandon submits incomplete application
  Given brandon is on join the hive page
  And brandon does not complete application
  When brandon clicks on submit button
  Then application is reloaded with information that has already been filled
  And is incomplete fields are highlighted

Scenario: Juan submits complete applicaiton
  Given juan is on join the hive page
  And juan completes application
  When juan clicks on submit button
  Then juan is presened with success message
