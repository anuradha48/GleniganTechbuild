Feature: OrangeHrm Logo
  Scenario: Logo presence on orange HRM
    Given Launch chrome browser
    When Open orange HRM
    Then Verify that logo present on page
    Then close browser