#!/usr/bin/env bash

# Checks if all RDFs are properly formatted, by formatting them and
# checking that the output is the same as the file in the repo.

{
if ! which xmllint; then
    echo "xmllint not installed. Installing it."
    sudo apt update --quiet --quiet
    sudo apt install libxml2-utils --quiet --yes
else
    echo "xmllint installed. Carry on."
fi

# Get the current directory with a lot of magic to handle a lot of corner cases.
THIS_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

shopt -s globstar # enable the ** construct
for rdf in $THIS_DIR/../**/*.rdf; do
    echo "Checking $rdf"
    # The <() construct put the output of a command in a file descriptor, allowing it to be used
    # by a command requiring files, like diff.
    # This says: if there is a difference betwwen the current file and the output of the format action,
    # then warn.
    if ! diff --brief <(xmllint --format $rdf) $rdf > /dev/null; then
        echo "At least $rdf is not properly formatted. Run scripts/indent.sh"
        exit 1
    fi
done

exit $?
}