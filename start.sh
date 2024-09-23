#!/bin/bash

# Variables passed from command line arguments
SCAN_URL=$1
JENKINS_SERVER_PATH=$2
PROJ=$3

echo """
SCAN_URL=$SCAN_URL
JENKINS_SERVER_PATH=$JENKINS_SERVER_PATH
PROJ=$PROJ
"""  > .env


if [ -z "$1" ]; then
  echo "No argument provided. Please provide 'test' as an argument."
  exit 1
fi

# Check if the argument is 'test'
if [ "$1" == "projname" ]; then
  echo """
SCAN_URL="URL"
JENKINS_SERVER_PATH="/var/lib/jenkins/zap-reports/filnename"
PROJ="PROJ_NAME"
"""  > .env
 python3 vapt-scan.py
