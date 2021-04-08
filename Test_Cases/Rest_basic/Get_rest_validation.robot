#1. Get Request to fetch specific student details.
#2. Pick and save  RESPONSE.
#3. Validate status code.
#4. Validate Response content.
#  josnformatter.com, josnpath.com
*** Settings ***
Documentation  Test case to validate the Data from API
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections

*** Variables ***
${Base_url}  http://thetestingworldapi.com/
${Student_id}  28
*** Test Cases ***
TC_001_Get_Validate
    [Tags]    DEBUG
    [Documentation]  First test case
    [Setup]  log to console  **** Test Case Starts ****
    [Teardown]  log to console  **** Test Case Stops ****
    create session  Fetch_data  ${Base_url}
    ${Response}=  get request   Fetch_data  api/studentsDetails/${Student_id}
    ${Actual_code}=  convert to string  ${Response.status_code}
    should be equal  ${Actual_code}  200
    ${json_res}=  to json  ${Response.content}

    @{first_name_list}=  get value from json  ${json_res}  data.first_name
    log to console  ${Response.content}
#    ${first_name}=  get from list  ${first_name_list}  0
#    log to console  ${first_name}
#    should be equal  ${first_name}  aman saini