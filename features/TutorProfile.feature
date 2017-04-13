Feature: Tutor Profile
  As a tutor
  I want a profile
  So students can see my informatiom

Background:
  Given Mike is a nect tutor and has already established student profile

Scenario: Mike wants to create a tutor profile
  Given Mike is signed into nectr
  And Mike is on tutor interface
  When Mike clicks on "My Profile"
  Then "Hello <Mike's username>" is shown
  And Mike can add information to his profile

Scenario: Mike wants to update About Me section on tutor profile page
  Given Mike is on his tutor profile page
  When Mike clicks on "Edit" button on "About Me" section of tutor profile
  Then Mike can edit his about me

Scenario: Mike wants to update subjects taught on tutor profile page
  Given Mike is on his tutor profile page
  When Mike clicks on "Edit" button on "subjects taught" section of tutor profile
  Then Mike can edit or add courses and subjects he offers tutoring in

Scenario: Mike wants to update availability on tutor profile page
  Given Mike is on his tutor profile page
  When Mike clicks on "Edit" button on "availability" section of tutor profile
  Then Mike can edit or add his days and times he is available

Scenario: Mike wants to update his pricing on tutor profile page
  Given Mike is on his tutor profile page
  When Mike clicks on "Edit" button on "Pricing" section of tutor profile
  Then Mike can update the price he charges for tutoring
