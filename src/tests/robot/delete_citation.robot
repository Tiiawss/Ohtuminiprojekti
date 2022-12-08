*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Delete All Citations And Go To Form Page
Test Teardown  Delete All Citations

*** Test Cases ***
Form Page Is Open
    Form Book Page Should Be Open

Delete Newest Citation
    Set Input Field  author  pekka
    Set Input Field  title  titteli
    Set Input Field  year  vuosi
    Set Input Field  publisher  julkaisija
    Set Input Field  tagit  tagii
    Submit Form

    ${citekey}  Get Text  id:citekey
    Go To All Page
    Click Button  remove-${citekey}

    Go To All Page
    Page Should Not Contain  ${citekey}

Delete Only Certain Citation
    Set Input Field  author  pekka
    Set Input Field  title  titteli
    Set Input Field  year  9000
    Set Input Field  publisher  julkaisija
    Set Input Field  tagit  tagii
    Submit Form
    ${citekey_to_be_deleted}  Get Text  id:citekey
    Go To Form Page
    Set Input Field  author  sami
    Set Input Field  title  titteli
    Set Input Field  year  2002
    Set Input Field  publisher  julkaisija
    Set Input Field  tagit  tagii
    Submit Form

    ${citekey}  Get Text  id:citekey
    Go To All Page
    Click Button  remove-${citekey_to_be_deleted}
    Go To All Page
    Page Should Not Contain  ${citekey_to_be_deleted}
    Page Should Contain  ${citekey}