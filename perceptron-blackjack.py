def dealer(list1,list2,list_cards_1):
    """decide the method of dealer plays"""
    total=sum(list1)
    if total>21:
        result='lose'
        return(result,list2)
    if list2[0] and list2[1]:
        if list2[0]+list2[1] > total:
             result='lose'
        else:
            dealer_3=random.choice(list_cards_1)
            list_cards_1.remove(dealer_3)
            if dealer_3 ==0:
                if sum(list2)<=10:
                    dealer_3=11
                else:
                    dealer_3=1
            list2.append(dealer_3)
            total_dealer=sum(list2)
            if total_dealer>21:
                result ='win'
            else:
                if total_dealer <= total:
                    result ='win'
                else:
                    result ='lose'


    if list2[0]==0 and list2[1] != 0:
        change_1=11
        if change_1+list2[1]> total:
            result ='lose'
        else:
            dealer_3 = random.choice(list_cards_1)
            list_cards_1.remove(dealer_3)
            list2.append(dealer_3)
            if dealer_3:    # not 0
                if change_1+list2[1]+dealer_3<=21:
                    if change_1+list2[1]+dealer_3>total:
                        result ='lose'
                    else:
                        result ='win'
                else:
                    change_1=1
                    if change_1+ list2[1] + dealer_3 > total:
                        result ='lose'
                    else:
                        result ='win'
            else:   # 0
                change_2=1
                if change_1+list2[1]+change_2<=21:
                    if change_1+list2[1]+change_2>total:
                        result ='lose'
                    else:
                        result ='win'
                else:  # bust
                    change_1=1
                    if change_1 + list2[1] + change_2> total:
                        result ='win'
                    else:
                        result ='lose'




    if list2[1]==0 and list2[0] != 0:
        change_1=11
        if change_1+list2[0]> total:
            result ='lose'
        else:
            dealer_3 = random.choice(list_cards_1)
            list_cards_1.remove(dealer_3)
            if dealer_3:    # not 0
                if change_1+list2[0]+dealer_3<=21:
                    if change_1+list2[0]+dealer_3>total:
                        result ='lose'
                    else:
                        result ='win'
                else:
                    change_1=1
                    if change_1+ list2[0] + dealer_3 > total:
                        result ='lose'
                    else:
                        result='win'
            else:   # 0
                change_2=1
                if change_1+list2[0]+change_2<=21:
                    if change_1+list2[0]+change_2>total:
                        result ='lose'
                    else:
                        result ='win'
                else:  # bust
                    change_1=1
                    if change_1 + list2[0] + change_2> total:
                        result =='win'
                    else:
                        result ='lose'
            list2.append(dealer_3)


    if list2[0]==0 and list2[1]==0:
        change_1=11
        change_2=1
        dealer_3 = random.choice(list_cards_1)
        list_cards_1.remove(dealer_3)
        if change_1 + change_2 +dealer_3>21:
            change_1=1
            if change_1 + change_2 + dealer_3 > total:
                result ='lose'
            else:
                result ='win'
        else:
            if change_1 + change_2 + dealer_3 > total:
                result ='lose'
            else:
                result ='win'
        list2.append(dealer_3)
    list_2=list2
    return (result,list_2)


import random
def choice():
    """define the first two cards that player and dealer have"""
    list_cards = [0, 0, 0, 0, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9,
                  9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    list_cards= list_cards*4
    play_1 = random.choice(list_cards)
    list_cards_1 = list_cards
    list_cards_1.remove(play_1)
    dealer_1 = random.choice(list_cards_1)
    list_cards_1.remove(dealer_1)
    play_2 = random.choice(list_cards_1)
    list_cards_1.remove(play_2)
    dealer_2 = random.choice(list_cards_1)
    list_cards_1.remove(dealer_2)
    list1=[play_1,play_2]
    list=[dealer_1,dealer_2]
    return (list1,list,list_cards_1)





# define player

def play(list, list_cards_1):
    """define original method of player use"""
    if list[0]==0 and list[1]!=0:
        list[0]=11
    if list[1]==0 and list[0] != 0:
        list[1]=11
    if list[0] ==0 and list[1]==0:
        list[0]=11
        list[1]==1
    while sum(list)<15:
        card=random.choice(list_cards_1)
        list.append(card)
        list_cards_1.remove(card)
    list_cards_2=list_cards_1
    list1=list
    return (list1,list_cards_2)



# bouble method to find the point


Y=[]
X=[]

for i in range(100):
    list1,list2,list_card= choice()
    list, list_card=play(list1,list_card)
    result,list2=dealer(list1,list2,list_card)
    if result=='lose':
        y=-1
    else:
        y=1
    x=(sum(list1),list2[0])
    X.append(x)
    Y.append(y)

import numpy as np
w=np.array([1,1])
b=1

# use perceptron to find classification (the condition that whether we hit or not)
arr=np.array(X)
arr_y=np.array(Y)
for j in range(100000):
    for i in range(100):
        while arr_y[i]*((np.dot(arr[i], w))+b) <= 0:
            w = w + (0.1*(arr[i]*arr_y[i])).T
            b = b + 0.1* arr_y[i]


# the condition is decided by sum of player's first two cards' number and the dealer's first card

list1,list2,list_card=choice()
if 1.2*sum(list1)+list2[0]*(-2.3)-24<0:
    card=random.choice(list_card)
    list1.append(card)
    list_card.remove(card)



number=0
for i in range(1000):
    list1, list2, list_card = choice()
    if list[0]==0:
        list[0]=11
    if list[1]==0:
        list[1]==11
    if 1.2 * sum(list1) + list2[0] * (-2.3) - 24 < 0:
        card = random.choice(list_card)
        list1.append(card)
        list_card.remove(card)
    result,list2=dealer(list1,list2,list_card)
    if result=='win':
        number+=1






























