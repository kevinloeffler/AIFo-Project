#!/bin/sh
echo "This script installs the python dependencies for dialogflow"
tput setaf 7; echo "(No version NR means something went wrong)"; tput sgr0
echo ""

pip install google-api-core
pip install google-cloud-dialogflow

echo ""

CORE_VERSION=$(pip list | grep "google-api-core" | grep -E -o "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")
DIALOGFLOW_VERSION=$(pip list | grep "google-cloud-dialogflow" | grep -E -o "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")

echo "Installed google-api-core version: $CORE_VERSION"
echo "Installed dialogflow version: $DIALOGFLOW_VERSION"

if [[ ! $DIALOGFLOW_VERSION =~ 2\.[0-9]+\.[0-9]+ ]]; then
    tput setaf 3; printf "[WARN] "; tput sgr0
    echo "Wrong major Version of Dialogflow: Expected '2.x.x'"
    echo "       Use 'pip install google-cloud-dialogflow==2.9.1'"
fi
