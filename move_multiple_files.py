import os
import shutil


def main():
    # asks user for input with the folder path, destination folder path and the file name to look for
    src_dir = input("Enter the source folder path: ")
    dst_dir = input("Enter the destination folder path: ")
    target_filename = input("Enter the file name to look for: ")
    sorted_file_list = []

    # iterate through each of the files in the folder
    for filename in os.listdir(src_dir):
        if filename.startswith(target_filename) and\
             os.path.isfile(f"{src_dir}/{filename}"):
            sorted_file_list.append(filename)
            shutil.move(f"{src_dir}/{filename}", f"{dst_dir}/{filename}")
    return sorted(sorted_file_list)


if __name__ == '__main__':
    print(main())
