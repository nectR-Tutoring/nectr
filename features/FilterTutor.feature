@browser-grid
Feature: Filter Tutors
  As a student
  I want the ability to filter tutors
  So I can find the right match

Background:
  Given Mike is on nectr web site

Scenario: Mike wants to filter tutors by subject
  Given Mike is on Search the hive page
  And Mike has not yet selected a tutor
  When Mike clicks on subject filter radio button
  Then all tutors who tutor that subject will be displayed

Scenario: Mike wants to filter tutors by subject
  Given Mike is on Search the hive page
  And Mike has not yet selected a tutor
  When Mike clicks <subject> radio button on subject filter
  Then all tutors who tutor <subject> will be displayed

Scenario: Mike wants to filter tutors by availability
  Given Mike is on Search the hive page
  And Mike has not yet selected a tutor
  When Mike clicks <dayOfTheWeek> radio button on availability filter
  Then all tutors who tutor on that day will be displayed

Scenario: Mike wants to filter tutors by price
  Given Mike is on Search the hive page
  And Mike has not yet selected a tutor
  When Mike wants to filter by hourly rate
  Then Mike should be able to filter using a slider
