*** Settings ***
Documentation  Basic Test Case to check the GET Request for Rest API
Library  RequestsLibrary

*** Variables ***
${Base_URL}  http://thetestingworldapi.com/


*** Test Cases ***
TC_001_Get_Request
    [Documentation]  First test case to check the Get Request
    [Setup]  log to console  **** Test Starts ****
    [Teardown]  log to console  **** Test Ends ****
    [Tags]  Smoke
    create session  Get_Student_Details  ${Base_URL}
    ${response} =  get request  Get_Student_Details  api/studentsDetails
    log to console  ${response.status_code}
    log to console  ${response.content}



