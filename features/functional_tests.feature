## Created by BrandonFox at 4/5/2017
@browser-grid
Feature: Test Functionality of Nectr
  As a developer of nectR
  I want to make sure the basic functionality I expect is working
  So that I can be sure the server is running and I can proceed making awesome stuff
#
#  Scenario: Server is responding to requests
#    # Enter steps here
#    Given The Server is Running on "Localhost"
#    And On Port 8000
#    When I visit http://localhost:8000
#    Then I should get a 200 response

  Scenario: Get and Test '200' response on all 'hrefs' for Given Page
    Given I am on '/' with 'Home'
    When I request each 'href'
    Then I should get a good response

  Scenario: Get and Test '200' response on all 'hrefs' for Given Page
    Given I am on '/about' with 'about'
    When I request each 'href'
    Then I should get a good response

  Scenario: Get and Test '200' response on all 'hrefs' for Given Page
    Given I am on '/users' with 'Sign'
    When I request each 'href'
    Then I should get a good response
