#!/bin/bash

set -e

pip3 install checkov
checkov -d . --external-checks-dir ../custom-checks --skip-framework terraform_json
