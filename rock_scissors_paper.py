import random # Подключение библиотеки random
# инициализируем переменные счета для игрока и компьютера
player_score = 0
computer_score = 0
restart ="д"
variants = ["камень", "ножницы", "бумага"] # список возможных вариантов выбора
print("Возможные варианты выбора: камень, ножницы, бумага")
while restart == "д": # цикл while для возможности повтора игры в пределах сессии
    player_choice = input("Игрок: ")
    # проверка на выбор правильного вариананта, пока не будет выбран корректный, пользователю будет предлагатся сделать выбор еще раз
    while player_choice.lower() not in variants: # добавляем .lower() чтобы ввод вариантов не был чуствителен к регистру
        print("Выберете вариант из возможных!")
        player_choice = input("Игрок: ")
    computer_choice = random.choice(variants) # выбор варианта компьютера
    print("Компьютер:",computer_choice) # выводим его на экран
    # организовываем логику игры

    # если выбраны одинаковые варианты
    if player_choice.lower() == computer_choice:
        print("Ничья! Счет: ",player_score,":",computer_score)
    #  варианты развития если игрок выбрал камень
    elif player_choice.lower() == "камень": 
        if computer_choice == "ножницы":
            player_score += 1
            print("Игрок победил! Счет: ",player_score,":",computer_score)
        else:
            computer_score += 1
            print("Компьютер победил :( Счет: ",player_score,":",computer_score)
    #  варианты развития если игрок выбрал ножницы
    elif player_choice.lower() == "ножницы":
        if computer_choice == "бумага":
            player_score += 1
            print("Игрок победил! Счет: ",player_score,":",computer_score)
        else:
            computer_score += 1
            print("Компьютер победил :( Счет: ",player_score,":",computer_score)
    #  варианты развития если игрок выбрал бумагу       
    elif player_choice.lower() == "бумага":
        if computer_choice == "камень":
            player_score += 1
            print("Игрок победил! Счет: ",player_score,":",computer_score)
        else:
            computer_score += 1
            print("Компьютер победил :( Счет: ",player_score,":",computer_score)
    # диалог приглашение сыграть еще раз
    restart = input("Если хотите сыграть еще раз нажмите д, а для выхода любую другую клавишу: ")
    print("") # пустая строка разделитель, чтобы было удобнее смотреть за результатами