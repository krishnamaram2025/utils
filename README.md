Project Title
--------------
Cloud Stones Platform

# Pre-Requisites
The below commands to set environment variables in Windows machine

vi setenv.cmd
set AZURE_SUBSCRIPTION_ID=""

set AZURE_TENANT_ID=""

set AZURE_CLIENT_ID=""

set AZURE_CLIENT_SECRET=""


az login

export MSYS_NO_PATHCONV=1
az ad sp create-for-rbac --name <myserviceprincipal> --role Contributor

https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd



Execution Flow
----------------
$git clone https://github.com/csp2022/CSP.git

$cd CSP/aws

$python3 vpc.py <accesskeyid> <secretaccesskey>
