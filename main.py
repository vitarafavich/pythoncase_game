import ru_local as ru
import time
budget = 16000
a = input(ru.BEGIN)
print('Day 1')
answer1_1 = input(ru.PHRASE1_1)
if answer1_1.lower() == ru.YES or answer1_1.lower() == 'yes':
    answer1_2 = input(ru.PHRASE1_2)
    if answer1_2.lower() == ru.YES or answer1_2.lower() == 'yes':
        budget = budget - 2500
        print(ru.PHRASE1_3, budget, ru.RUBLES)
        time.sleep(1.0)
        print(ru.PHRASE1_4)
    else:
        print(ru.PHRASE1_4)
        time.sleep(1.5)
    while True:
        answer1_3 = input(ru.PHRASE1_5)
        if answer1_3.lower() == ru.YES or answer1_3.lower() == 'yes':
            answer1_4 = input(ru.PHRASE1_7)
            answer1_4_1 = answer1_4.strip(' ,.;')
            summ = 0
            if '1' in answer1_4_1:
                summ += 200
            if '2' in answer1_4_1:
                summ += 300
            if '3' in answer1_4_1:
                summ += 200
            budget = budget - summ
            print(ru.PHRASE1_3, budget, ru.RUBLES)
            time.sleep(1.0)
            print(ru.PHRASE1_9)
            time.sleep(1.5)
            answer1_5 = input(ru.PHRASE1_8)
            if answer1_5.lower() == ru.YES or answer1_5.lower() == 'yes':
                budget = budget - 300
                print(ru.PHRASE1_3, budget, ru.RUBLES)
                time.sleep(1.0)
                print(ru.PHRASE1_13)
            else:
                a = input(ru.PHRASE1_10)
                time.sleep(1.0)
                b = input(ru.PHRASE1_11)
                time.sleep(1.0)
                c = input(ru.PHRASE1_12)
                budget = budget - 500
                print(ru.PHRASE1_3, budget, ru.RUBLES)
        else:
            print(ru.PHRASE1_6)
            continue
        break
else:
    print(ru.PHRASE1_4)
    time.sleep(1.5)
    while True:
        answer1_3 = input(ru.PHRASE1_5)
        if answer1_3.lower() == ru.YES or answer1_3.lower() == 'yes':
            answer1_4 = input(ru.PHRASE1_7)
            answer1_4_1 = answer1_4.strip(' ,.;')
            summ = 0
            if '1' in answer1_4_1:
                summ += 200
            if '2' in answer1_4_1:
                summ += 300
            if '3' in answer1_4_1:
                summ += 200
            budget = budget - summ
            print(ru.PHRASE1_3, budget, ru.RUBLES)
            time.sleep(1.0)
            print(ru.PHRASE1_9)
            time.sleep(1.5)
            answer1_5 = input(ru.PHRASE1_8)
            if answer1_5.lower() == ru.YES or answer1_5.lower() == 'yes':
                budget = budget - 300
                print(ru.PHRASE1_3, budget, ru.RUBLES)
                time.sleep(1.0)
                print(ru.PHRASE1_13)
            else:
                print(ru.PHRASE1_10)
                time.sleep(1.0)
                print(ru.PHRASE1_11)
                time.sleep(1.0)
                print(ru.PHRASE1_12)
                budget = budget - 500
                print(ru.PHRASE1_3, budget, ru.RUBLES)
        else:
            print(ru.PHRASE1_6)
            continue
        break
time.sleep(1.3)

# day 2
print('Day 2')
print(ru.phrase2_1)
interactive2_1 = input(ru.phrase2_2)
interactive2_1 = interactive2_1.strip('!?,.:;-_/ ')
if interactive2_1.lower() == ru.YES or interactive2_1.lower() == 'yes':
    interactive2_1_1 = input(ru.phrase2_2_1)
    interactive2_1_1 = interactive2_1_1.strip('!?,.:;-_/ ')
    if interactive2_1_1 == '1':
        print(ru.phrase_singly)
    interactive2_1_2 = input(ru.phrase2_2_2)
    interactive2_1_2 = interactive2_1_2.strip('!?,.:;-_/ ')
    if interactive2_1_2.lower() == ru.YES or interactive2_1_2.lower() == 'yes':

        while True:
            interactive_couple = input(ru.phrase_mutual_lang)
            interactive_couple = interactive_couple.strip('!?,.:;-_/ ')
            if interactive_couple.lower() == ru.YES or interactive_couple.lower() == 'yes':
                print(ru.phrase_accord)
                time.sleep(2.0)
                print(ru.phrase_cellar)
                time.sleep(2.0)
            else:
                break
        print(ru.phrase_conviction)
        time.sleep(2.0)
        print(ru.phrase_search)
        budget = budget - 1800
        print(ru.PHRASE1_3, budget, ru.RUBLES)

    else:
        print(ru.phrase_refusing)
        time.sleep(1.5)
        print(ru.phrase_search)
        budget = budget - 1800
        print(ru.PHRASE1_3, budget, ru.RUBLES)

else:
    time.sleep(1.0)
    print(ru.phrase_good)
    time.sleep(2.0)
    print(ru.phrase_lada)
    time.sleep(2.0)
    print(ru.phrase_hotel)
    time.sleep(2.0)
    print(ru.phrase_spending)
    budget = budget - 800
    print(ru.PHRASE1_3, budget, ru.RUBLES)

#day 3
print('Day 3')
time.sleep(1.5)
print(ru.DAY3_Q1)
budget = budget - 2500
print(ru.PHRASE1_3, budget, ru.RUBLES)
time.sleep(1.0)
b_ = input(ru.DAY3_Q2)
if b_.lower() == ru.NO or b_.lower() == 'no':
    x_ = input(ru.DAY3_Q2_NO)
    time.sleep(2.5)
    print('Day 4')
    time.sleep(2.5)
    y_ = input(ru.DAY4_Q1_1)
if b_.lower() == ru.YES or b_.lower() == 'yes':
    print(ru.DAY3_Q2_YES_1_1)
    time.sleep(1.0)
    print(ru.PHRASE3_5)
    time.sleep(2.0)
    print(ru.DAY3_Q2_YES_1_2)
    time.sleep(2.0)
    while True:
        answer_q3 = input(ru.DAY3_Q2_YES_1_3)
        if '1' in answer_q3:
            print(ru.DAY3_Q3_1)
            budget = budget - 5000
            print(ru.PHRASE1_3, budget, ru.RUBLES)
            print(ru.PHRASE3_13)
            time.sleep(2.5)
            print(ru.DAY3_Q3_1_2)
            print(ru.DAY3_Q3_1_3)
            time.sleep(2.0)
            print(ru.DAY3_Q3_1_4)
            time.sleep(2.0)
            print(ru.DAY3_Q3_1_5)
        else:
            j_ = input(ru.DAY3_Q3_2_1)
            k_ = input(ru.DAY3_Q3_2_2)
            if answer1_5.lower() == ru.YES or answer1_5.lower() == 'yes':
                budget = budget - 2500
                print(ru.PHRASE1_3, budget, ru.RUBLES)
                time.sleep(1.0)
                l_ = input(ru.DAY3_Q4_1_1)
                m_ = input(ru.DAY3_Q4_1_2)
            if answer1_5.lower() == ru.NO or answer1_5.lower() == 'no':
                budget = budget - 5000
                print(ru.PHRASE1_3, budget, ru.RUBLES)
                time.sleep(1.0)
                n_ = input(ru.DAY3_Q5_1_1)
                m_ = input(ru.DAY3_Q4_1_2)
            break
print(ru.DAY3_Q6_1_1)
time.sleep(1.5)
print(ru.PHRASE3_23)
budget = budget - 400
print(ru.DAY3_Q6_1_3, ru.PHRASE1_3, budget, ru.RUBLES)
time.sleep(2.0)
print(ru.DAY3_Q6_1_2)
time.sleep(1.5)
print('Day 4')
time.sleep(1.5)
q_ = input(ru.DAY4_Q1_2)
r = input(ru.DAY4_Q1_2_2)

