import sys
import zipfile
import os

def unzip(argv):
    # argv should only process 2 arguments
    if len(argv) != 2:
        print("> Invalid input. Please use the following format:")
        print(f'$ python3 unzip.py zipped-filename destination-directory')
        return False

    # Get command line arguments
    zipped = argv[0]
    destination = argv[1]

    # Unzip file
    try:
        with zipfile.ZipFile(zipped, 'r') as read:
            read.extractall(destination)
    except:
        return False

    # Remove zipped assignment file
    os.system(f"rm -rf *.zip")

    # Navigate to the destination directory
    os.chdir(destination)

    # Remove redundant .txt files
    os.system("rm *.txt")

    # For each zipped assignment in the destination directory
    for assignment in os.listdir(zipped[0:len(zipped) - 4]):
        # Check if the file is actually a zipped folder
        if assignment[len(assignment)-3:] != "zip":
            continue

        # Get student username from auto-generated filename from BlackBoard
        username = assignment.split("_")[1]

        # Unzip student file
        try:
            # Find the path to the assignment
            assignment_path = zipped[0:len(zipped) - 4] + "/" + assignment
            
            with zipfile.ZipFile(assignment_path, 'r') as read:
                read.extractall(username)
        except:
            return False

    # Remove zipped assignment file
    os.system(f"rm -rf *.zip")

    return True


if __name__ == '__main__':
    # Syntax: python3 unzip.py zipped destination
    succeeded = unzip(sys.argv[1:])

    print(
        "> Successfully unzipped file!"
        if succeeded
        else "> An error occurred when trying to unzip file!"
    )
