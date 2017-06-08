#__author__ = 'NehaS'
# date = 08-06-17
'''PROBLEM : THE JUICE PROBLEM '''

'''SOLUTION : Its was a combinations problem and the exact match for calarios requirnment can only be achieved by trying 
various combination of juice availability in stock. The stock available for a particular friend was taken while taking input from user

Logic: 1. fruitjuice_inCuboard : a list to store available_juice in sorted order.
       2. uniqueItem : a list to store unique juices .
       3. cal_list : contains the list of calarios or respective juices in uniqueItem.
       4. If the combination matched extract the particular juices and its respt calarios and sum them up. And if the sumed result matches 
          with requested calorie then break the loop and display the result


EX:
3 (Number of friends)
5   21 1 21 3 3                  (Calories of each unique fruit juice on the cupboard) (The number of unique fruit juices)
accdeeccdeeaab                   (The actual list of fruit juices in the cupboard)
2                                (Calorie intake requirement for your first friend)
2 3 4                            (Calories of each unique fruit juice on the cupboard) (The number of unique fruit juices)  
baba                             (The actual list of fruit juices in the cupboard)
7                                (Calorie intake requirement for your second friend)

3 5 4 6                          (Calories of each unique fruit juice on the cupboard) (The number of unique fruit juices)
abcbacbabcc                      (The actual list of fruit juices in the cupboard)
15                               (Calorie intake requirement for your third friend)

Output:
SORRY, YOU JUST HAVE WATER (For Friend 1)
ab (For Friend 2)
aaa (For Friend 3)

'''
from itertools import combinations

#global variable
flag = False
calorie_request = 0
fruitjuice_inCuboard = []
uniqueItem = []

#User input for N number of friends are taken
def user_input():
    start = []
    global fruitjuice_inCuboard
    global cal_req
    frnds = input()
    if 1<=frnds<=200:
        # Taking inputs
        for i in range(frnds):
            frnds_list = []
            fruits = raw_input()
            fruitjuice_inCuboard = raw_input()
            cal_req = input()

            frnds_list.append(fruits)
            frnds_list.append(fruitjuice_inCuboard)
            frnds_list.append(cal_req)
            start.append(frnds_list)
            print "\n"
        return start
    else:
        print " Friend limit exceed, party cancle..."

# This function breaks the user input into proper structure
# and store it into its corresponding data structure then manipulate it
def container(userA):
    cal_list = []
    m = 0
    global calorie_request
    global fruitjuice_inCuboard
    global uniqueItem
    global flag

    fruits = userA[0]
    fruitjuice_inCuboard = userA[1]
    calorie_request = userA[2]

    fruits_cal = fruits.split(' ',1)    #spliting number of fruits and its calarios 
    m = int(fruits_cal[0])
    cal_list = fruits_cal[1].split()

    # preparing a structure for the inputs
    if 1<=m<=26 and len(cal_list) == int(m):
        fruitjuice_inCuboard = sorted(fruitjuice_inCuboard)
        for i in fruitjuice_inCuboard:
            if i not in uniqueItem:
                uniqueItem.append(i)
            else:
                pass

        for i in range(1,len(fruitjuice_inCuboard)):
            comb = []
            comb = combinations(fruitjuice_inCuboard, i)
            for j in comb:
                sum_list = 0
                for k in j:
                    if k in uniqueItem:
                        sum_list = sum_list + int(cal_list[uniqueItem.index(k)])
                if calorie_request == sum_list:
                    print ''.join(j)
                    flag = True
                    break
    else:
        print "calories list exceeded or less then the number of fruits"

#############################
# EXECUTION BEGIN FROM HERE #
#############################
content = user_input()
for i in range(len(content)):
    print "\n(For friend "+str(i)+ ")"
    container(content[i])
    if flag == True:
        continue
    else:
        print "SORRY, YOU JUST HAVE WATER"
#.......................................................... END ...................................................................#