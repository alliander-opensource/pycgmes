#!/usr/bin/env bash

if ! which xmllint; then
    echo "xmllint not installed. Installing it."
    sudo apt update
    sudo apt install libxml2-utils
else
    echo "xmllint installed. Carry on."
fi

shopt -s globstar # enable the ** construct
for rdf in  **/*.rdf; do
    echo "$rdf"
    # xmllint cannot update in place, so output in a temporary file and rename. 
    xmllint --format $rdf --output ${rdf}.2
    mv ${rdf}.2 $rdf
done
