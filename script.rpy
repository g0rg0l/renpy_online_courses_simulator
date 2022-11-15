#let's celebrate and suck some dick

label touch_pet: # Лейбл, который вызывается из лейбла, в котором мы трогаем питомца. Далее - возврат туда, откуда был вызван
    if pet == "cat":
        $ rnd = renpy.random.randint(1, 3)

        if rnd == 1:
            show cat_zoom_1 with fade
        elif rnd == 2:
            show cat_zoom_2 with fade
        else:
            show cat_zoom_3 with fade

        cat "*Мурлычет*"

        window hide

        if rnd == 1:
            hide cat_zoom_1 with fade
        elif rnd == 2:
            hide cat_zoom_2 with fade
        else:
            hide cat_zoom_3 with fade

    else:
        $ rnd = renpy.random.randint(1, 3)

        if rnd == 1:
            show dog_zoom_1 with fade
        elif rnd == 2:
            show dog_zoom_2 with fade
        else:
            show dog_zoom_3 with fade

        dog "*Радостно виляет хвостиком*"

        window hide

        if rnd == 1:
            hide dog_zoom_1 with fade
        elif rnd == 2:
            hide dog_zoom_2 with fade
        else:
            hide dog_zoom_3 with fade

    return

# Начальный лейбл
label start:
    scene input_bg

    call screen input_name with fade

    python:
        checked_name = check_name(_return)
        if checked_name == "emptyemptyemptyemptye":
            renpy.say(navigator, "Пустой ввод.")
            renpy.jump("technical_label_input")
        elif checked_name == "largelargelargelargel":
            renpy.say(navigator, "Слишком длинное имя.")
            renpy.jump("technical_label_input")
        elif checked_name == "spacesspacesspacesspa":
            renpy.say(navigator, "Имена, состоящие только лишь из пробелов, запрещены.")
            renpy.jump("technical_label_input")
        else:
            name = checked_name
            renpy.jump("continue_of_entering")

# технические лейблы нужны для того, чтобы "циклиться" в каком-то месте в сюжете (изучить повнимательнее)
label technical_label_input:
    scene input_bg

    call screen input_name

    python:
        checked_name = check_name(_return)
        if checked_name == "emptyemptyemptyemptye":
            renpy.say(navigator, "Пустой ввод.")
            renpy.jump("technical_label_input")
        elif checked_name == "largelargelargelargel":
            renpy.say(navigator, "Слишком длинное имя.")
            renpy.jump("technical_label_input")
        elif checked_name == "spacesspacesspacesspa":
            renpy.say(navigator, "Имена, состоящие только лишь из пробелов, запрещены.")
            renpy.jump("technical_label_input")
        else:
            name = checked_name


 # ввод ПОЛА и ПИТОМЦА
label continue_of_entering:
    call screen input_sex_and_pet with dissolve

label part_1_2:

    if pet == "cat":
        scene home_with_cat with dissolve
    elif pet == "dog":
        scene home_with_dog with dissolve


    navigator "Здравствуйте, [name]! Меня зовут  Навигатор."

    $ navigator_name = "Навигатор"

    navigator "Вам нужно сделать онлайн-курс? Я Ваш цифровой помощник на этом пути."
    navigator "В ходе игры Вы будете выполнять задания, которые помогут закрепить знания по разработке онлайн-курса."
    navigator "Действия игры происходят в разных локациях. Вы можете перемещаться между ними."
    navigator "Если возникнут сложности, обращайтесь ко мне."
    navigator "Следите за электронной почтой! Не пропустите важные сообщения."
    navigator "Ой,{w=1} кажется Вам уже кто-то написал..."

    $ current_message = ("Зав. кафедрой", "Добрый день, [name]! У меня для Вас интересное поручение. Жду Вас сегодня на кафедре. С уважением, Заведующий кафедрой.")
    $ user_have_new_message = True # иконка нового письма
    $ user_need_to_read_mail = True # сюжетное сообщение
    $ flag_room_computer_opened = True # компьютер разблокирован
    $ arrow_at_computer = True # стрелки
    $ arrow_at_message_icon = True # стрелки

 # Если человек прочитал сюжетное сообщение, то при закрытии компьютера -> выход
 # Во всех остальных случаях - цикличность
label technical_label_1_2_1:

    if pet == "cat":
        scene home_with_cat
    elif pet == "dog":
        scene home_with_dog

    if flag_technical_label_1_2_1:

        call screen room with fade
    else:
        $ flag_technical_label_1_2_1 = True
        call screen room

    $ arrow_at_computer = False

    if _return == "open_computer":

        scene desktop_bg

        call screen computer with fade

        if _return == "close_computer":
            jump technical_label_1_2_1
        elif _return == "mail_checked":
            $ user_need_to_read_mail = False
            jump giving_an_order_at_home # Выход

# Первых выход из комнаты
label giving_an_order_at_home:

    if pet == "cat":
        scene home_with_cat with fade
    elif pet == "dog":
        scene home_with_dog with fade

    navigator "Чтобы покинуть комнату, нажмите на дверь."

    $ flag_room_door_opened = True
    $ arrow_at_door_at_home = True

# Пока не выйдем из комнаты
label technical_label_1_2_2:

    if pet == "cat":
        scene home_with_cat
    elif pet == "dog":
        scene home_with_dog

    if flag_technical_label_1_2_2:
        call screen room with fade
    else:
        $ flag_technical_label_1_2_2 = True
        call screen room

    if _return == "open_computer":
        scene desktop_bg

        call screen computer with fade

        if _return == "close_computer":
            jump technical_label_1_2_2

    elif _return == "exit":
        $ arrow_at_door_at_home = False
        menu:
            "Пойти на кафедру":
                jump department_door
            "Остаться дома":
                $ flag_technical_label_1_2_2 = False
                navigator "Вас ждут на кафедре."
                jump technical_label_1_2_2

# Пришли к двери кафедры
# Запускается мини-мини-игра с кликами на дверь
label department_door:
    scene department_door with fade

    if sex == "male":
        male_player "{i}Через 10 минут я уже стоял перед дверью{/i}"
        male_player "{i}Осталось только постучать.{/i}"
    else:
        female_player "Через 10 минут я уже стояла перед дверью"
        female_player "Осталось только постучать."

    navigator "Для того чтобы постучать в дверь, нажмите несколько раз на неё."

    call screen department_door

    if _return == "go":
        jump department_1_3

# Зашли на кафедру
label department_1_3:
    scene department with fade

    show headOfDepartment medium_funny with moveinleft

    headOfDepartment "Добрый день, коллега!"
    headOfDepartment "Какая хорошая сегодня погода, не правда ли?"

    if sex == "male":
        male_player "Здравствуйте! Да, день сегодня чудесный!"
    else:
        female_player "Здравствуйте! Да, день сегодня чудесный!"

    hide headOfDepartment at dslv
    show headOfDepartment normal at dslv(0.4)

    headOfDepartment "У меня для Вас интересное поручение."
    headOfDepartment "Трендом нашего времени является онлайн-образование. Дисциплина, которую Вы ведёте, очень популярна у студентов."
    headOfDepartment "Предлагаю Вам разработать по ней онлайн-курс. Думаю, это будет интересный опыт!"

    if sex == "male":
        male_player "Согласен, будем новыми звёздами онлайна!"
    elif sex == "female":
        female_player "Согласна, будем новыми звёздами онлайна!"

    hide headOfDepartment at dslv
    show headOfDepartment funny:
        align (0.3699, 1.0)

    headOfDepartment "Отлично! Сходите к коллегам из Центра \"Открытое образование\", узнайте, какие Ваши дальнейшие действия."

    if sex == "male":
        male_player "Хорошо. До свидания!"
    else:
        female_player "Хорошо. До свидания!"

    headOfDepartment "Всего доброго!"

    window hide Dissolve(0.0)
    hide headOfDepartment with dissolve

# Пока не уйдём в центр
label technical_label_1_3:
    call screen department

    if _return == "exit":
        menu:
            "Остаться на кафедре":
                navigator "Вас уже ждут в Центре."
                jump technical_label_1_3
            "Пойти в Центр":
                jump nots_1_4
            "Пойти домой":
                navigator "Лучше не затягивать с дальнейшей работой. Вас ждут в Центре."
                jump technical_label_1_3

# В центре
label nots_1_4:
    scene nots with  fade

    if sex == "male":
        male_player "Добрый день, коллеги! Меня зовут [name]."
        male_player "Мне нужна Ваша консультация по созданию онлайн-курса. Могли бы Вы помочь?"
    else:
        female_player "Добрый день, коллеги! Меня зовут [name]."
        female_player "Мне нужна Ваша консультация по созданию онлайн-курса. Могли бы Вы помочь?"

    show ekaterina pry with dissolve

    ekaterina_hiden "Здравствуйте, [name]! Меня зовут Екатерина. Какой у Вас вопрос?"

    if sex == "male":
        male_player "Приступаю к разработке онлайн-курса. Что мне нужно сделать на первом этапе?"
    else:
        female_player "Приступаю к разработке онлайн-курса. Что мне нужно сделать на первом этапе?"

    show ekaterina funny

    ekaterina "Отлично! Для начала  достаточно подготовить программу курса и подобрать Вашу фотографию."

    show ekaterina normal_2

    ekaterina "Мы отправим Вам на почту шаблон программы. Вы ее заполните, согласуете и отправите нам. Все достаточно просто!"

    if sex == "male":
        male_player "Это легко. Спасибо! Побегу за компьютер, буду искать фотографию! До свидания!"
    else:
        female_player "Это легко. Спасибо! Побегу за компьютер, буду искать фотографию! До свидания!"

    show ekaterina funny

    ekaterina "До свидания! Рады, что Вы с нами!"

    window hide Dissolve(0.0)
    hide ekaterina with dissolve

# пока не уйдём домой
label technical_label_1_4:
    call screen nots

    if _return == "exit":
        menu:
            "Пойти на кафедру":
                navigator "Вам нужно подобрать фотографию, а на кафедре это сделать вряд ли получится."
                jump technical_label_1_4
            "Остаться в Центре":
                navigator "Заведующий ждёт Вашу программу. Лучше не затягивать."
                jump technical_label_1_4
            "Пойти домой":
                jump pre_choosing_photo_1_5

# Пришли домой - запуск знакомства с питомцем. Shake() - в user_variables.rpy
label pre_choosing_photo_1_5:
    if pet == "cat":
        scene home_with_cat with fade
    elif pet == "dog":
        scene home_with_dog with fade

    navigator "Пора подобрать фотографию, заглянем в фотоальбом?"

    if pet == "cat":
        cat "Мяу... мяу... мяу..." with Shake((0, 0, 0, 0), 1.5, dist=10)
    elif pet == "dog":
        dog "Гав... гав... гав..." with Shake((0, 0, 0, 0), 1.5, dist=10)

    navigator "Кажется, Ваш питомец заскучал."
    navigator "К слову, как его зовут?"

# Пока не введём нормальное имя для питомца
label technical_label_1_5_1:
    call screen input_name_of_pet with dissolve
    python:
        checked_name = check_name(_return)
        if checked_name == "emptyemptyemptyemptye":
            renpy.say(navigator, "Пустой ввод.")
            renpy.jump("technical_label_1_5_1")
        elif checked_name == "largelargelargelargel":
            renpy.say(navigator, "Слишком длинное имя.")
            renpy.jump("technical_label_1_5_1")
        elif checked_name == "spacesspacesspacesspa":
            renpy.say(navigator, "Имена, состоящие только лишь из пробелов, запрещены.")
            renpy.jump("technical_label_1_5_1")
        else:
            pet_name = checked_name


    navigator "Замечательное имя!"
    navigator "Не забывайте иногда гладить его."
    $ flag_room_pet_opened = True # Теперь можно гладить питомца в комнате
    $ arrow_at_pet = True # В первый раз заставляем нажать на питомца стрелкой

# Пока не погладим питомца
label technical_label_1_5_2:

    if pet == "cat":
        scene home_with_cat
    elif pet == "dog":
        scene home_with_dog

    if flag_technical_label_1_5_2:
        call screen room with fade
    else:
        $ flag_technical_label_1_5_2 = True
        call screen room

    if _return == "open_computer":
        scene desktop_bg
        call screen computer with fade

        if _return == "close_computer":
            jump technical_label_1_5_2

    elif _return == "exit":
        $ flag_technical_label_1_5_2 = False
        menu:
            "Пойти в Центр":
                navigator "Вы ещё не выполнили задание Екатерины."
                jump technical_label_1_5_2
            "Пойти на кафедру":
                navigator "Кажется, дома у Вас ещё остались незаконченные дела."
                jump technical_label_1_5_2
            "Остаться дома":
                jump technical_label_1_5_2
    elif _return == "touch_pet":
        $ arrow_at_pet = False
        call touch_pet

    navigator "Ах да{w=1}, фотография."
    $ flag_room_album_opened = True
    $ arrow_at_album = True

# Погладили, теперь - пока не нажмём на альбом
label technical_label_1_5_3:

    if pet == "cat":
        scene home_with_cat
    elif pet == "dog":
        scene home_with_dog

    if flag_technical_label_1_5_3:
        call screen room with fade
    else:
        $ flag_technical_label_1_5_3 = True
        call screen room

    if _return == "open_computer":
        scene desktop_bg
        call screen computer with fade

        if _return == "close_computer":
            jump technical_label_1_5_3

    elif _return == "exit":
        $ flag_technical_label_1_5_3 = False
        menu:
            "Пойти в Центр":
                navigator "Вы ещё не выполнили задание Екатерины."
                jump technical_label_1_5_3
            "Пойти на кафедру":
                navigator "Кажется, дома у Вас ещё остались незаконченные дела."
                jump technical_label_1_5_3
            "Остаться дома":
                jump technical_label_1_5_3
    elif _return == "touch_pet":
        $ flag_technical_label_1_5_3 = False
        call touch_pet
        jump technical_label_1_5_3
    elif _return == "open_album":
        $ arrow_at_album = False
        jump choosing_photo_1_5

# Запуск мини-игры с отбором фотографий в альбоме
label choosing_photo_1_5:

    scene album
    call screen album with fade

    if pet == "cat":
        scene home_with_cat with fade
    elif pet == "dog":
        scene home_with_dog with fade

    if _return != "correct":

        if _return == "uncorrect_1":
            navigator "Фотография выглядит обрезанной, поищите другую."
        elif _return == "uncorrect_2":
            navigator "Вряд ли эта фотография подойдёт. Вы стоите слишком далеко."
        elif _return == "uncorrect_3":
            navigator "Неудачная фотография. Фон у фото должен быть светлым."
        elif _return == "uncorrect_4":
            navigator "Красивые обои! Однако, нужен однотонный фон."
        elif _return == "uncorrect_5":
            navigator "Неверное соотношение сторон у фотографии."
        jump choosing_photo_1_5
    else: # как только выбрали нужное фото
        navigator "Да, это фотография подходит: светлый фон, размер 1:1, Вас хорошо видно."
        navigator "Стоит проверить почту. Возможно, Екатерина прислала необходимые документы."

        $ flag_room_album_opened = False # на альбом больше нельзя нажать
        $ current_message = ("Екатерина", "Здравствуйте, [name]! В продолжение разговора отправляю Вам шаблон программы онлайн-курса. Желаю удачи! С уважением, куратор Екатерина")
        $ user_have_new_message = True # пришло письмо
        $ user_need_to_read_mail = True # оно сюжетное
        $ show_file_to_make_programm = True # показать иконку "приложенный файл" в письме

        jump technical_label_1_6

# Пока не нажмём на приложенный в письме файл
label technical_label_1_6:

    if pet == "cat":
        scene home_with_cat
    elif pet == "dog":
        scene home_with_dog

    if flag_technical_label_1_6:
        call screen room with fade
    else:
        $ flag_technical_label_1_6 = True
        call screen room

    if _return == "open_computer":
        scene desktop_bg
        call screen computer with fade

        if _return == "close_computer":
            jump technical_label_1_6
        elif _return == "mail_checked":
            $ user_need_to_read_mail = False
            jump technical_label_1_6
        elif _return == "open_file":
            $ user_need_to_read_mail = False
            jump making_program_1_6
    elif _return == "exit":
        $ flag_technical_label_1_6 = False
        menu:
            "Пойти в Центр":
                navigator "Кажется, дома у Вас ещё остались незаконченные дела."
            "Пойти на кафедру":
                navigator "Программа ещё не составлена. Рекомендую заняться ей."
            "Остаться дома":
                pass
        jump technical_label_1_6
    elif _return == "touch_pet":
        $ flag_technical_label_1_6 = False
        call touch_pet
        jump technical_label_1_6

# мини игра на составление программы
label making_program_1_6:

    scene bg

    call screen making_program_mini_game with fade

    if pet == "cat":
        scene home_with_cat with fade
    elif pet == "dog":
        scene home_with_dog with fade

    navigator "Отлично! Программа составлена, давайте проверим почту - не ответили ли Вам."

    $ current_message = ("Зав. кафедрой", "Здравствуйте, [name]! Программу получил, сегодня обязательно посмотрю. Жду Вас на кафедре, чтобы обсудить детали. С уважением, Заведующий кафедрой")
    $ user_have_new_message = True # пришло письмо
    $ user_need_to_read_mail = True # оно сюжетное
    $ show_file_to_make_programm = False # приложенный файл больше не показывается в письмах

# Пока не прочтём письмо
label technical_label_1_7_1:

    if pet == "cat":
        scene home_with_cat
    elif pet == "dog":
        scene home_with_dog

    if flag_technical_label_1_7_1:
        call screen room with fade
    else:
        $ flag_technical_label_1_7_1 = True
        call screen room

    if _return == "open_computer":
        scene desktop_bg
        call screen computer with fade

        if _return == "close_computer":
            jump technical_label_1_7_1
        elif _return == "mail_checked":
            $ user_need_to_read_mail = False
            jump technical_label_1_7_2
    elif _return == "exit":
        $ flag_technical_label_1_7_1 = False
        menu:
            "Пойти в Центр":
                navigator "Вы ещё не согласовали составленную программу. Дождитесь письма от Заведующего кафедрой."
            "Пойти на кафедру":
                navigator "Думаю, стоит сперва проверить почту."
            "Остаться дома":
                pass
        jump technical_label_1_7_1
    elif _return == "touch_pet":
        $ flag_technical_label_1_7_1 = False
        call touch_pet
        jump technical_label_1_7_1

# Пока не пойдём на кафедру
label technical_label_1_7_2:

    if pet == "cat":
        scene home_with_cat
    elif pet == "dog":
        scene home_with_dog

    if flag_technical_label_1_7_2:
        call screen room
    else:
        call screen room with fade

    if _return == "open_computer":
        scene desktop_bg
        call screen computer with fade

        if _return == "close_computer":
            $ flag_technical_label_1_7_2 = False
            jump technical_label_1_7_2

    elif _return == "exit":
        $ flag_technical_label_1_7_2 = True
        menu:
            "Пойти на кафедру":
                jump checking_created_program_1_7
            "Пойти в Центр":
                navigator "Думаю, сейчас Вам нужно не туда."
                jump technical_label_1_7_2
            "Остаться дома":
                navigator "Поторопитесь на кафедру - Заведующий Вас уже ждёт."
                jump technical_label_1_7_2
    elif _return == "touch_pet":
        $ flag_technical_label_1_7_2 = True
        call touch_pet
        jump technical_label_1_7_2

# разбор полётов по программе с зав. кафедрой
label checking_created_program_1_7:
    scene department with fade

    show headOfDepartment medium_funny with dissolve

    if sex == "male":
        male_player "Добрый день!"
    else:
        female_player "Добрый день!"

    headOfDepartment "Здравствуйте!"

    if sex == "male":
        male_player "Как Вам моя программа онлайн-курса?"
    else:
        female_player "Как Вам моя программа онлайн-курса?"

    # Если ошибок нет
    if making_program_one_true == "correct" and making_program_two_true == "correct" and making_program_three_true == "correct" and making_program_four_true == "correct" and making_program_five_true == "correct" and making_program_six_true == "correct" and making_program_seven_true == "correct":

        show headOfDepartment funny

        headOfDepartment "Программа получилась хорошая, у меня замечаний нет, согласую. Не забудьте отправить все документы в Центр!"

        if sex == "male":
            male_player "Отлично! Уже бегу к своему компьютеру!"
        else:
            female_player "Отлично! Уже бегу к своему компьютеру!"

    else:
        hide headOfDepartment
        show headOfDepartment normal at dslv(0.35)

        headOfDepartment "Программа получилась хорошая, однако, есть над чем еще поработать."

        hide headOfDepartment
        show headOfDepartment sad:
            align (0.35, 1.0)
            linear 0.3 xalign 0.9

        # диалог с объяснением ошибок, опирающийся на запомненные в самой мини-игре переменные
        if making_program_one_true != "correct":
            if making_program_one_true == "uncorrect_2":
                headOfDepartment "Вы неверно сформулировали название Вашего курса."
                headOfDepartment "Оно может совпадать с той формулировкой, которая указана в учебном плане."
                headOfDepartment "Однако она должна содержать не более 7 слов. Если название дисциплины слишком длинное - сократите его."
            elif making_program_one_true == "uncorrect_3":
                headOfDepartment "Название Вашего курса слишком длинное, это запутает студентов."
                headOfDepartment "К тому же, на онлайн-платформах есть ограничение на длину названия онлайн-курса: 7-9 слов."
                headOfDepartment "Иначе оно просто не поместится в отведенном для него поле."
            elif making_program_one_true == "uncorrect_4":
                headOfDepartment "Напрасно считать, что название онлайн-курса не важно."
                headOfDepartment "Оно должно мотивировать студента записаться на Ваш курс и быть коротким, отражать суть."

        if making_program_two_true != "correct":
            if making_program_two_true == "uncorrect_1":
                headOfDepartment "С аннотацией Вам нужно еще поработать."
                headOfDepartment "Цели, пререквизиты, продолжительность и время изучения в неделю отражаются в других пунктах."
                headOfDepartment "Аннотация описывает содержание и его особенности в 1-2 предложениях (до 400 знаков без пробелов)."
            elif making_program_two_true == "uncorrect_2":
                headOfDepartment "С аннотацией Вам нужно еще поработать."
                headOfDepartment "Нормативные документы, содержание по разделам и темам, виды аттестации в аннотации не указываются."
                headOfDepartment "Аннотация описывает содержание и его особенности в 1-2 предложениях (до 400 знаков без пробелов)."
            elif making_program_two_true == "uncorrect_4":
                headOfDepartment "С аннотацией Вам нужно еще поработать."
                headOfDepartment "Задачи, связь с другими дисциплинами, информация об авторах указываются в других разделах программы."
                headOfDepartment "Аннотация описывает содержание и его особенности в 1-2 предложениях (до 400 знаков без пробелов)."

        if making_program_three_true != "correct":
            if making_program_three_true == "uncorrect_1":
                headOfDepartment "Цель курса формулируется кратко и отвечает на вопрос, чему научится студент после прохождения курса."
            elif making_program_three_true == "uncorrect_3":
                headOfDepartment "Для онлайн-курса не рекоммендуется копировать цель из рабочей программы дисциплины."
                headOfDepartment "Она должна быть краткой и отвечать на вопрос, как студент сможет использовать полученные знания."
            elif making_program_three_true == "uncorrect_4":
                headOfDepartment "Цель курса - это не об использовании образовательных технологий."
                headOfDepartment "Цель - это про то, чему научится студент после прохождения курса."

        if making_program_four_true != "correct":
            if making_program_four_true == "uncorrect_1":
                headOfDepartment "Кроме всего прочего, нужно рассчитать примерную учебную нагрузку в неделю."
            elif making_program_four_true == "uncorrect_2":
                headOfDepartment "Вы забыли указать в трудоемкость в зачетных единицах."
            elif making_program_four_true == "uncorrect_3":
                headOfDepartment "Вы забыли указать в трудоемкость в академических и астрономических часах."

        if making_program_five_true != "correct":
            if making_program_five_true == "uncorrect_1":
                headOfDepartment "Не всегда язык Вашего онлайн-курса будет русским."
                headOfDepartment "Например, для студентов-иностранцев рекоммендуется разрабатывать курс на понятном им языке."
            elif making_program_five_true == "uncorrect_3":
                headOfDepartment "Выбор языка, на котором будет читаться курс, делает кафедра, ответственная за его реализацию."
                headOfDepartment "Если он рассчитан на иностранных студентов, то рекоммендуется разрабатывать курс на понятном им языке."
            elif making_program_five_true == "uncorrect_4":
                headOfDepartment "Язык курса может отличаться от языка реализации образовательной программы."
                headOfDepartment "Выбор делает кафедра, ответственная за онлайн-курс."

        if making_program_six_true != "correct":
            if making_program_six_true == "uncorrect_1":
                headOfDepartment "Вы неправильно сформировали результаты обучения."
                headOfDepartment "Формулировки результатов - это навыки, полученные студентом."
                headOfDepartment "Они короткие, содержат всего 7-9 слов."
            elif making_program_six_true == "uncorrect_2":
                headOfDepartment "Формулировки результатов обучения не следует копировать из рабочей программой дисциплины."
                headOfDepartment "Формулировки результатов - это навыки, полученные студентом."
                headOfDepartment "Они короткие, содержат всего 7-9 слов."
            elif making_program_six_true == "uncorrect_4":
                headOfDepartment "Формулировки результатов обучения - это навыки, полученные студентом."
                headOfDepartment "Они короткие, содержат всего 7-9 слов."

        if making_program_seven_true != "correct":
            if making_program_seven_true == "uncorrect_2":
                headOfDepartment "В содержании курса Вы зря указали страницы."
                headOfDepartment "Курс состоит из разделов (глав), подразделов (тем), и компонентов."
                headOfDepartment "Компоненты включают видеолекции и дополнительные материалы, а также тесты."
            elif making_program_seven_true == "uncorrect_3":
                headOfDepartment "Курс состоит не из недель, как Вы указали, а из разделов, каждый из которых равен 1 неделе."
                headOfDepartment "Раздел делится на темы, которые включают видеолекции, тесты и дополнительные материалы."
            elif making_program_seven_true == "uncorrect_4":
                headOfDepartment "Вы правильно указали структуру курса, но ошиблись в компонентах."
                headOfDepartment "Они включают видеолекции и дополнительные материалы, а также тесты."

        hide headOfDepartment
        show headOfDepartment funny at dslv(0.5)

        headOfDepartment "Все замечания исправлены, согласую. Не забудьте отправить все документы в Центр!"

        if sex == "male":
            male_player "Спасибо! Возвращаюсь к компьютеру!"
        else:
            female_player "Спасибо! Возвращаюсь к компьютеру!"

    window hide Dissolve(0.0)
    hide headOfDepartment with dissolve

    $ current_message = ("Екатерина", "Здравствуйте, [name]! Прошу Вас прислать программу, фотографию и список достижений. С уважением, Екатерина.")
    $ user_have_new_message = True # новое письмо
    $ user_need_to_read_mail = True # оно сюжетное

# Пока не пойдём домой
label technical_label_1_7_3:
    call screen department

    if _return == "exit":
        menu:
            "Остаться на кафедре":
                navigator "Екатерина ждёт Ваши документы. Поторопитесь."
                jump technical_label_1_7_3
            "Пойти в Центр":
                navigator "Лучше не затягивать с дальнейшей работой. Необходимые документы находятся дома."
                jump technical_label_1_7_3
            "Пойти домой":
                jump technical_label_1_8_1

# Мини-вступление перед прочтением письма
label technical_label_1_8_1:
    if pet == "cat":
        scene broken_home_with_cat with fade
    elif pet == "dog":
        scene broken_home_with_dog with fade

    $ flag_room_broken = True

    if sex == "male":
        male_player "Что тут произошло?!"
    else:
        female_player "Что тут произошло?!"

    navigator "Кажется, [pet_name] немного не расчитал силы, пока играл."
    navigator "Но сейчас не время отвлекаться на это! Давайте проверим почту, Екатерина должна была прислать перечень документов."

# Пока не прочтём письмо
label technical_label_1_8_1_1:

    if pet == "cat":
        scene broken_home_with_cat
    elif pet == "dog":
        scene broken_home_with_dog

    if flag_technical_label_1_8_1_1:
        call screen room with fade
    else:
        $ flag_technical_label_1_8_1_1 = True
        call screen room

    if _return == "open_computer":
        scene desktop_bg
        call screen computer with fade

        if _return == "close_computer":
            jump technical_label_1_8_1_1
        elif _return == "mail_checked":
            $ user_need_to_read_mail = False

            if pet == "cat":
                scene broken_home_with_cat with fade
            elif pet == "dog":
                scene broken_home_with_dog with fade

            navigator "Видимо, придётся отыскать необходимые документы среди этого беспорядка."
            jump finding_documents_1_8
    elif _return == "exit":
        $ flag_technical_label_1_8_1_1 = False
        menu:
            "Пойти в Центр":
                navigator "Вы ещё не ответили на письмо Екатерины."
            "Пойти на кафедру":
                navigator "Вам нужно собрать комплект документов дома."
            "Остаться дома":
                pass
        jump technical_label_1_8_1_1
    elif _return == "touch_pet":
        $ flag_technical_label_1_8_1_1 = False
        call touch_pet
        jump technical_label_1_8_1_1

# Мини-игра на поиск документов в комнате
label finding_documents_1_8:

    call screen find_all_documents with dissolve

    if _return == "finded_first":
        navigator "Вы нашли свою фотографию. Берём?"
        menu:
            "Да":
                navigator "Отлично, берём."
            "Нет":
                navigator "Предлагаю взять, иначе зачем Вы её тогда выбирали в альбоме?"

    elif _return == "finded_second":
        navigator "Это Ваша новая статья для научного журнала. Берём?"
        menu:
            "Да":
                navigator "Не рекоммендую. Екатерина её не просила."
            "Нет":
                navigator "Всё верно. Пока это не пригодится."

    elif _return == "finded_third":
        navigator "Вы нашли программу курса. Берём?"
        menu:
            "Да":
                navigator "Замечательно, берём."
            "Нет":
                navigator "Надо брать! Вы только что согласовали её с Заведующим кафедрой."

    elif _return == "finded_fourth":
        navigator "Это список Ваших достижений. Берём?"
        menu:
            "Да":
                navigator "Правильно, берём."
            "Нет":
                navigator "Лучше взять, Екатерина в письме упоминала его."

    elif _return == "finded_fifth":
        navigator "Вы нашли рецепт яблочного пирога. Берём?"
        menu:
            "Да":
                navigator "Лучше сохранить его для себя."
            "Нет":
                navigator "Всё верно. Убираем."

    # Пока всё не нашли
    if not (first_document_finded and second_document_finded and third_document_finded and fourth_document_finded and fifth_document_finded):
        jump finding_documents_1_8

    navigator "Отлично! Вы нашли все документы. Фото, программу и список достижений отправляю коллегам в Центр."
    navigator "Давайте здесь немного приберёмся."

    if sex == "male":
        male_player "Ты прав. Действуй!"
    else:
        female_player "Ты прав. Действуй!"

    if pet == "cat":
        scene home_with_cat with fade
    else:
        scene home_with_dog with fade

    if sex == "male":
        male_player "Теперь полный порядок. Можно двигаться дальше."
    else:
        female_player "Теперь полный порядок. Можно двигаться дальше."

    navigator "Хорошо. Давайте проверим, не пришёл ли Вам ответ из Центра."

    $ flag_room_broken = False # комната больше не сломана

    ### кнопка отправить ###
    $ current_message = ("Екатерина", "Добрый день, [name]! Ваши документы получили. Спасибо за оперативную работу! Ждем Вас у нас в Центре для обсуждения деталей. С уважением, куратор Екатерина")
    $ user_have_new_message = True # новое сообщение
    $ user_need_to_read_mail = True # оно сюжетное

# Пока не прочитаем письмо
label technical_label_1_8_2:

    if pet == "cat":
        scene home_with_cat
    else:
        scene home_with_dog

    if flag_technical_label_1_8_2:
        call screen room with fade
    else:
        $ flag_technical_label_1_8_2 = True
        call screen room

    if _return == "open_computer":
        scene desktop_bg
        call screen computer with fade

        if _return == "close_computer":
            jump technical_label_1_8_2
        elif _return == "mail_checked":
            $ user_need_to_read_mail = False
            jump technical_label_1_8_3
    elif _return == "exit":
        $ flag_technical_label_1_8_2 = False
        menu:
            "Пойти в Центр":
                navigator "Вы не получили подтверждения от Екатерины в письме."
            "Пойти на кафедру":
                navigator "Не торопитесь на кафедру. Сначала переговорите с Екатериной."
            "Остаться дома":
                pass
        jump technical_label_1_8_2
    elif _return == "touch_pet":
        $ flag_technical_label_1_8_2 = False
        call touch_pet
        jump technical_label_1_8_2

# Пока не пойдём в центр
label technical_label_1_8_3:

    if pet == "cat":
        scene home_with_cat
    else:
        scene home_with_dog

    if flag_technical_label_1_8_3:
        call screen room
    else:
        $ flag_technical_label_1_8_3 = True
        call screen room with fade

    if _return == "open_computer":
        scene desktop_bg
        call screen computer with fade

        if _return == "close_computer":
            $ flag_technical_label_1_8_3 = False
            jump technical_label_1_8_3

    elif _return == "exit":
        $ flag_technical_label_1_8_3 = True
        menu:
            "Пойти на кафедру":
                navigator "У Вас встреча с Екатериной в Центре."
                jump technical_label_1_8_3
            "Пойти в Центр":
                jump part_1_9
            "Остаться дома":
                navigator "Поторопитесь в Центр."
                jump technical_label_1_8_3
    elif _return == "touch_pet":
        $ flag_technical_label_1_8_3 = True
        call touch_pet
        jump technical_label_1_8_3

# балдёжный разговор с девочкой-вайфу Катенькой
label part_1_9:
    scene nots with fade

    show ekaterina funny with dissolve

    ekaterina "Здравствуйте, [name]!"

    if sex == "male":
        male_player "Здравствуйте, Екатерина!"
    else:
        female_player "Здравствуйте, Екатерина!"

    hide ekaterina
    show ekaterina normal_1 at dslv(0.94)

    ekaterina "Подскажите, как оформлены Ваши трудовые отношения с Университетом?"

    # Тут катя задаёт вопросы нам, а мы должны на них отвечать. В зависимости от правильности
    # Отображаются эмоции Кати. Вопросы разделены на две ветки: Трудовой договор/ГПХ - определяем тут же.
    menu:
        "Я работаю в университете по трудовому договору.":

            ekaterina "Вам оформляются доп. соглашение к трудовому договору и служебное задание."

            ekaterina "Давайте уточним основные юридические моменты."

            hide ekaterina
            show ekaterina normal_1 at dslv(0.9)

            ekaterina "Сколько времени нужно для создания онлайн-курса?"
            menu discission_in_1_9_part_1_1:

                "От 6 до 12 месяцев.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Не стоит растягивать работу на год, у Вас есть и другие задачи."
                    jump discission_in_1_9_part_1_1
                "От 3 до 6 месяцев.":
                    show ekaterina funny:
                        xalign 0.9015
                    ekaterina "Правильно. Это оптимальный срок проекта."
                "От 1 до 3 месяцев.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Чтобы сделать качественный онлайн-курс, этого времени недостаточно."
                    jump discission_in_1_9_part_1_1
                "От 2 недель до 1 месяца.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Вряд ли успеете! Выбирайте реалистичный вариант."
                    jump discission_in_1_9_part_1_1
                "Повторите, пожалуйста, вопрос.":
                    show ekaterina normal_1:
                        xalign 0.9
                    ekaterina "Сколько времени нужно для создания онлайн-курса?"
                    jump discission_in_1_9_part_1_1

            show ekaterina normal_1:
                xalign 0.9

            ekaterina "Какие документы НЕ оформляются для фиксации прав на онлайн-курс?"
            menu discission_in_1_9_part_1_2:

                "Служебное задание.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неверно. Это нужный документ."
                    jump discission_in_1_9_part_1_2
                "Дополнительное соглашение к трудовому договору.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Это нужный документ - в нём указывается конкретный онлайн-курс."
                    jump discission_in_1_9_part_1_2
                "Акт приема-передачи.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Вы ошиблись. Это нужный документ."
                    jump discission_in_1_9_part_1_2
                "Программа онлайн-курса.":
                    show ekaterina funny:
                        xalign 0.9015
                    ekaterina "Всё верно. Это методический, а не юридический документ."
                "Повторите, пожалуйста, вопрос.":
                    show ekaterina normal_1:
                        xalign 0.9
                    ekaterina "Какие документы НЕ оформляются для фиксации прав на онлайн-курс?"
                    jump discission_in_1_9_part_1_2

            show ekaterina normal_1:
                xalign 0.9

            ekaterina "Как распределяются права на онлайн-курс между автором и вузом?"
            menu discission_in_1_9_part_1_3:

                "Все права остаются у автора онлайн-курса.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Не совсем так. Исключительные права автор передаёт вузу."
                    jump discission_in_1_9_part_1_3
                "Неимущественные авторские права передаются вузу.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Право авторства, право на имя и целостность онлайн-курса принадлежат только автору."
                    jump discission_in_1_9_part_1_3
                "Исключительные права автор передает вузу.":
                    show ekaterina funny:
                        xalign 0.9015
                    ekaterina "Верно. Это нужно для размещения курса на внешней платформе."
                "Все права на онлайн-курс переходят к вузу.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неправильно. Авторские права сохраняются, а вузу передаются исключительные."
                    jump discission_in_1_9_part_1_3
                "Повторите, пожалуйста, вопрос.":
                    show ekaterina normal_1:
                        xalign 0.9
                    ekaterina "Как распределяются права на онлайн-курс между автором и вузом?"
                    jump discission_in_1_9_part_1_3

            show ekaterina normal_1:
                xalign 0.9

            ekaterina "Может ли автор использовать онлайн-курс для своей работы?"
            menu discission_in_1_9_part_1_4:

                "Может без ограничений.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неверно. Только для выполнения трудовых обязанностей в вузе. В иных случаях - по согласию вуза."
                    jump discission_in_1_9_part_1_4
                "Может, но есть ограничения.":
                    show ekaterina funny:
                        xalign 0.9015
                    ekaterina "Верно. Автор не вправе публиковать отдельные фрагменты онлайн-курса без согласия вуза."
                "Нет, не может.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Онлайн-курс - отличный помощник автору при проведении занятий в вузе."
                    jump discission_in_1_9_part_1_4
                "Не знаю.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Автор может использовать онлайн-курс для выполнения трудовых обязанностей в вузе."
                "Повторите, пожалуйста, вопрос.":
                    show ekaterina normal_1:
                        xalign 0.9
                    ekaterina "Может ли автор использовать онлайн-курс для своей работы?"
                    jump discission_in_1_9_part_1_4

            show ekaterina normal_1:
                xalign 0.9

            ekaterina "Какие задачи у руководителя авторского коллектива?"
            menu discission_in_1_9_part_1_5:

                "Несет ответственность за правовоую чистоту аудио-, видеоматериалов и тестов.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неверно. Ответственность за это несёт персонально каждый автор."
                    jump discission_in_1_9_part_1_5
                "Организует процесс согласования и подписания всех документов для онлайн-курса.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "У руководителя другие задачи. Все документы вместе с авторами готовит Центр."
                    jump discission_in_1_9_part_1_5
                "Организует работу коллектива и определяет доли персонального участия каждого автора.":
                    show ekaterina funny:
                        xalign 0.9015
                    ekaterina "Верно. Руководитель управляет коллективом в процессе создания онлайн-курса."
                "Контролирует внешний вид авторов перед каждой съемкой видеолекций.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Не совсем так. Внешний вид автора согласуется после прохождения тестовой съемки и остается неизменным."
                    jump discission_in_1_9_part_1_5
                "Повторите, пожалуйста, вопрос.":
                    show ekaterina normal_1:
                        xalign 0.9
                    ekaterina "Какие задачи у руководителя авторского коллектива?"
                    jump discission_in_1_9_part_1_5

            show ekaterina normal_1:
                xalign 0.9

            ekaterina "Где используется информация из регистрационной карты курса?"
            menu discission_in_1_9_part_1_6:

                "На странице сайта кафедры.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Там размещается другая информация."
                    jump discission_in_1_9_part_1_6
                "В каталоге курсов онлайн-платформы.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неверно. Информация в карточку на платформе вносится из программы онлайн-курса."
                    jump discission_in_1_9_part_1_6
                "На странице сайта Центра.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неточно. Информация на сайт вносится из программы онлайн-курса."
                    jump discission_in_1_9_part_1_6
                "В каталоге библиотеки вуза.":
                    show ekaterina funny:
                        xalign 0.9015
                    ekaterina "Правильно. На основе сведений регистрационной карты создается библиографическая запись."
                "Повторите, пожалуйста, вопрос.":
                    show ekaterina normal_1:
                        xalign 0.9
                    ekaterina "Где используется информация из регистрационной карты курса?"
                    jump discission_in_1_9_part_1_6

        "Я работаю в университете по договору ГПХ.":

            #show ekaterina normal_2:
            #    xalign 0.656

            ekaterina "Тогда Вы заключаете с университетом договор авторского заказа на создание онлайн-курса."

            ekaterina "Давайте уточним основные юридические моменты."

            hide ekaterina
            show ekaterina normal_1 at dslv(0.9)

            ekaterina "Чем Договор авторского заказа отличается от служебного задания?"
            menu discission_in_1_9_part_2_1:

                "Он содержит иной механизм оплаты вознаграждения авторам онлайн-курса.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неправильно. Для оплаты авторского вознаграждения используется один и тот же механизм."
                    jump discission_in_1_9_part_2_1
                "Он содержит иную технологию создания онлайн-курса.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неверно. Онлайн-курсы создаются по единой технологии."
                    jump discission_in_1_9_part_2_1
                "Он заключается с авторами на условиях договора гражданско-правового характера.":
                    show ekaterina funny:
                        xalign 0.9015
                    ekaterina "Правильно. Вы хорошо знаете правовую базу!"
                "Он жестко закрепляет права и обязанности руководителя авторского коллектива.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неправильно. Авторский коллектив самостоятельно распределяет работу и определяет функционал руководителя."
                    jump discission_in_1_9_part_2_1
                "Повторите, пожалуйста, вопрос.":
                    show ekaterina normal_1:
                        xalign 0.9
                    ekaterina "Чем Договор авторского заказа отличается от служебного задания?"
                    jump discission_in_1_9_part_2_1

            show ekaterina normal_1:
                xalign 0.9

            ekaterina "Каким образом происходит передача онлайн-курса Университету?"
            menu discission_in_1_9_part_2_2:

                "Издается приказ ректора о принятии онлайн-курса на баланс Университета.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неверно. Приказом ректора утверждается список онлайн-курсов, планируемых к созданию в течение учебного года."
                    jump discission_in_1_9_part_2_2
                "Подписывается дополнительное соглашение к трудовому договору.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неверно. В дополнительном соглашении не указывается конкретный онлайн-курс."
                    jump discission_in_1_9_part_2_2
                "Готовые материалы онлайн-курса отправляются на электронную почту.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Вы ошиблись. Использование электронной почты не является подтверждением передачи онлайн-курса."
                    jump discission_in_1_9_part_2_2
                "Подписывается Акт приёма-передачи онлайн-курса обеими сторонами.":
                    show ekaterina funny:
                        xalign 0.9015
                    ekaterina "Всё верно. Это завершающий очень важный документ."
                "Повторите, пожалуйста, вопрос.":
                    show ekaterina normal_1:
                        xalign 0.9
                    ekaterina "Каким образом происходит передача онлайн-курса Университету?"
                    jump discission_in_1_9_part_2_2

            show ekaterina normal_1:
                xalign 0.9

            ekaterina "Сколько раз можно переносить даты и время видеосъемок по инициативе автора?"
            menu discission_in_1_9_part_2_3:

                "Не более 2-х раз.":
                    show ekaterina funny:
                        xalign 0.9015
                    ekaterina "Правильно. И только по уважительной причине, подтверждённой документально."
                "Не более 4-х раз.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неверно. Видеолекций разных курсов много, и ресурсы студии нужно беречь."
                    jump discission_in_1_9_part_2_3
                "Ограничений нет.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Вы ошибаетесь. В команде есть оператор, он занят в разных проектах, и его время не безгранично."
                    jump discission_in_1_9_part_2_3
                "Не знаю.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Количество пропусков регламентировано. Рекомендую изучить документы на сайте в разделе \"Авторам\"."
                    jump discission_in_1_9_part_2_3
                "Повторите, пожалуйста, вопрос.":
                    show ekaterina normal_1:
                        xalign 0.9
                    ekaterina "Сколько раз можно переносить даты и время видеосъемок по инициативе автора?"
                    jump discission_in_1_9_part_2_3

            show ekaterina normal_1:
                xalign 0.9

            ekaterina "Что НЕ включает в себя служебное задание на создание онлайн-курса?"
            menu discission_in_1_9_part_2_4:

                "Результаты обучения.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неверно."
                    jump discission_in_1_9_part_2_4
                "Сроки выполнения работ.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Пока неправильно. Попробуйте еще раз!"
                    jump discission_in_1_9_part_2_4
                "Монтажные презентации.":
                    show ekaterina funny:
                        xalign 0.9015
                    ekaterina "Правильно. Они являются вспомогательным элементом для записи видеолекции."
                "Структура учебно-методических материалов.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неверно. Это трудное задание. Давайте еще раз!"
                    jump discission_in_1_9_part_2_4
                "Повторите, пожалуйста, вопрос.":
                    show ekaterina normal_1:
                        xalign 0.9
                    ekaterina "Что НЕ включает в себя служебное задание на создание онлайн-курса?"
                    jump discission_in_1_9_part_2_4

            show ekaterina normal_1:
                xalign 0.9

            ekaterina "Предоставляется ли автору льготный срок для исполнения служебного задания?"
            menu discission_in_1_9_part_2_5:
                "Да. Половина основного срока.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неправильно. Дополнительно предоставляется более короткий период."
                    jump discission_in_1_9_part_2_5
                "Да. Четверть основного срока.":
                    show ekaterina funny:
                        xalign 0.9015
                    ekaterina "Правильно. Такой срок предоставляется при необходимости и при наличии уважительных причин."
                "Да. Без ограничений.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Неверно. Максимальный срок создания онлайн-курса 6 месяцев. Льготный срок короче."
                    jump discission_in_1_9_part_2_5
                "Нет. Не предоставляется.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Как же так? В жизни много событий, и сложно выдержать жесткий график."
                    jump discission_in_1_9_part_2_5
                "Повторите, пожалуйста, вопрос.":
                    show ekaterina normal_1:
                        xalign 0.9
                    ekaterina "Предоставляется ли автору льготный срок для исполнения служебного задания?"
                    jump discission_in_1_9_part_2_5

            show ekaterina normal_1:
                xalign 0.9

            ekaterina "С помощью каких ресурсов автор устраняет недостатки созданного онлайн-курса?"
            menu discission_in_1_9_part_2_6:

                "Силами других преподавателей за счёт средств Университета.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Вы ошибаетесь. Это было бы слишком просто!"
                    jump discission_in_1_9_part_2_6
                "Своими силами за счёт средств Университета.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Не совсем так. Средства Университета для устранения недостатков не используются."
                    jump discission_in_1_9_part_2_6
                "Своими силами и за свой счёт.":
                    show ekaterina funny:
                        xalign 0.9015
                    ekaterina "Верно. Ответственность за качество онлайн-курса несёт его автор!"
                "Силами других преподавателей за их счёт.":
                    show ekaterina sad:
                        xalign 0.9015
                    ekaterina "Ваши коллеги готовы помочь, но опреативно исправить недостатки таким путём не получится."
                    jump discission_in_1_9_part_2_6
                "Повторите, пожалуйста, вопрос.":
                    show ekaterina normal_1:
                        xalign 0.9
                    ekaterina "С помощью каких ресурсов автор устраняет недостатки созданного онлайн-курса?"
                    jump discission_in_1_9_part_2_6


    hide ekaterina
    show ekaterina pry at dslv(0.5)

    ekaterina "Хорошая работа, [name]! Приступайте к подготовке материалов по курсу."

    if sex == "male":
        male_player "Спасибо, Екатерина! Всего доброго."
    elif sex == "female":
        female_player "Спасибо, Екатерина! Всего доброго."

    show ekaterina funny

    ekaterina "До свидания!"

    window hide Dissolve(0.0)
    hide ekaterina with dissolve

# Пока не пойдём домой
label technical_label_1_9:
    call screen nots

    if _return == "exit":
        menu:
            "Пойти на кафедру":
                navigator "Вам дали весьма объёмное задание. Лучше не затягивать с подготовкой материалов."
                jump technical_label_1_9
            "Остаться в Центре":
                navigator "Материалы удобнее собирать дома."
                jump technical_label_1_9
            "Пойти домой":
                jump conclusion_of_the_first_part

# Как только придём домой нас поздравляют с окончанием первой части
label conclusion_of_the_first_part:
    if pet == "cat":
        scene home_with_cat with fade
    elif pet == "dog":
        scene home_with_dog with fade

    navigator "Поздравляем! Вы прошли предварительный этап игры!"
    navigator "Добро пожаловать в следующий."
    navigator "Впереди несколько мини-игр, которые помогут развить навыки создания онлайн-курса."
    navigator "Прогресс прохождения отображается в компьютере."
    navigator "Не волнуйтесь, у Вас всё получится!"

    $ show_todo_icon = True # открывается иконка ту-ду листа в компьютере
    $ arrow_at_todo_icon = True # в первый раз на неё указывает стрелка

# Пока не нажмём на задания в ту-ду листе
label technical_label_2_1:
    if pet == "cat":
        scene home_with_cat
    elif pet == "dog":
        scene home_with_dog

    call screen room

    if _return == "open_computer":
        call screen computer

        if _return == "close_computer":
            jump technical_label_2_1
        ### выполнение мини-игр ###
        elif _return == "1":
            jump first_mini_game_production
        elif _return == "2":
            jump second_mini_game_production
        elif _return == "3":
            jump third_mini_game_production
        elif _return == "4":
            jump fourth_mini_game_production
        elif _return == "5":
            jump fifth_mini_game_production
        elif _return == "6":
            jump sixth_mini_game_production

    elif _return == "exit":
        menu:
            "Пойти на кафедру":
                navigator "Кажется, дома у Вас ещё остались незаконченные дела."
            "Пойти в Центр":
                navigator "Кажется, дома у Вас ещё остались незаконченные дела."
            "Остаться дома":
                pass
        jump technical_label_2_1
    elif _return == "touch_pet":
        call touch_pet
        jump technical_label_2_1

# Пока они пустые и нас просто возвращает обратно на technical_label_2_1

label first_mini_game_production:
    ""
    jump technical_label_2_1

label second_mini_game_production:
    ""
    jump technical_label_2_1

label third_mini_game_production:
    ""
    jump technical_label_2_1

label fourth_mini_game_production:
    ""
    jump technical_label_2_1

label fifth_mini_game_production:
    ""
    jump technical_label_2_1

label sixth_mini_game_production:
    ""
    jump technical_label_2_1
