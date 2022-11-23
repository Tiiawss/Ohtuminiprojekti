*** Settings ***
Library  SeleniumLibrary
Library  ../../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.1 seconds
${HOME URL}  http://${SERVER}
${FORM URL}  http://${SERVER}/form
${ALL URL}  http://${SERVER}/all

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  Etusivu

Form Page Should Be Open
    Title Should Be  Lisää Viite

All Page Should Be Open
    Title Should Be  Kaikki Viitteet

Go To Home Page
    Go To  ${HOME URL}

Go To Form Page
    Go To  ${FORM URL}

Go To All Page
    Go To  ${ALL URL}