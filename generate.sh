#!/usr/bin/env sh

generate() {
    datamodel-codegen \
        --input "$1" \
        --input-file-type json \
        --class-name "$2" \
        --snake-case-field \
        --allow-population-by-field-name \
        --output "$3"
}

generate "customer.json" "BaseCustomer" "base_customer.py"
generate "donut.json" "BaseDonut" "base_donut.py"
