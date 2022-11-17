*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  jonne  jonne123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  jonne  jonne123
    Input New Command
    Input Credentials  jonne  jonne123
    Output Should Contain  User with username jonne already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  j  jonne123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  jonne  jonne1
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  jonne  jonnegabagoo
    Output Should Contain  Password should contain numbers

*** Keywords ***


Input New Command And Create User
    Input New Command
    Input Credentials  jonne  jonne123
    Run Application
