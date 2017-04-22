Feature: Search the hive
  As a user
  I want to search for tutors
  So I can find the right tutor

 Background:
   # One day during class, Brandon decides he needs
   # Tutoring in his Android class
   # He already has an account but
   # Quickly goes to nectr's website
  Given Brandon is a registered user
   ######### And Brandon is not signed into nectr ########
   # In the class down the hall, Mike
   # is also having trouble. His Java class
   # has gotten hard and he needs some help
   # so he opens his laptop and returns to nectr's
   # website.
   Given Mike is a registered user
   And Mike is signed into nectr

Scenario: Brandon searches nectr
  Given Brandon is on search the hive page
  When Brandon types "Computer Science" in search box
  And clicks search the hive button
  Then he is directed to list of tutors page
  And he can view preview of tutor profile
  And he will see a view profile button

Scenario: Mike searches nectr
  Given mike is on search the hive page
  When mike types in what he is looking for in search box
  And clicks search the hive button
  Then he is directed to list of tutors page
  And he can view preview of tutor profile
  And he will see a view profile button

#------------------------------------------------------------------
  #Charlie is a student at Farmingdale and he is enrolled
  #in a Java class. He has an exam coming up in a few days and needs
  #help preparing ASAP. He pulls out his laptop and goes to the nectr web site.
  #He already has a nectR account and is already signed in and on the
  #search the hive page

  Scenario: Charlie searches nectR
    Given Charlie is on the search the hive page
    And Charlie clicks on search bar
    And CHarlie types in "course name"
    When Charlie presses enter on keyboard
    Then Charlie is redirected to a "search results" page
    And the "search results" page contains a table of 10 rows
    And the each row contains tutor profile preview
    And each tutor profile preview displays tutor name
    And tutor profile picture
    And tutor rating
    And hourly rate
    When Charlie clicks on one of the rows
    Then Charlie is redirected to tutors profile
