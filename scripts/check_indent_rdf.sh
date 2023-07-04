#!/usr/bin/env bash

# Checks if all RDFs are properly formatted, by formatting them and
# checking that the output is the same as the file in the repo.

if ! which xmllint; then
    echo "xmllint not installed. Installing it."
    sudo apt update
    sudo apt install libxml2-utils
else
    echo "xmllint installed. Carry on."
fi

shopt -s globstar # enable the ** construct
for rdf in  **/*.rdf; do
    if ! diff --brief <(xmllint  $rdf) $rdf; then
        echo "At least $rdf is not properly formatted. Run scripts/indent.sh"
        exit 1
    fi
done