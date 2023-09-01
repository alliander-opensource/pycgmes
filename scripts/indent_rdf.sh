#!/usr/bin/env bash

# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

# Indent/format all rdfs in this repo.

{
if ! which xmllint; then
    echo "xmllint not installed. Installing it."
    sudo apt update
    sudo apt install libxml2-utils
else
    echo "xmllint installed. Carry on."
fi

# Get the current directory with a lot of magic to handle a lot of corner cases.
THIS_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

shopt -s globstar # enable the ** construct
for rdf in $THIS_DIR/../**/*.rdf; do
    echo "$rdf"
    # xmllint cannot update in place, so output in a temporary file and rename.
    xmllint --format $rdf --output ${rdf}.2
    mv ${rdf}.2 $rdf
done
exit $?
}