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

    # Only handle .zip files
    if zipped[-3:] != "zip":
        print(f"> {zipped} is not a zip file.")
        print()
        return False

    # Unzip assignment file
    try:
        with zipfile.ZipFile(zipped, 'r') as read:
            read.extractall(destination)
            print(f"> Unzipped {zipped}.")
    except:
        print("> Could not unzip assignment file.")

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

    # Remove redundant .txt files
    try:
        os.system("rm *.txt")
    except:
        # We should still continue the routine
        print("> Could not remove .txt files, or no .txt files was found.")

    # Keep track of how many files we can unzip.
    count = 0
    # Target is an integer determined by the number of .zip files in the destination directory.
    target = len([filename for filename in os.listdir() if filename[-3:] == "zip"])

    # For each zipped assignment in the destination directory
    for assignment in os.listdir():
        # Only handle .zip files
        if assignment[-3:] != "zip":
            print(f"> {assignment} is not a zip file.")
            continue

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
                count += 1
                print(f"> Unzipped {username}'s deliverable. ({count} / {target})")
        except:
            print("> Could not unzip student's zipped assignment.")
            continue

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
        "> Finished unzipping files!"
        if succeeded
        else "> An error occurred when trying to unzip files!"
    )
