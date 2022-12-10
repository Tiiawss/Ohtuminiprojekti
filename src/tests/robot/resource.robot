*** Settings ***
Library  SeleniumLibrary
Library  ../../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0.0 seconds
${HOME URL}  http://${SERVER}
${FORM URL}  http://${SERVER}/form
${ALL URL}  http://${SERVER}/all
${BIBTEX URL}  http://${SERVER}/bibtex
${DELETE_ALL URL}  http://${SERVER}/bibtex

*** Keywords ***
Open And Configure Browser
    Use Test Db
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  Bibtex sovellus
Form Book Page Should Be Open
    Title Should Be  Bibtex sovellus - Lisää viite

All Page Should Be Open
    Title Should Be  Bibtex sovellus - Kaikki viitteet

Bibtex Page Should Be Open
    Title Should Be  Bibtex

Go To Bibtex Page
    Go To  ${BIBTEX URL}

Go To Home Page
    Go To  ${HOME URL}

Go To Form Page
    Go To  ${FORM URL}

Go To All Page
    Go To  ${ALL URL}

Set Input Field
    [Arguments]  ${field_id}  ${text}
    Input Text  ${field_id}  ${text}

Submit Form
    Click Button  Luo viite

Delete All Citations And Go To Form Page
    Delete All Citations
    Go To  ${FORM URL}
