import docx
import csv
import numpy as np
import pandas as pd


index_pos_list = []

def get_index_positions_2(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    for i in range(len(list_of_elems)):
        if list_of_elems[i] == element:
            index_pos_list.append(i)
    return index_pos_list


def compare (userInput, dataArray):
    #compare and count the number of standards in the config Database array
    #finding the standard by comparing it to the array 
    n = 0 
    count = 0 
    standard = userInput[0]

    for y in dataArray[:,1]:
        
        if  userInput[0] == dataArray[n,1]:
            print("Standard found")
            print("-------------------------------------")  
            flag = True
            count += 1 
        n+=1
        
    my_string = f'There is {count} iterations of {standard}'
    if count == 0: 
        print("there is no such standard ")
        print ("--------------------------------------------------")
        flag = False
        return flag
    print(my_string) #prints out the standard found and the number of iterations in the database 
    return flag 

def standardInDatabase (userInput,dataArray2):
    #find the standard from the Standard Database , retrieve the quotation and description of the User Input standard
    n = 0
    i = 0
    for x in dataArray2[:,0]:
        
        if userInput[0] == dataArray2[n,0]:

            standard = userInput[0] ;description = dataArray2[n,1];mbCost = dataArray2[n,2]
            day = dataArray2[n,3] ;man = dataArray2[n,4]; rate = dataArray2[n,5]
            abCost = dataArray2[n,6]; stkCost = dataArray2[n,7] ; eng = dataArray2[n,8]
            pack = dataArray2[n,9]; totalCost = dataArray2[n,10] ; exch = dataArray2[n,11]
            stkCostUSD = dataArray2[n,12] ;markUp = dataArray2[n,13] ;listPrice = dataArray2[n,14] ; note = dataArray2[n,15]


            print("Standard found in the database")
            print("Standard:",standard)
            print("Description:",description)
            print("MB Cost (MYR):",mbCost)
            print("day: ", day)
            print("man: ", man)
            print("rate: ", rate)
            print("AB cost: ", abCost)
            print("STK cost: ", stkCost)
            print("ENG (MYR): ", eng)
            print("Pack :", pack)
            print("Total Cost (MYR): ", totalCost)
            print("EXCH : ", exch)
            print("STK cost (USD): ", stkCostUSD)
            print("Mark Up ", markUp)
            print("List Price: ", listPrice)
            print("Note: ", note)
            print("--------------------------------------------------")
            

            flag = True
            return flag
            
        n+=1
    
                

def addOnInDatabase (userInput,dataArray3):
    #find the addOn from the AddOns Database , retrieve the quotation and description of the User Input standard
    n = 0
    i = 0
    userInputDataArray = userInput[1].split(",")
    addonDataArray = dataArray3[:,0]

    for x in userInputDataArray:
        for y in addonDataArray:
            if x == y:

                mbCost = dataArray3[i,2]
                day = dataArray3[i,3]
                man = dataArray3[i,4]
                rate = dataArray3[i,5]
                abCost = dataArray3[i,6]
                stkCost = dataArray3[i,7]
                eng = dataArray3[i,8]
                pack = dataArray3[i,9]
                totalCost = dataArray3[i,10]
                exch = dataArray3[i,11]
                stkCostUSD = dataArray3[i,12]
                markUp = dataArray3[i,13]
                listPrice = dataArray3[i,14]

                print("add on found:" , x)
                print("MB Cost (MYR):",mbCost)
                print("day: ", day)
                print("man: ", man)
                print("rate: ", rate)
                print("AB cost: ", abCost)
                print("STK cost: ", stkCost)
                print("ENG (MYR): ", eng)
                print("Pack :", pack)
                print("Total Cost (MYR): ", totalCost)
                print("EXCH : ", exch)
                print("STK cost (USD): ", stkCostUSD)
                print("Mark Up ", markUp)
                print("List Price: ", listPrice)

                print("--------------------------------------------------")

        i+=1


      
def standardMatch (userInput,dataArray):
    n = 0 
    i = 0
    # finding it when the new input Array has the same standard
    # checking which standard correlates to the index 
    for x in index_pos_list:
        
        if userInput[0] == dataArray[index_pos_list[i],1]:
            array1 = userInput[1].split(",")
            array2 = dataArray[index_pos_list[i],2].split(",")
            thisCheckMatched = check(array1,array2)
            if thisCheckMatched == True:
                
                print("C series is found !", dataArray[index_pos_list[i]])
                print ("--------------------------------------------------")

            else: 

                print("C series is not found ! Add new entry to the database")
                print ("--------------------------------------------------")

        i+=1

# Get indexes of all occurrences of same standards  in the list



def check(c,d):# these are 2 array input 
    #checking function to check if the userinput array matches the ConfigCode Database Array

    countTrue = 0 
    if(len(c) != len(d)):
        print("this string doesnt match the length of the userinput string")
        print ("--------------------------------------------------")
        checkALL = False 
        return checkALL
    
    #to check the presence of a valid Addon from configCode DataBase inside the userinput regardless of order
    else:
        for x in c:
            for y in d:
                #print(x,y)
                if x != y: 
                    addOnFlag = False
                    #print(addOnFlag)
                else:
                    addOnFlag = True
                    #print(addOnFlag)
                    break
            if addOnFlag != True:
                check = False
                #print("This Element is False")
                break
            else:
                check = True 
                #print("this Element is true")
                countTrue += 1 
                continue
        
        if countTrue != len(d):
            checkALL = False 
            return checkALL
        else : 
            checkALL = True 
            return checkALL
     
def writetoCSV (userInput,dataArray1,dataArray2,dataArray3):
    # find the standard from the standard Database , retrieve the quotation and description of the User Input standard, put them all together in a csv file
    i = 0 
    n = 0
    j = 0

    userInputDataArray = userInput[1].split(",")
    addonDataArray = dataArray3[:,0]


    header1 = ['Configuration Code For ISP3100', 'Standard', 'Add On']
    header11 = [ 'Standard', 'Add On', 'Configuration Code not found in Database']

    for b in index_pos_list:
        
        if userInput[0] == dataArray1[index_pos_list[j],1]:
            array1 = userInput[1].split(",")
            array2 = dataArray1[index_pos_list[j],2].split(",")
            thisCheckMatched = check(array1,array2)
            if thisCheckMatched == True:
                configurationCode = dataArray1[index_pos_list[j]]
                with open(r"C:\Users\60111\Coding project\Quotation\totalQuotation2.csv",'w') as f_object0: 
                    writer_object = csv.writer(f_object0)
                    writer_object.writerow(header1)
                    writer_object.writerow(configurationCode)
                    #print("Configuration Code found !", configurationCode)
            else:
                with open(r"C:\Users\60111\Coding project\Quotation\totalQuotation2.csv",'w') as f_object0:
                    writer_object = csv.writer(f_object0)
                    writer_object.writerow(header11)
                    writer_object.writerow(userInput)

        j+=1




    header2 = ['Module','Item description','MB Cost','Day', 'Man', 'Rate', 'AB Cost', 'STK Cost (MYR)', 'ENG', 'Pack', 'Total Cost', 'EXCH', 'STK Cost (USD)', 'Mark Up', 'List Price', 'Note']

    for x in dataArray2[:,0]:
        if userInput[0] == dataArray2[n,0]:
            #print("Standard found !", dataArray2[n])
            #print ("--------------------------------------------------")
            standardData = dataArray2[n]
            with open(r"C:\Users\60111\Coding project\Quotation\totalQuotation2.csv",'a') as f_object: 
                writer_object = csv.writer(f_object)
                writer_object.writerow(header2)
                writer_object.writerow(standardData)
            #print("done with writing")
            #print("--------------------------------------------------")
        n+=1

    for k in addonDataArray: 
        for l in userInputDataArray:
            if k == l: 
                #print("addOn found !", dataArray3[i])
                #print ("--------------------------------------------------")
                addOnData = dataArray3[i]
                with open(r"C:\Users\60111\Coding project\Quotation\totalQuotation2.csv",'a',encoding = 'utf-8') as f_object2: 
                    writer_object2 = csv.writer(f_object2)
                    writer_object2.writerow(addOnData)
                #print("done with writing")
                #print("--------------------------------------------------")
        i+=1



# Main program starts here 
# read the csv file and convert it to a numpy array
ff = pd.read_csv(r'C:\Users\60111\Coding project\dataBases\configCode.csv', header=0)
configCodedataArray = ff.to_numpy()

ee = pd.read_csv(r'C:\Users\60111\Coding project\dataBases\standardDatabase.csv', header=0)
standardDataArray2 = ee.to_numpy()
#print("array_new : ", array_new)

gg = pd.read_csv(r'C:\Users\60111\Coding project\dataBases\addOnsDatabase.csv',encoding = 'unicode_escape', header=0)
addOndataArray3 = gg.to_numpy()

#User Input defined here , can be changed to a different method 
userInput = np.array(['ISP3100-S07', 'ISP31-MCRSET,ISP31-3DVIEW,ISP31-PCRAIL,ISP31-ION,ISP31-BCRSET'])


print("userInput : ",userInput)
print("dataArray : ",configCodedataArray)


thisCompareMatch = compare(userInput,configCodedataArray)
thisStandardInDatabase = standardInDatabase(userInput,standardDataArray2)
thisAddOnInDatabase = addOnInDatabase(userInput,addOndataArray3)



if thisCompareMatch == True: 
    index_pos_list = get_index_positions_2(configCodedataArray[:,1],userInput[0])
    print("index_pos_list : ",index_pos_list)
    standardMatch(userInput,configCodedataArray)


testing = writetoCSV(userInput,configCodedataArray, standardDataArray2,addOndataArray3)

#written by Lee Zheng Yi ,for QES Sdn Bhd, product configuration quotation system
#last updated: 30/12/2022
#Checked By : <name here> 
#Date : <date here>