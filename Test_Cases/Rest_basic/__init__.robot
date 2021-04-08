*** Settings ***

Documentation    Init File to Run all test case in Rest_basic suite
Suite Setup  Before Rest_basic Test Suite
Suite Teardown  After Rest_basic Test Suite

*** Keywords ***
Before Rest_basic Test Suite
    [Documentation]  Before Rest_basic Suite
    log to console  Before Rest_basic Suite

After Rest_basic Test Suite
    [Documentation]  After Rest_basic Suite
    log to console  After Rest_basic Suite