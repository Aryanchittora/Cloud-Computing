def visitors():
    count = open('C:\\Users\\Asus\\Desktop\\Cloud Computing\\Code\\count.txt', 'r')
    no = int(count.read())
    count.close()

    no = no + 1
    open2 = open('count.txt', 'w')
    open2.write(str(no))
    open2.close()

    print('Total Visitors -', no)

def covid_data():
    country = input('Enter Country Name - ')
    data = 'https://covid-api-262.herokuapp.com/?country='+country
    
    print(data)

visitors()
covid_data()