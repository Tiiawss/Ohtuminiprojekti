*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Form Page


*** Test Cases ***
Form Page Is Open
    Form Book Page Should Be Open

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

Last Book Is In All
    Set Input Field  author  pekka
    Set Input Field  title  titteli
    Set Input Field  year  1234
    Set Input Field  publisher  julkaisija
    Submit Form

    Home Page Should Be Open
    ${citekey}  Get Text  id:citekey

    Go To All Page
    Element Should Contain  id:${citekey}-type  Book
    ${author}  Get Text  id:${citekey}-author
    Should Be Equal  ${author}  author: pekka
    ${author}  Get Text  id:${citekey}-title
    Should Be Equal  ${author}  title: titteli
    ${author}  Get Text  id:${citekey}-year
    Should Be Equal  ${author}  year: 1234
    ${author}  Get Text  id:${citekey}-publisher
    Should Be Equal  ${author}  publisher: julkaisija

Create Book With Missing Author
    Set Input Field  title  titteli
    Set Input Field  year  vuosi
    Set Input Field  publisher  julkaisija
    Submit Form
    Form Book Page Should Be Open

Select Article From Dropdown
    Select From List By Index  name:types  1
    List Selection Should Be  name:types  Article

Create Article With Required Values
    Select From List By Index  name:types  1
    Set Input Field  author  pekka
    Set Input Field  title  titteli
    Set Input Field  journal  journali
    Set Input Field  year  2922
    Submit Form
    Home Page Should Be Open
    ${citekey}  Get Text  id:citekey

    Go To All Page
    Page Should Contain  Article
    Element Should Contain  id:${citekey}-type  Article
    ${author}  Get Text  id:${citekey}-author
    Should Be Equal  ${author}  author: pekka
    ${author}  Get Text  id:${citekey}-title
    Should Be Equal  ${author}  title: titteli
    ${author}  Get Text  id:${citekey}-year
    Should Be Equal  ${author}  year: 2922
    ${author}  Get Text  id:${citekey}-journal
    Should Be Equal  ${author}  journal: journali
