#Program 1 --> to read file

# file = open('demo.txt', 'r')
# print (file.read())

#for each in file:
    #print(each)


#Program -->2)Write a function to count the number of lines from a text file which is not starting with an alphabet "T".
def line_count():
    file = open("demo.txt","r")
    count=0
    for line in file:
        if line[0] not in 'T':
            count+= 1
    file.close()
    print("No of lines not starting with 'T'=",count)

line_count()

#Program 3
def occurrence():
    file = open(r"E:\VIT\python\Lab assigment\assigment\MyCountry.txt","r")
    a= file.read().count("the")
    print('\noccurrence of the word "the"=',a)
    file.close()
occurrence()

#Program 4
def write():
    file= open(r"E:\VIT\python\Lab assigment\assigment\MyCountry.txt","a")
    a = input("\nEnter : ")
    file.write(a)
    file= open(r"E:\VIT\python\Lab assigment\assigment\MyCountry.txt","r")
    print(file.read())
    file.close()
write()