def read_temperatures(filename):
    
    with open(filename) as f:    
        
        line = f.readline()

        list2 = []
        while line:

            month = int(line[0:5])
            day = int(line[14:17])
            year = int(line[28:33])
            average = float(line[40:47])


            list1 = [month,day,year,average]

            list2.append(list1)

            line = f.readline()

    return list2 

def delete_year(data, year):
   
    list1 = []
    index= 0
    length = len(data)

    while index < length:

        if data[index][2]!=year:
            list1.append(data[index])
    
        index = index + 1

    return list1 



def monthly_averages(data, year):
    
    listyear = []
    listaverage = []
    index = 0
    length = len(data)

    while index < length:

        if data[index][2]==year:
            listyear.append(data[index])

        index = index + 1
  
    index = 0
    length = len(listyear)
    b = listyear[length-1][0]
    
    for i in range(b):
        index = 0
        summa = 0
        count = 0
        while index < length:

            if i+1 == listyear[index][0]:

                if listyear[index][3]!=-99:

                    summa += listyear[index][3]
                    count +=1

            index +=1

        listaverage.append(summa/count)

    return listaverage 



def main():
    """
    The code given here is for you test your functions. When submitting, 
    make sure the code you leave under main() does not cause a syntax error.
    """
    istanbul_data = read_temperatures("ISTANBUL.txt")
    print(istanbul_data)
    ankara_data = read_temperatures("ANKARA.txt")
    print(ankara_data)
    
    print(delete_year(istanbul_data, 2020))
    print(delete_year(ankara_data, 2020))
    
    print(monthly_averages(istanbul_data, 2017))
    print(monthly_averages(ankara_data, 2017))
   



################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()
