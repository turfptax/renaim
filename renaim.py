import os

def rename_files():
    path = os.getcwd()
    file_list = os.listdir(path)

    for file in file_list:
        if file.endswith(".jpg"):
            split_name = file.split('-')
            if len(split_name) > 1:
                number = split_name[0]
                suffix = split_name[1].split('.')[0]
                new_name = f'{suffix}-{number}.jpg'
                os.rename(file, new_name)
                print(f"Renamed: {file} -> {new_name}")

if __name__ == "__main__":
    rename_files()
