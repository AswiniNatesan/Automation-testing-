*** Settings ***
Library  SeleniumLibrary
Library    SeleniumLibrary

*** Variables ***
${link}     chrome
${URL}     https://www.facebook.com/

*** Test Cases ***
Facebook
     Open Browser    ${URL}    ${link}
     loginTest
     close browser

*** Keywords ***
loginTest
    input text    name:email    aswini@gmail.com
    input text    name:pass     aswini123
    click element    name:login



