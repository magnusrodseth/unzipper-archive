#!/usr/bin/env bash

validate() {
  echo "> Make sure your input is on the following format:"
  echo "$ sh validate.sh path_to_html_file target_directory"
  echo

  filename=$1
  target_directory=$2

  echo "> Posting file to W3 Validator"
  echo

  curl -H "Content-Type: text/html; charset=utf-8" \
    --data-binary "$filename" \
    https://validator.w3.org/nu/?out=json >"$target_directory"/validate.json

  echo
  echo "> Wrote response to validate.json"
}

validate "$1" "$2"
