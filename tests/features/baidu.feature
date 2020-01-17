Feature: login   
  
Scenario: login in the   
  Given I go to "www.baidu.com"
     When I set the id "modal_uname_input" with "1"
     And I set the id "modal_upass_input" with "11"  
     And I click id "startLogin" with baidu once
     Then I close browser
