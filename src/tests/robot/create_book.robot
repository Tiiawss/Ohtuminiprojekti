*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Form Page


*** Test Cases ***
Form Page Is Open
    Form Page Should Be Open

Last Book Is In All
    Set Input Field  author  pekka
    Set Input Field  title  titteli
    Set Input Field  year  1234
    Set Input Field  publisher  julkaisija
    Submit Form

    Home Page Should Be Open
    ${citekey}  Get Text  id:citekey

    Go To All Page
    ${author}  Get Text  id:${citekey}-author
    Should Be Equal  ${author}  pekka
    ${author}  Get Text  id:${citekey}-title
    Should Be Equal  ${author}  titteli
    ${author}  Get Text  id:${citekey}-year
    Should Be Equal  ${author}  1234
    ${author}  Get Text  id:${citekey}-publisher
    Should Be Equal  ${author}  julkaisija



Create Book With Correct Values
    Set Input Field  author  pekka
    Set Input Field  title  titteli
    Set Input Field  year  vuosi
    Set Input Field  publisher  julkaisija
    Submit Form
    Home Page Should Be Open

Show Last Citation In Home Page
    Set Input Field  author  matti
    Set Input Field  title  titteli
    Set Input Field  year  vuosi
    Set Input Field  publisher  julkaisija
    Submit Form
    Page Should Contain  matti
    Page Should Contain  titteli
    Page Should Contain  vuosi
    Page Should Contain  julkaisija

*** Keyword ***

Set Input Field
    [Arguments]  ${field_id}  ${text}
    Input Text  ${field_id}  ${text}

Submit Form
    Click Button  Luo viite