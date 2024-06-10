#!/bin/bash
# requires:
#   NodeJS
#     httypyac
#   Python and pip
#     junit2htmlreport (https://github.com/inorton/junit2html)

# npm install -g httpyac
# pip install junit2htmlreport

# use SCRIPT_DIR for all other locations so we can run from anywhere
SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
TIMESTAMP=$(date +'%Y/%m/%Y-%m-%d-%H-%M-%S')

ASSURANCE_FHIR_SRC_DIR=$(readlink -f $SCRIPT_DIR/fhir-service-prime/src/2024-06-10)
ASSURANCE_FHIR_RESULTS_DIR=$(readlink -f $SCRIPT_DIR/../../../../../public/assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/results)
TIMESTAMPPED_ASSURANCE_FHIR_RESULTS_DIR=$ASSURANCE_FHIR_RESULTS_DIR/$TIMESTAMP

mkdir -p $TIMESTAMPPED_ASSURANCE_FHIR_RESULTS_DIR

printf "NodeJS " && node --version
printf "httpyac " && httpyac --version

# needed by fhir-service.test.http
export HOST="${HOST:-https://synthetic.fhir.api.techbd.org}"
echo "HOST $HOST"

httpyac $ASSURANCE_FHIR_SRC_DIR/fhir-service.test.http --all > $TIMESTAMPPED_ASSURANCE_FHIR_RESULTS_DIR/regression-test-results.httpyac.txt
httpyac $ASSURANCE_FHIR_SRC_DIR/fhir-service.test.http --all --junit > $TIMESTAMPPED_ASSURANCE_FHIR_RESULTS_DIR/regression-test-results.httpyac.junit.xml
python -m junit2htmlreport $TIMESTAMPPED_ASSURANCE_FHIR_RESULTS_DIR/regression-test-results.httpyac.junit.xml $TIMESTAMPPED_ASSURANCE_FHIR_RESULTS_DIR/regression-test-results.httpyac.junit.xml.html

# make sure symlinks are relative (for Git)
# create a symlink to the ASSURANCE_FHIR_SRC_DIR so we know what we ran
cd $TIMESTAMPPED_ASSURANCE_FHIR_RESULTS_DIR
echo $(realpath -s --relative-to="$TIMESTAMPPED_ASSURANCE_FHIR_RESULTS_DIR" "$ASSURANCE_FHIR_SRC_DIR")
ln -s $(realpath -s --relative-to="$TIMESTAMPPED_ASSURANCE_FHIR_RESULTS_DIR" "$ASSURANCE_FHIR_SRC_DIR") src
echo $(ls -al src)

# create a symlink to the most recently created results so it's convenient to access
cd $ASSURANCE_FHIR_RESULTS_DIR
rm -f latest
ln -s $TIMESTAMP latest
echo $(ls -al latest)
