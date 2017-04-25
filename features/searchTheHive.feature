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

  #Billy is a student at farmingdale and needs to find
  #a math tutor to prepare for an upcoming exam so he
  #pulls out his laptop and goes to nectr's website
  #and goes to search the hive page. Billy already has
  #a nectr account is already signed in
  #Billy is also struglling in his C++ programming class
  #so he also wants to search for C++ tutors

  Scenario: Billy searches nectr for math tutors
    Given there are 15 Math tutors
    Given Billy is signed into nectr
    And Billy is on search the hive page
    When Billy clicks on search bar
    And Billy enters "Math"
    And Billy clicks "Submit" button
    Then search results are loaded on search the hive page
    And 10 tutor search results are displayed
    And each search result contains "view tutor profile" button
    When Billy clicks "more results" button
    Then remaining 5 tutors are diaplyed


    Scenario: Billy searches nectr for C++ programming tutors
      Given there are 5 C++ Programming tutors
      Given Billy is signed into nectr
      And Billy is on search the hive page
      When Billy clicks on search bar
      And Billy enters "C++ Programming"
      And Billy clicks "Submit" button
      Then search results are loaded on search the hive page
      And 5 tutor search results are displayed
      And each search result contains "view tutor profile" button
