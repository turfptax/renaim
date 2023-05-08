import os

def rename_files():
    path = os.getcwd()
    file_list = os.listdir(path)

    # Initialize a counter for the new sequence
    count = 1

    # Sort the file_list to ensure correct ordering
    file_list.sort()

    for file in file_list:
        if file.endswith(".jpg"):
            split_name = file.split('-')
            if len(split_name) > 1:
                # Replace the original number with the counter value
                number = count
                count += 1
                suffix = split_name[1].split('.')[0]
                new_name = f'{suffix}-{number}.jpg'
                os.rename(file, new_name)
                print(f"Renamed: {file} -> {new_name}")

if __name__ == "__main__":
    rename_files()
