Feature: login   
  
Scenario: login in the   
  Given I go to "http://121.36.8.180/login"
     When I set the id "modal_uname_input" with "vip000000081"
     And I set the id "modal_upass_input" with "123456"  
     And I click id "startLogin" with baidu once
     Then I close browser
