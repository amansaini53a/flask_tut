*** Settings ***
Documentation    Suite description
Library  RequestsLibrary
Library  JSONLibrary
Library  Collecti
ons

*** Variables ***
${Base_url}=  http://reqres.in

*** Test Cases ***
Validate Get Request with Param
    create session  Get_param  ${Base_url}
    &{param}=  create dictionary  page=2
    ${response}=  get request  Get_param  /api/users  params=${param}
    ${statuscode}=  convert to string  ${response.status_code}
    should be equal  ${statuscode}  200
#    log  ${response.content}
    ${jsonresponse}=  to json  ${response.content}
    @{name_list}=  get value from jsonrt  ${jsonresponse}  data[0].first_name