# Created by ashva at 1/15/2025
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can go to settings and edit the personal information
    given Open sign in page
    when enter_email
    and enter password
    and click on signin button
    and Click on settings option
    and Click on Edit profile option
    and Enter English in the language input field
    then Check language English is present in the input field
    and Click on save changes button
    and Click on close button