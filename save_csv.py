def save_sheet(list_of_lines, name, folder):
    data = ""
    for lines in list_of_lines:
        data += lines + "\n"
    file = open(f"{folder}/{name}", "w")
    file.write(data)
    file.close()
    print(f"Saved in {name} file inside the directory : {folder}")