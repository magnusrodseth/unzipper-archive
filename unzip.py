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

    # Unzip assignment file
    try:
        with zipfile.ZipFile(zipped, 'r') as read:
            read.extractall(destination)
    except:
        print("> Could not unzip assignment file.")
        return False

    # Remove zipped assignment file
    try:
        os.system(f"rm -rf *.zip")
    except:
        # We should still continue the routine
        print("> Could not remove zipped assignment file.")

    # Navigate to the destination directory
    try:
        os.chdir(destination)
    except:
        print("> Could not navigate to the destination directory.")
        return False

    # Remove redundant .txt files
    try:
        os.system("rm *.txt")
    except:
        # We should still continue the routine
        print("> Could not remove .txt files.")

    # For each zipped assignment in the destination directory
    for assignment in os.listdir():
        username = ""

        # Get student username from auto-generated filename from BlackBoard
        try:
            username = assignment.split("_")[1]
        except:
            # We should still continue the routine
            print("> Could not simplify student's directory name.")

        # Unzip student file
        try:
            with zipfile.ZipFile(assignment, 'r') as read:
                read.extractall(username)
        except:
            print("> Could not unzip student's zipped assignment.")
            return False

    # Remove zipped assignment file
    try:
        os.system(f"rm -rf *.zip")
    except:
        # We should still continue the routine
        print("> Could not remove zipped assignment file.")

    return True


if __name__ == '__main__':
    # Syntax: python3 unzip.py zipped destination
    succeeded = unzip(sys.argv[1:])

    print(
        "> Successfully unzipped file!"
        if succeeded
        else "> An error occurred when trying to unzip file!"
    )
