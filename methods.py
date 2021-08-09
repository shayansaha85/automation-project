import time
import date_change as dc
import save_csv as sc
import download_image as di

def launch_driver(driver, url):
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    if len(driver.find_elements_by_id("onetrust-accept-btn-handler")):
        driver.find_element_by_id("onetrust-accept-btn-handler").click()

def functionality_1(driver,products,tricentis_tosca,title_1, description_1, title_2, description_2, title_3, description_3, title_4, description_4, title_5, description_5, title_6, description_6, title_7, description_7, title_8, description_8, title_9, description_9, title_10, description_10, title_11, description_11):
    time.sleep(5)
    driver.find_element_by_xpath(products).click()
    time.sleep(3)
    driver.find_element_by_xpath(tricentis_tosca).click()
    time.sleep(10)
    title_1 = driver.find_element_by_xpath(title_1).text
    title_2 = driver.find_element_by_xpath(title_2).text
    title_3 = driver.find_element_by_xpath(title_3).text
    title_4 = driver.find_element_by_xpath(title_4).text
    title_5 = driver.find_element_by_xpath(title_5).text
    title_6 = driver.find_element_by_xpath(title_6).text
    title_7 = driver.find_element_by_xpath(title_7).text
    title_8 = driver.find_element_by_xpath(title_8).text
    title_9 = driver.find_element_by_xpath(title_9).text
    title_10 = driver.find_element_by_xpath(title_10).text
    title_11 = driver.find_element_by_xpath(title_11).text
    description_1 =  driver.find_element_by_xpath(description_1).text
    description_2 =  driver.find_element_by_xpath(description_2).text
    description_3 =  driver.find_element_by_xpath(description_3).text
    description_4 =  driver.find_element_by_xpath(description_4).text
    description_5 =  driver.find_element_by_xpath(description_5).text
    description_6 =  driver.find_element_by_xpath(description_6).text
    description_7 =  driver.find_element_by_xpath(description_7).text
    description_8 =  driver.find_element_by_xpath(description_8).text
    description_9 =  driver.find_element_by_xpath(description_9).text
    description_10 =  driver.find_element_by_xpath(description_10).text
    description_11 =  driver.find_element_by_xpath(description_11).text
    
    l = []
    l.append("Titles","Descriptions")
    l.append(title_1,description_1)
    l.append(title_2,description_2)
    l.append(title_3,description_3)
    l.append(title_4,description_4)
    l.append(title_5,description_5)
    l.append(title_6,description_6)
    l.append(title_7,description_7)
    l.append(title_8,description_8)
    l.append(title_9,description_9)
    l.append(title_10,description_10)
    l.append(title_11,description_11)

    s = ""
    for x in l:
        s = s+x+"\n"
    f = open("spreadsheets/capabilities.csv", "w")
    f.write(s)
    f.close()

def functionality_2(driver,why_tricentis,newsroom,date_1,headline_1, date_2,headline_2, date_3,headline_3):
    driver.maximize_window()
    time.sleep(5)
    driver.find_element_by_xpath(why_tricentis).click()
    time.sleep(3)
    driver.find_element_by_xpath(newsroom).click()
    time.sleep(3)
    date_1 = dc.change_date_format(driver.find_element_by_xpath(date_1).text)
    date_2 = dc.change_date_format(driver.find_element_by_xpath(date_2).text)
    date_3 = dc.change_date_format(driver.find_element_by_xpath(date_3).text)
    headline_1 = driver.find_element_by_xpath(headline_1).text    
    headline_2 = driver.find_element_by_xpath(headline_2).text 
    headline_3 = driver.find_element_by_xpath(headline_3).text
    data = []
    data.append("Date,Headline")
    data.append(f"{date_1},{headline_1}")
    data.append(f"{date_2},{headline_2}")
    data.append(f"{date_3},{headline_3}")
    s = ""
    for x in data:
        s = s+x+"\n"
    f = open("spreadsheets/latest_press_releases.csv", "w")
    f.write(s)
    f.close()
    print("Saved in latest_press_releases.csv file inside the directory : spreadsheets")

def functionality_3(driver,url_customers,url_awards,mediacontact_name,mediacontact_email,client1, client2, client3, client4, client5, client6, client7, client8, client9, client10, client11, client12):
    clients= [client1, client2, client3, client4, client5, client6, client7, client8, client9, client10, client11, client12]
    driver.get(url_customers)
    driver.implicitly_wait(10)
    if len(driver.find_elements_by_id("onetrust-accept-btn-handler")):
        driver.find_element_by_id("onetrust-accept-btn-handler").click()
    i=1
    for x in clients:
        di.save_logo(driver,x,f'client{i}.png',"top_clients")
        i=i+1
    driver.get(url_awards)
    driver.implicitly_wait(10)
    if len(driver.find_elements_by_id("onetrust-accept-btn-handler")):
        driver.find_element_by_id("onetrust-accept-btn-handler").click()
    media_contact_name = driver.find_element_by_xpath(mediacontact_name).text
    media_contact_email = driver.find_element_by_xpath(mediacontact_email).text
    s = ""
    s = media_contact_name + "\n" + media_contact_email
    file = open("notes/media_contact_tricentis.md", "w")
    file.write(s)
    file.close()
    print("Saved in media_contact_tricentis.md file in the directory : notes")


def functionality_4(driver,services,consulting_services,title_1_bc,description_1_bc,title_2_bc,description_2_bc,title_3_bc,description_3_bc,title_1_em,description_1_em,title_2_em,description_2_em,title_3_em,description_3_em):
    time.sleep(5)
    driver.find_element_by_xpath(services).click()
    time.sleep(3)
    driver.find_element_by_xpath(consulting_services).click()
    time.sleep(3)
    title_1_bc = driver.find_element_by_xpath(title_1_bc).text
    title_2_bc = driver.find_element_by_xpath(title_2_bc).text
    title_3_bc = driver.find_element_by_xpath(title_3_bc).text
    print(title_2_bc)
    description_1_bc = driver.find_element_by_xpath(description_1_bc).text
    description_2_bc = driver.find_element_by_xpath(description_2_bc).text
    description_3_bc = driver.find_element_by_xpath(description_3_bc).text
    print(description_3_bc)
    title_1_em = driver.find_element_by_xpath(title_1_em).text
    title_2_em = driver.find_element_by_xpath(title_2_em).text
    title_3_em = driver.find_element_by_xpath(title_3_em).text
    print(title_1_em)
    description_1_em = driver.find_element_by_xpath(description_1_em).text
    description_2_em = driver.find_element_by_xpath(description_2_em).text
    description_3_em = driver.find_element_by_xpath(description_3_em).text
    print(description_2_em)
    bc = []
    bc.append("Title,Description")
    bc.append(f"{title_1_bc},{description_1_bc}")
    bc.append(f"{title_2_bc},{description_2_bc}")
    bc.append(f"{title_3_bc},{description_3_bc}")
    a = ""
    for x in bc:
        a= a+x+"\n"
    b = open("spreadsheets/consulting_pros_tricentis.csv","w")
    b.write(a)
    b.close()
    em = []
    em.append("Title,Description")
    em.append(f"{title_1_em},{description_1_em}")
    em.append(f"{title_2_em},{description_2_em}")
    em.append(f"{title_3_em},{description_3_em}")
    m = ""
    for x in em:
        m = m+x+"\n"
    n = open("spreadsheets/engagement_models_tricentis.csv","w")
    n.write(m)
    n.close()
    print(f"Saved in engagement_models_tricentis.csv file inside the directory : spreadsheets")

def functionality_5(driver,url_knowledge,trouble_shooting,num_data1,num_data2,num_data3,num_data4,num_data5,num_data6,num_data7,num_data8,num_data9,num_data10,product_data2,product_data4,product_data5,product_data6,product_data7,product_data8,product_data9,title_data1,title_data2,title_data3,title_data4,title_data5,title_data6,title_data7,title_data8,title_data9,title_data10,category_data1,category_data2,category_data3,category_data4,category_data5,category_data6,category_data7,category_data8,category_data9,category_data10,state_data1,state_data2,state_data3,state_data4,state_data5,state_data6,state_data7,state_data8,state_data9,state_data10,created_data1,created_data2,created_data3,created_data4,created_data5,created_data6,created_data7,created_data8,created_data9,created_data10,updated_data1,updated_data2,updated_data3,updated_data4,updated_data5,updated_data6,updated_data7,updated_data8,updated_data9,updated_data10):
    driver.get(url_knowledge)
    driver.implicitly_wait(10)
    if len(driver.find_elements_by_id("onetrust-accept-btn-handler")):
        driver.find_element_by_id("onetrust-accept-btn-handler").click()
    time.sleep(5)
    driver.find_element_by_xpath(trouble_shooting).click()
    time.sleep(5)
    num_data1 = driver.find_element_by_xpath(num_data1).text
    num_data2 = driver.find_element_by_xpath(num_data2).text
    num_data3 = driver.find_element_by_xpath(num_data3).text
    num_data4 = driver.find_element_by_xpath(num_data4).text
    num_data5 = driver.find_element_by_xpath(num_data5).text
    num_data6 = driver.find_element_by_xpath(num_data6).text
    num_data7 = driver.find_element_by_xpath(num_data7).text
    num_data8 = driver.find_element_by_xpath(num_data8).text
    num_data9 = driver.find_element_by_xpath(num_data9).text
    num_data10 = driver.find_element_by_xpath(num_data10).text
    product_data1 = ""
    product_data2 = driver.find_element_by_xpath(product_data2).text
    product_data3 = ""
    product_data4 = driver.find_element_by_xpath(product_data4).text
    product_data5 = driver.find_element_by_xpath(product_data5).text
    product_data6 = driver.find_element_by_xpath(product_data6).text
    product_data7 = driver.find_element_by_xpath(product_data7).text
    product_data8 = driver.find_element_by_xpath(product_data8).text
    product_data9 = driver.find_element_by_xpath(product_data9).text
    product_data10 = ""
    title_data1 = driver.find_element_by_xpath(title_data1).text
    title_data2 = driver.find_element_by_xpath(title_data2).text
    title_data3 = driver.find_element_by_xpath(title_data3).text
    title_data4 = driver.find_element_by_xpath(title_data4).text
    title_data5 = driver.find_element_by_xpath(title_data5).text
    title_data6 = driver.find_element_by_xpath(title_data6).text
    title_data7 = driver.find_element_by_xpath(title_data7).text
    title_data8 = driver.find_element_by_xpath(title_data8).text
    title_data9 = driver.find_element_by_xpath(title_data9).text
    title_data10 = driver.find_element_by_xpath(title_data10).text
    category_data1 = driver.find_element_by_xpath(category_data1).text
    category_data2 = driver.find_element_by_xpath(category_data2).text
    category_data3 = driver.find_element_by_xpath(category_data3).text
    category_data4 = driver.find_element_by_xpath(category_data4).text
    category_data5 = driver.find_element_by_xpath(category_data5).text
    category_data6 = driver.find_element_by_xpath(category_data6).text
    category_data7 = driver.find_element_by_xpath(category_data7).text
    category_data8 = driver.find_element_by_xpath(category_data8).text
    category_data9 = driver.find_element_by_xpath(category_data9).text
    category_data10 = driver.find_element_by_xpath(category_data10).text
    state_data1 = driver.find_element_by_xpath(state_data1).text
    state_data2 = driver.find_element_by_xpath(state_data2).text
    state_data3 = driver.find_element_by_xpath(state_data3).text
    state_data4 = driver.find_element_by_xpath(state_data4).text
    state_data5 = driver.find_element_by_xpath(state_data5).text
    state_data6 = driver.find_element_by_xpath(state_data6).text
    state_data7 = driver.find_element_by_xpath(state_data7).text
    state_data8 = driver.find_element_by_xpath(state_data8).text
    state_data9 = driver.find_element_by_xpath(state_data9).text
    state_data10 = driver.find_element_by_xpath(state_data10).text
    created_data1 = driver.find_element_by_xpath(created_data1).text
    created_data2 = driver.find_element_by_xpath(created_data2).text
    created_data3 = driver.find_element_by_xpath(created_data3).text
    created_data4 = driver.find_element_by_xpath(created_data4).text
    created_data5 = driver.find_element_by_xpath(created_data5).text
    created_data6 = driver.find_element_by_xpath(created_data6).text
    created_data7 = driver.find_element_by_xpath(created_data7).text
    created_data8 = driver.find_element_by_xpath(created_data8).text
    created_data9 = driver.find_element_by_xpath(created_data9).text
    created_data10 = driver.find_element_by_xpath(created_data10).text
    updated_data1 = driver.find_element_by_xpath(updated_data1).text
    updated_data2 = driver.find_element_by_xpath(updated_data2).text
    updated_data3 = driver.find_element_by_xpath(updated_data3).text
    updated_data4 = driver.find_element_by_xpath(updated_data4).text
    updated_data5 = driver.find_element_by_xpath(updated_data5).text
    updated_data6 = driver.find_element_by_xpath(updated_data6).text
    updated_data7 = driver.find_element_by_xpath(updated_data7).text
    updated_data8 = driver.find_element_by_xpath(updated_data8).text
    updated_data9 = driver.find_element_by_xpath(updated_data9).text
    updated_data10 = driver.find_element_by_xpath(updated_data10).text
    list_for_csv = []
    list_for_csv.append("Number,Product,Title,Category,State,Created,Updated")
    list_for_csv.append(num_data1 + "," + product_data1 + "," + title_data1 + "," + category_data1 + "," + state_data1 + "," + created_data1 + "," + updated_data1)
    list_for_csv.append(num_data2 + "," + product_data2 + "," + title_data2 + "," + category_data2 + "," + state_data2 + "," + created_data2 + "," + updated_data2)
    list_for_csv.append(num_data3 + "," + product_data3 + "," + title_data3 + "," + category_data3 + "," + state_data3 + "," + created_data3 + "," + updated_data3)
    list_for_csv.append(num_data4 + "," + product_data4 + "," + title_data4 + "," + category_data4 + "," + state_data4 + "," + created_data4 + "," + updated_data4)
    list_for_csv.append(num_data5 + "," + product_data5 + "," + title_data5 + "," + category_data5 + "," + state_data5 + "," + created_data5 + "," + updated_data5)
    list_for_csv.append(num_data6 + "," + product_data6 + "," + title_data6 + "," + category_data6 + "," + state_data6 + "," + created_data6 + "," + updated_data6)
    list_for_csv.append(num_data7 + "," + product_data7 + "," + title_data7 + "," + category_data7 + "," + state_data7 + "," + created_data7 + "," + updated_data7)
    list_for_csv.append(num_data8 + "," + product_data8 + "," + title_data8 + "," + category_data8 + "," + state_data8 + "," + created_data8 + "," + updated_data8)
    list_for_csv.append(num_data9 + "," + product_data9 + "," + title_data9 + "," + category_data9 + "," + state_data9 + "," + created_data9 + "," + updated_data9)
    list_for_csv.append(num_data10 + "," + product_data10 + "," + title_data10 + "," + category_data10 + "," + state_data10 + "," + created_data10 + "," + updated_data10)
    sc.save_sheet(list_for_csv, "troubleshoot.csv", "spreadsheets")
    
def quit_driver(driver):
    driver.quit()