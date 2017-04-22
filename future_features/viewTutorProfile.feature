Feature: View tutor profile 
  As a user 
  I want to view tutor profiles
  So I can see information about tutor and contact 
  
 Bacground:
  Given mike is signed into nectr
  Given brandon is not signed into nectr
  
 Scenario: Mike clicks on tutor profile 
  Given mike is on search results page 
  When mike clicks on view tutor profile button 
  Then mike is redirected to tutors profile 
  And mike will see a "contact tutor" button
  
Scenario: Brandon clicks on tutor profile 
  Given brandon is on search results page 
  When brandon clicks on view tutor profile button 
  Then brandon is redirected to tutors profile 
  And brandon will see a "sign in to contact tutor" button
