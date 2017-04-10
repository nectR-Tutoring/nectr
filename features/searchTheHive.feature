Feature: Search the hive
  As a user
  I want to search for tutors 
  So I can find the right tutor 
  
 Background:
  Given brandon is not signed into nectr
  Given mike is signed into nectr
  
Scenario: Brandon searches nectr
  Given brandon is on search the hive page 
  When brandon types in what he is looking for in search box
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
