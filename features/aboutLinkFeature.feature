@browser-grid
Feature: aboutLinkFeature
As a visitor
I want to click on "About" link
so I can find out more information about nectr


#Mike is a student who is visiting nectr web site
# and opens up home page of web site

Scenario: Mike clicks on about page
  Given Mike is on nectr home page
  When Mike clicks on "home_tile_about_link"
  Then Mike should be redirected to "About" page
