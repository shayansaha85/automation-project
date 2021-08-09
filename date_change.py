def change_date_format(date):
    date = date.replace(",","")
    date_components = date.split()
    new_date = date_components[1] + "_" + date_components[0] + "_" + date_components[2]
    return new_date