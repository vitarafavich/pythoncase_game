import time
PHRASE1_3 = 'Оставшийся бюджет: '
budget = 8000
YES = 'да'
PHRASE1_8 = 'купили еду?'
answer1_5 = input(PHRASE1_8)


RUBLES = 'рублей'
NO = 'нет'

DAY3_Q1 = '''Вы проснулись в гостинице и спустились на завтарак
Собрав вещи, вы отправляетесь в дорогу, предварительно заехав на заправку, стоимость бензина 2500'''
DAY3_Q2 = 'Спустя 4 часа дороги вы видите автомобиль на аварийке, водитель просит о помощи. Остановимся помочь?'
DAY3_Q2_NO = 'Спустя 12 часов в дороге и несколько остановок, вы добираетесь до Новосибирска'
DAY3_Q2_YES_1_1 = '''Остановившись, вы подходите к водителю. Внезапно из-за деревьев выбегает пара человек, 
запрыгивает в вашу машину и угоняет ее. На эмоциях вы кидаетесь следом и пытаетесь ее догнать.'''
DAY3_Q2_YES_1_2 = '''Тем временем водитель «сломанного» автомобиля тоже трогается с места и быстро уезжает следом. 
Кажется, это крах..'''
DAY3_Q2_YES_1_3 = '''Идя пешком по трассе, вы обнаруживаете старый велосипед, одиноко стоящий у столба. 
На нем за час вы добираетесь до ближайшейго поселка городского типа. У вас остается не так много времени, 
а добраться до Красноярска как-то надо. Как действуем дальше?'''
DAY3_Q3_O = '''1. Пойти на жд вокзал
2. Отправиться к поселковому аэропорту'''
DAY3_Q3_1 = ('Стоимость билета 5000')
DAY3_Q3_1_2 = ('Спустя 3 часа к вам подсаживается попутчик, завязывает разговор и предлагает попить чаю')
DAY3_Q3_1_3 = ('Разговорившись, вы не замечаете как проходит следующий час, после чего попутчик прощается и уходит')
DAY3_Q3_1_4 = '''Настало время показать билет, но вы не можете его найти. 
Проводница в ярости высаживает вас на следующей станции в пригороде Омска.'''
DAY3_Q3_1_5 = ('Грустно наблюдая за отъезжающим поездом, в окне вы замечаете улыбающегося *попутчика*.')
DAY3_Q3_2_1 = '''У одного из кукурузников вы замечаете мужчину, который вам кого-то напоминает и через некоторое время вы понимаете,
что это мужчина из забегаловки'''
DAY3_Q3_2_2 = ('Узнав своего старого знакомого, вы просите довезти вас и договариваетесь о приемлемой цене')
DAY3_Q4_1_1 = 'Полет проходит благополучно, спустя 3 часа вы приземляетесь в Омской области'
DAY3_Q4_1_2 = '''Приземлившись в полях омской области, вы еще за час добираетесь до пригорода. ' \
Нужно что-то делать дальше...'''
DAY3_Q5_1_1 = '''Вроде все идет хорошо, но ваш старый знакомый припоминает вам случай из забегаловки двухдневной давности
и просит покинуть самолет. У выхода вы не находите ничего кроме парашюта и жизнь не оставляет вам выбора'''
DAY3_Q6_1_1 = '''Поужинать вы заходите в шашлычную "В гостях у Армена". В заведении было много дальнобойщиков, 
обсуждающих предстоящую поездку в новосибирск. Один из них соглашается подвезти вас бесплатно.'''
DAY3_Q6_1_2 = 'После ужина вы садитесь в фуру и благополучно засыпаете.'
DAY3_Q6_1_3 = '''Стоимость ужина: 400 рублей
'''
DAY4_Q1_2 = 'На утро вы благополучно прибываете в Новосибирск'
DAY4_Q1_2_2 = '''К сожалению, у вас не осталось средств для аренды авто до Красноярска. ' \
Но у вас есть возможность их заработать. Сыграем?'''
DAY4_Q1_1 = '''у вас совсем не осталось денег на бензин, чтобы благополучно добраться до Красноярска 
необходимо их заработать. Сыграем?'''
GAME_1 = '''Вам будет предложено решить 10 примеров. Чтобы решить задание и ввести ответ дается 15 секунд. ' \
Проигрывая один раз ы завершаете свое участие и не добираетесь до Красноярска
'''
GAME_0 = '''1. Верно
2. Неверно'''

print('Day 3')
time.sleep(1.5)
a_ = input(DAY3_Q1)
budget = budget - 2500
print(PHRASE1_3, budget, RUBLES)
time.sleep(1.5)
b_ = input(DAY3_Q2)
if b_.lower() == NO or b_.lower() == 'no':
    x_ = input(DAY3_Q2_NO)
    time.sleep(1.5)
    print('Day 4')
    time.sleep(1.5)
    y_ = input(DAY4_Q1_1)
if b_.lower() == YES or b_.lower() == 'yes':
    c_1 = input(DAY3_Q2_YES_1_1)
    c_2 = input(DAY3_Q2_YES_1_2)
    c_3 = input(DAY3_Q2_YES_1_3)
    answer_q3 = input(DAY3_Q3_O)
    if '1' in answer_q3:
        e_ = input(DAY3_Q3_1)
        budget = budget - 5000
        time.sleep(1.5)
        print(PHRASE1_3, budget, RUBLES)
        time.sleep(1.5)
        f_ = input(DAY3_Q3_1_2)
        g_ = input(DAY3_Q3_1_3)
        h_ = input(DAY3_Q3_1_4)
        i_ = input(DAY3_Q3_1_5)
        #СДЛЕАТЬ ЦИКЛ ВОЗВРАЩЕНИЯ К ВОПРОСУ И ВОЗРАТА 5К
    if '2' in answer_q3:
        j_ = input(DAY3_Q3_2_1)
        k_ = input(DAY3_Q3_2_2)
        if answer1_5.lower() == YES or answer1_5.lower() == 'yes':
            budget = budget - 2500
            print(PHRASE1_3, budget, RUBLES)
            time.sleep(1.0)
            l_ = input(DAY3_Q4_1_1)
            m_ = input(DAY3_Q4_1_2)
        if answer1_5.lower() == NO or answer1_5.lower() == 'no':
            budget = budget - 5000
            print(PHRASE1_3, budget, RUBLES)
            time.sleep(1.0)
            n_ = input(DAY3_Q5_1_1)
            m_
    o_ = input(DAY3_Q6_1_1)
    budget = budget - 400
    print(DAY3_Q6_1_3, PHRASE1_3, budget, RUBLES)
    time.sleep(1.0)
    p_ = input(DAY3_Q6_1_2)
    time.sleep(1.5)
    print('Day 4')
    time.sleep(1.5)
    q_ = input(DAY4_Q1_2)
    r = input(DAY4_Q1_2_2)
#game
z = input(GAME_1, GAME_0)
z_0 = input()
ans_1 = input('25*3>6*10 + 5')
while time.sleep<=(15) and '1' in ans_1:
    ans_2 = input('436+416=852')
    if '2' is ans_2:
        ans_3 = input('')






