Feature: Contact tutor
  As a student
  I want to contact a tutor
  So I can set up a meeting

Background:
  Given Mike is signed into nectr
  Given Brandon is not signed into nectr

Scenario: Mike wants to contact tutor
  Given mike is on tutors profile
  When mike clicks "contact <tutor name>" button
  Then mike will be redirected to message tutor form

Scenario: Brandon wants to contact tutor
  Given brandon is on tutors profile
  When brandon clicks "contact <tutor name>" button
  Then brandon will be redirected to sign up or sign in page
