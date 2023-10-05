import os


# Function to rename multiple files
def main():
    # path of the folder containing the raw files
    folder = input("Enter the folder path: ")
    rename_prefix = input("Enter the rename prefix:")

    # iterate through each of the files in the folder
    for count, filename in enumerate(os.listdir(folder)):
        # gets the extension of the file
        _, ext = os.path.splitext(filename)
        dst = f"{rename_prefix}-{count}.{ext}"
        src = f"{folder}/{filename}"
        dst = f"{folder}/{dst}"

        # rename() function will rename all the files
        os.rename(src, dst)


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
