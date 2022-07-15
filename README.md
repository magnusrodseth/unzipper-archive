# Unzipper 📂

## Description ✏️

This repository was developed out of frustration related to the tedious process of downloading and grading student deliverables.

Before following the **Running the application** below, make sure you place the zipped file in the `unzipper` directory.

## Directory Structure 📂

After running the script, the directories `deliverables` and `feedback` are generated. The files contained in these folders are named after each student's username. Use the `.txt` files in the `feedback` directory to easily write student feedback. When you are done giving the feedback, simply `Copy + Paste` the contents of the `.txt` file to the comment section in BlackBoard.

## Validate files with W3 Validator 🔍

Do you want to "automagically" validate all `.html`, `.css` and `.js` files for an assignment using W3 Validator? Simply use the `validate.sh` script to recursively navigate through all subdirectories for an assignment and `POST` the relevant files. The result is stored as a `.json` file in each student's deliverable directory.

**`Terminal`**

```sh
# Execute the script from the unzipper directory and simply name the assignment directory
sh validate.sh assignment-1
```

**`about_html.json`**

```json
// An example of a result from W3 Validator
{
  "messages": [
    {
      "type": "error",
      "lastLine": 16,
      "lastColumn": 82,
      "firstColumn": 9,
      "message": "Bad value “100px” for attribute “width” on element “img”: Expected a digit but saw “p” instead.",
      "extract": " \n        <img src=\"attachments/me.jpg\" alt=\"My image\" width = \"100px\" height=\"100\">\n     ",
      "hiliteStart": 10,
      "hiliteLength": 74
    }
  ]
}
```

## Developer Information 🙋🏼‍♂️

Developed by Magnus Rødseth.

## Running the application ✅

```sh
cd unzipper

# Unzip and structure files
python3 unzip.py zipped_filename destination_directory

# Validate all students' .html, .css and .js files
sh validate.sh assignment_directory
```
