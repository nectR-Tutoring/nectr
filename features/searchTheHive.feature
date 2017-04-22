@WIP
@browser-grid
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
  And Brandon clicks search the hive button
  Then Brandon is directed to list of tutors page
  And the search text "Computer Science" is in title
  And he can view preview of tutor profile
#  And he will see a view profile button

Scenario: Mike searches nectr
  Given mike is on search the hive page
  When mike types in what he is looking for in search box
  And Mike clicks search the hive button
  Then he is directed to list of tutors page
  And he can view preview of tutor profile
#  And he will see a view profile button

Scenario: Chris searchs nectr for a tutor
  Given Chris is on the home page
  # Chris wants to search for a tutor for his Computer Science Class
  When Chris types "Computer Science" in search box and presses ENTER
  Then Chris is directed to list of tutors page
  And Chris's search "Computer Science" is in the title

Scenario: Steve searchs nectr for a tutor
  Given Steve is on the home page
  When Steve clicks "language_quick_search_button"
  Then Steve is directed to list of tutors page
  And Steve's search "Language" is in the title

Scenario: Tom searchs nectr for a tutor
  Given Tom is on the home page
  When Tom clicks "math_quick_search_button"
  Then Tom is directed to list of tutors page
  And Tom's search "Math" is in the title
