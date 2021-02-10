# ATP JSON Output Reader

Reads output from the ATP prototype and generates csv file based on select values.

Current fields populated:

* VodRequest_ID 
* name
* ATPScore
* group
* amount
* log value
* date
* description squeezed and trimmed
* description original

## Layout

Main processing occurs in parse_python.py

script-csv.py primarily facilitates output formatting

## Usage

Run script-csv.py

Choose input. Note that input file must be in .jjson format, not .json

Output will automatically generate