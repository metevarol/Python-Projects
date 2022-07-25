import csv

def read_iris(filename):

    with open(filename, 'r') as file:
        csv_file = csv.DictReader(file)

        list1 = []
        list2 = []

        for column in csv_file:
            list1.append(float(column['sepal_length']))
            list1.append(float(column['sepal_width']))
            list1.append(float(column['petal_length']))
            list1.append(float(column['petal_width']))
            list1.append(column['variety'])

            list2.append(list1)

            list1 = []
      
    return list2 


def avg_versicolor(lst):
    
    index = 0
    sum1 = 0
    sum2 = 0
    versicount = 0
    length = len(lst)

    while index < length:

        if lst[index][4]=="Versicolor":
            sum1 = sum1 + lst[index][0]
            sum2 = sum2 + lst[index][2]
            versicount +=1

        index +=1

    average1 = sum1 / versicount
    average2 = sum2 / versicount

    list1 = "{'Versicolor': ("+str(average1)+", "+str(average2)+")}"
            
    return list1 # change me


def main():
    """
    The code given here is for you test your functions. When submitting, 
    make sure the code you leave under main() does not cause a syntax error.
    """
    
    my_list = read_iris('iris_data.csv')
    print(my_list)
    avg = avg_versicolor(my_list)
    print(avg)
    
    

################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()
