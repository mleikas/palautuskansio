*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kall
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  k1
    Set Password Confirmation  k1
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  kalle4321
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  kalle1
    Set Password  kalle12345
    Set Password Confirmation  kalle12345
    Submit Credentials
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  kalle1
    Set Password  kalle12345
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  kalle4321
    Submit Credentials
    Click Link  Login
    Set Username  kalle
    Set Password  kalle1234
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Submit Credentials
    Click Button  Register

Submit Credentials Login
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
