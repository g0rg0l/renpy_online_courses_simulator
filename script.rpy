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
            $ arrow_at_close = False
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
    $arrow_at_door_in_department = True
    call screen department

    if _return == "exit":
        menu:
            "Остаться на кафедре":
                navigator "Вас уже ждут в Центре."
                jump technical_label_1_3
            "Пойти в Центр":
                $arrow_at_door_in_department = False
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
    $arrow_at_door_in_nots = True
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
                $arrow_at_door_in_nots = False
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
        call touch_pet from _call_touch_pet

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
        call touch_pet from _call_touch_pet_1
        jump technical_label_1_5_3
    elif _return == "open_album":
        $ arrow_at_album = False
        jump choosing_photo_1_5

# Запуск мини-игры с отбором фотографий в альбоме
label choosing_photo_1_5:

    scene album

    if sex == "female":
        if album_photos_selected_1:
            show wb_photo1F at Position(xpos = 235, ypos = 152, xanchor = 0, yanchor = 0)
        else:
            show default_photo1F at Position(xpos = 235, ypos = 152, xanchor = 0, yanchor = 0)

        if album_photos_selected_2:
            show wb_photo2F at Position(xpos = 597, ypos = 152, xanchor = 0, yanchor = 0)
        else:
            show default_photo2F at Position(xpos = 597, ypos = 152, xanchor = 0, yanchor = 0)

        if album_photos_selected_3:
            show wb_photo3F at Position(xpos = 412, ypos = 561, xanchor = 0, yanchor = 0)
        else:
            show default_photo3F at Position(xpos = 412, ypos = 561, xanchor = 0, yanchor = 0)
            
        if album_photos_selected_4:
            show wb_photo4F at Position(xpos = 970, ypos = 152, xanchor = 0, yanchor = 0)
        else:
            show default_photo4F at Position(xpos = 970, ypos = 152, xanchor = 0, yanchor = 0)

        if album_photos_selected_5:
            show wb_photo5F at Position(xpos = 1328, ypos = 152, xanchor = 0, yanchor = 0)
        else:
            show default_photo5F at Position(xpos = 1328, ypos = 152, xanchor = 0, yanchor = 0)

        if album_photos_selected_6:
            show wb_photo6F at Position(xpos = 1048, ypos = 561, xanchor = 0, yanchor = 0)
        else:
            show default_photo6F at Position(xpos = 1048, ypos = 561, xanchor = 0, yanchor = 0)
    else:
        if album_photos_selected_1:
            show wb_photo1M at Position(xpos = 235, ypos = 152, xanchor = 0, yanchor = 0)
        else:
            show default_photo1M at Position(xpos = 235, ypos = 152, xanchor = 0, yanchor = 0)

        if album_photos_selected_2:
            show wb_photo2M at Position(xpos = 597, ypos = 152, xanchor = 0, yanchor = 0)
        else:
            show default_photo2M at Position(xpos = 597, ypos = 152, xanchor = 0, yanchor = 0)

        if album_photos_selected_3:
            show wb_photo3M at Position(xpos = 412, ypos = 561, xanchor = 0, yanchor = 0)
        else:
            show default_photo3M at Position(xpos = 412, ypos = 561, xanchor = 0, yanchor = 0)
            
        if album_photos_selected_4:
            show wb_photo4M at Position(xpos = 970, ypos = 152, xanchor = 0, yanchor = 0)
        else:
            show default_photo4M at Position(xpos = 970, ypos = 152, xanchor = 0, yanchor = 0)

        if album_photos_selected_5:
            show wb_photo5M at Position(xpos = 1328, ypos = 152, xanchor = 0, yanchor = 0)
        else:
            show default_photo5M at Position(xpos = 1328, ypos = 152, xanchor = 0, yanchor = 0)

        if album_photos_selected_6:
            show wb_photo6M at Position(xpos = 1048, ypos = 561, xanchor = 0, yanchor = 0)
        else:
            show default_photo6M at Position(xpos = 1048, ypos = 561, xanchor = 0, yanchor = 0)
    
    call screen album

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
        if pet == "cat":
            scene home_with_cat with fade
        elif pet == "dog":
            scene home_with_dog with fade

        navigator "Стоит проверить почту. Возможно, Екатерина прислала необходимые документы."

        $ flag_room_album_opened = False # на альбом больше нельзя нажать
        $ current_message = ("Екатерина", "Здравствуйте, [name]! В продолжение разговора отправляю Вам шаблон программы онлайн-курса. Желаю удачи! С уважением, куратор Екатерина")
        $ user_have_new_message = True # пришло письмо
        $ user_need_to_read_mail = True # оно сюжетное
        $ show_file_to_make_programm = True # показать иконку "приложенный файл" в письме
        $ arrow_at_computer = True # стрелка на пк

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
        $ arrow_at_computer = False
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
        call touch_pet from _call_touch_pet_2
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
        call touch_pet from _call_touch_pet_3
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
        call touch_pet from _call_touch_pet_4
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
                headOfDepartment "Для онлайн-курса не рекомендуется копировать цель из рабочей программы дисциплины."
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
                headOfDepartment "Например, для студентов-иностранцев рекомендуется разрабатывать курс на понятном им языке."
            elif making_program_five_true == "uncorrect_3":
                headOfDepartment "Выбор языка, на котором будет читаться курс, делает кафедра, ответственная за его реализацию."
                headOfDepartment "Если он рассчитан на иностранных студентов, то рекомендуется разрабатывать курс на понятном им языке."
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
        call touch_pet from _call_touch_pet_5
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
                navigator "Не рекомендую. Екатерина её не просила."
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
        call touch_pet from _call_touch_pet_6
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
        call touch_pet from _call_touch_pet_7
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
        call touch_pet from _call_touch_pet_8
        jump technical_label_2_1


label technical_label_5_5:
    if pet == "cat":
        scene home_with_cat
    elif pet == "dog":
        scene home_with_dog

    call screen computer with fade

    if _return == "close_computer":
        jump technical_label_2_1
    ### выполнение мини-игр ###
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



################## 2 #######################


label second_mini_game_production:   ####   Мини-игра "Текст" ####
    scene text_normal with fade
    navigator "Отлично, [name], что Вы решили проверить свои навыки в работе с текстом."
    navigator "Писать тексты для онлайн-курса нужно в информационном стиле."
    navigator "Вырезайте из текста только лишние слова и фразы. Сокращайте путь читателя к основной мысли."
    navigator "Сейчас проверим текст на читаемость. Вам нужно найти 12 стоп-слов и словосочетаний."
    navigator "Однако будьте внимательны, у Вас всего 2 попытки. Удачи!"
    jump mini_game_text

label mini_game_text:
    call screen text_mini_game
    if _return == "" or _return == "T":
        jump mini_game_text
    if _return == "proverka":
        if right_choise == 12:
            navigator "Это победа! Вы профи. Спасибо за игру!"
            $game_vin = True
            jump text_mini_game_final
        if popitki < 3: 
            navigator "Вы нашли [right_choise] из 12 стоп-слов. Попробуйте еще раз."
            jump mini_game_text
        elif right_choise == 0:
            navigator "[right_choise] из 12 стоп-слов. Все ошибаются :)). Нестрашно."
            jump text_mini_game_final
        elif right_choise == 1:
            navigator "[right_choise] из 12 стоп-слов. Не падайте духом!."
            jump text_mini_game_final
        elif right_choise == 2:
            navigator "[right_choise] из 12 стоп-слов. Верьте в себя и свои силы!"
            jump text_mini_game_final
        elif right_choise == 3:
            navigator "[right_choise] из 12 стоп-слов. Дорога к успеху трудна. Но Вы справитесь!"
            jump text_mini_game_final
        elif right_choise == 4:
            navigator "[right_choise] из 12 стоп-слов. Вам надо тренироваться!"
            jump text_mini_game_final
        elif right_choise == 5:
            navigator "[right_choise] из 12 стоп-слов. Это было красиво :) Вы молодец!"
            jump text_mini_game_final
        elif right_choise == 6:
            navigator "[right_choise] из 12 стоп-слов. Вы очень хорошо постарались!"
            jump text_mini_game_final
        elif right_choise == 7:
            navigator "[right_choise] из 12 стоп-слов. Поразительно! Вы нашли больше половины стоп-слов."
            jump text_mini_game_final
        elif right_choise == 8:
            navigator "[right_choise] из 12 стоп-слов. Вы лучше всех! Жаль, что не всё нашлось."
            jump text_mini_game_final
        elif right_choise == 9:
            navigator "[right_choise] из 12 стоп-слов. Мы здорово проводим время вместе :) Вы не нашли всего 3  стоп-слова."
            jump text_mini_game_final
        elif right_choise == 10:
            navigator "[right_choise] из 12 стоп-слов. Ваши знания восхищают! Вы не нашли всего 2 стоп-слова."
            jump text_mini_game_final
        elif right_choise == 11:
            navigator "[right_choise] из 12 стоп-слов. Почти в яблочко! Вы были в шаге от победы."
            jump text_mini_game_final

label text_mini_game_final:
    $lst2[2] = True
    $lst2[7] = True
    $lst2[11] = True
    $lst2[35] = True
    $lst2[50] = True
    $lst2[56] = True
    $lst2[59] = True
    $lst2[67] = True
    $lst2[81] = True
    $lst2[86] = True
    $lst2[99] = True
    $lst2[104] = True

    $game_over = True
    if game_finish:
        call screen text_mini_game
        if (_return == "exit"):
            jump technical_label_5_5
        else:
            jump text_mini_game_final    
    else:
        if game_vin == False:
            navigator "Взгляните сначала на правильные варианты ответов и, чтобы закрыть игру, нажмите на крестик в правом верхнем углу."
        else:
            navigator "Чтобы закрыть игру нажмите на крестик в правом верхнем углу."
        $game_finish = True
        $todo_two_colmpleted = True
        jump text_mini_game_final



################## 3 #######################


label third_mini_game_production: #### Мини-игра "Авторское право" ####
    jump copyright_law_start

label copyright_law_start:
    scene copyright_law with fade

    navigator "У каждого текста и иллюстрации есть автор. Его творчество охраняется авторскими правами."
    navigator "Это цифровые лицензии. По комбинации значков и аббревиатур сразу понятно, как можно использовать произведение."
    navigator "Все эти лицензии неисключительные, бессрочные, действуют для всех, везде и применяются ко всем одинаково."
    navigator "Давайте проверим как Вы разбираетесь в лицензиях."
    navigator "Перед Вами картинки. Подберите каждой картике разрешенное условие ее использования."
    navigator "Будьте внимательны. У вас есть по 3 попытки на каждом уровне. Удачи!"
    
    jump copyright_law_game

label copyright_law_game: #авторское право
    if(first_game_copyright):
        $ first_game_copyright = False
        call screen copyright_law with dissolve
        if copyright_progress == 1:
            scene copyright_law
            show text1_image at Position(xpos = 680, ypos =  700, xanchor = 0, yanchor = 0)
            show text2_image at Position(xpos = 1302, ypos = 700, xanchor = 0, yanchor = 0)
            show text3_image at Position(xpos = 58, ypos = 700, xanchor = 0, yanchor = 0)
        else:
            scene copyright_law2
            show text4_image at Position(xpos = 1305, ypos =  700, xanchor = 0, yanchor = 0)
            show text5_image at Position(xpos = 60, ypos = 700, xanchor = 0, yanchor = 0)
            show text6_image at Position(xpos = 683, ypos = 700, xanchor = 0, yanchor = 0)
    else:
        #проверка полей на заполненность
        python:
            for check_full_ans in range(1, 4): #перебираем все поля ответов
                check_full = False
                for check_full_txt in range(1, 4): #перебираем все текстовые таблички
                    if text_position[check_full_txt][0] == answer_position[check_full_ans][0] and text_position[check_full_txt][1] == answer_position[check_full_ans][1]:
                        check_full = True
                answer_full[check_full_ans] = check_full
        call screen copyright_law

    if (isinstance(_return, str)): #проверка строковых вариантов

        if _return == "text_reset1" or _return == "text_reset2" or _return == "text_reset3": #проверка вариантов с перетаскиванием "в никуда"
            $ char_return = [char for char in _return]
            $ text_position[int(char_return[10])][0] = 0
            $ text_position[int(char_return[10])][1] = 0

        elif _return == "next_level":
            if(answer_correct[1] and answer_correct[2] and answer_correct[3]):
                $ count_of_mistakes = 0
                if copyright_progress == 1:
                    navigator "Замечательно! Так держать!"
                    python:
                        for a in range(1, 4):
                            text_position[a][0] = 0
                            text_position[a][1] = 0
                            answer_full[a] = False
                            answer_correct[a] = False
                        default_position = [0, 1305, 60, 683]
                        answer_position = [[0, 0], [60, 506], [683, 507], [1305, 507]]
                        copyright_progress += 1
                        first_game_copyright = True 
                else:
                    scene copyright_law_answers2
                    navigator "В яблочко! Всё правильно."
                    navigator "Итак, основные виды лицензий мы повторили. Можно двигаться дальше."
                    $todo_three_colmpleted = True
                    call screen copyright_final
                    if _return == "exit":
                        jump technical_label_5_5
            else:
                if(count_of_mistakes == 0):
                    $ count_of_mistakes += 1
                    navigator "Немного не так. Попробуйте ещё раз!"
                elif(count_of_mistakes == 1):
                    $ count_of_mistakes += 1
                    navigator "Не совсем так. Подумайте!"
                else:
                    if(copyright_progress == 1):
                        navigator "Не расстраивайтесь, бывает. Давайте узнаем правильные ответы."
                        scene copyright_law_answers1 with dissolve
                        navigator "При лицензии CC BY можем распространять, редактировать, брать за основу, использовать."
                        navigator "При лицензии CC BY-SA можем редактировать, но распространять будем на условиях этой же лицензии."
                        navigator "При лицензии CC BY-NC можем распространять, но только в исходном виде. Редактирование запрещено."
                        python:
                            for a in range(1, 4):
                                text_position[a][0] = 0
                                text_position[a][1] = 0
                                answer_full[a] = False
                                answer_correct[a] = False
                            default_position = [0, 1305, 60, 683]
                            answer_position = [[0, 0], [60, 506], [683, 507], [1305, 507]]
                            copyright_progress += 1
                            count_of_mistakes = 0
                            first_game_copyright = True 
                    else:
                        navigator "В следующий раз повезёт! А вот и правильные ответы."
                        scene copyright_law_answers2 with dissolve
                        navigator "При лицензии CC BY-NC можем редактировать, но распространять будем только в некоммерческих целях."
                        navigator "При лицензии CC BY-NC-ND не можем без согласия автора редактировать и распространять в коммерческих целях."
                        navigator "При лицензии CC BY 0 можем свободно использовать без ограничений, не спрашивая разрешения у автора."
                        scene copyright_law_answers2 with dissolve
                        navigator "Итак, основные виды лицензий мы повторили. Можно двигаться дальше."
                        $todo_three_colmpleted = True
                        call screen copyright_final
                        if _return == "exit":
                            jump technical_label_5_5
                    
                python:
                    for a in range(1, 4):
                        text_position[a][0] = 0
                        text_position[a][1] = 0
                jump copyright_law_game
        elif _return == "open_help":
            jump copyright_help_page

    else: #проверка ответов в полях
        $ answer_num = _return[0]
        $ text_num = _return[1]
        $ answer_full[answer_num] = True
        $ text_position[text_num][0] = answer_position[answer_num][0]
        $ text_position[text_num][1] = answer_position[answer_num][1]
        if answer_num == text_num:
            $ answer_correct[answer_num] = True
        else:
            $ answer_correct[answer_num] = False

    jump copyright_law_game


label copyright_help_page:
    call screen copyright_help_page

    if _return == "return_to_game":
        python:
            for a in range(1, 4):
                text_position[a][0] = 0
                text_position[a][1] = 0
        jump copyright_law_game



################## 4 #######################



label fourth_mini_game_production:  ####   Мини-игра "Презентации" ####
    jump presentation1

label presentation1:
    if flag_presentation1 == False:
        scene 1_wrong with Fade(0.3, 0.0, 0.3)
        navigator "Ой, ошибки на слайдах, найдите их."
        navigator "Постарайтесь не ошибаться. У вас есть по 2 попытки на каждый слайд."
    else:
        scene 1_wrong
    call screen first_presentation
    if (k == 2):
        scene 1_right with dissolve
        navigator "Здесь была ошибка выравнивания. Не забывайте выровнять элементы по левому краю."
    elif (_return == "exit"):
        $flag_presentation1 = True
        navigator "Вы не закончили. Осталось еще немного."
        jump presentation1
    elif (_return == "viravnivanie"):
        scene 1_right with dissolve
        navigator "Верно!  Обязательно выравнивайте элементы по левому краю."
    else:
        if sex == "male":
            navigator "Вы внимательный! Но есть более серьезная ошибка. Поищите еще!"
        else:
            navigator "Вы внимательная! Но есть более серьезная ошибка. Поищите еще!"
        $flag_presentation1 = True
        jump presentation1
    $k = 0
    jump presentation2

label presentation2:
    if flag_presentation2 == False:
        scene 2_wrong with Fade(0.3, 0.0, 0.3)
    else:
        scene 2_wrong

    call screen second_presentation
    if (k == 2):
        show 2_right with dissolve
        navigator "Градиент не используйте. Без него гораздо лучше."
    elif (_return == "exit"):
        $flag_presentation2 = True
        navigator "Вы не закончили. Осталось еще немного."
        jump presentation2
    elif (_return == "gradient"):
        show 2_right with dissolve
        navigator "Вы правы!"
    else:
        navigator "Ошибка на поверхности! Давайте еще разок!"
        $flag_presentation2 = True
        jump presentation2
    $k = 0
    jump presentation3

label presentation3:
    if flag_presentation3 == False:
        scene 3_wrong with Fade(0.3, 0.0, 0.3)
    else:
        scene 3_wrong

    call screen third_presentation
    if (k == 2):
        show 3_right with dissolve
        navigator "Это была ошибка \"Количество текта\". Нужно с ней бороться всегда и везде!"
    elif (_return == "exit"):
        $flag_presentation3 = True
        navigator "Вы не закончили. Осталось еще немного."
        jump presentation3
    elif (_return == "kolichestvo_texta"):
        show 3_right with dissolve
        navigator "Конечно! Стену текста нужно убрать"
    else:
        navigator "Попробуйте другой вариант."
        $flag_presentation3 = True
        jump presentation3
    $k = 0
    jump presentation4

label presentation4:
    if flag_presentation4 == False:
        scene 4_wrong with Fade(0.3, 0.0, 0.3)
    else:
        scene 4_wrong

    call screen fouth_presentation
    if (k == 2):
        show 4_right with dissolve
        navigator "Здесь много лишних рисунков без связи с текстом и висячий предлог."
    elif (_return == "exit"):
        $flag_presentation4 = True
        navigator "Вы не закончили. Осталось еще немного."
        jump presentation4
    elif (_return == "lishnie_elementi"):
        show 4_right with dissolve
        navigator "Отлично! Ключевая ошибка найдена!"
    else:
        navigator "Неудачный выбор! Давайте по новой."
        $flag_presentation4 = True
        jump presentation4
    $k = 0
    jump presentation5

label presentation5:
    if flag_presentation5 == False:
        scene 5_wrong with Fade(0.3, 0.0, 0.3)
    else:
        scene 5_wrong

    call screen fifth_presentation
    if (k == 2):
        show 5_right with dissolve
        navigator "На слайде нарушена иерархия. Акцент сделан на вводную фразу, а не на основной текст."
    elif (_return == "exit"):
        $flag_presentation5 = True
        navigator "Вы не закончили. Осталось еще немного."
        jump presentation5
    elif (_return == "narushenie_ierarhii"):
        show 5_right with dissolve
        navigator "Замечательно! Вы молодец!"
    else:
        navigator "Это сложная ошибка. Подумайте!"
        $flag_presentation5 = True
        jump presentation5
    $k = 0
    jump presentation6

label presentation6:
    if flag_presentation6 == False:
        scene 6_wrong with Fade(0.3, 0.0, 0.3)
    else:
        scene 6_wrong

    call screen six_presentation
    if (k == 2):
        scene 6_right with dissolve
        navigator "Неправильно оформлена выноска с репликой персонажа."
    elif (_return == "exit"):
        $flag_presentation6 = True
        navigator "Вы не закончили. Осталось еще немного."
        jump presentation6
    elif (_return == "oformlenie_vinosok"):
        scene 6_right with dissolve
        navigator "Согласен с Вами, оранжевая выноска - неудачное решение."
    else:
        navigator "Здесь всё очевидно! Не торопитесь!"
        $flag_presentation6 = True
        jump presentation6
    $k = 0
    jump presentation7

label presentation7:
    if flag_presentation7 == False:
        scene 7_wrong with Fade(0.3, 0.0, 0.3)
    else:
        scene 7_wrong

    call screen seven_presentation
    if (k == 2):
        scene 7_right with dissolve
        navigator "Здесь была ошибка в оформлении текста. Теперь весь текст хорошо читается."
    elif (_return == "exit"):
        $flag_presentation7 = True
        navigator "Вы не закончили. Осталось еще немного."
        jump presentation7
    elif (_return == "oformlenie_texta"):
        scene 7_right with dissolve
        navigator "Правильно! Текст должно быть хорошо видно."
    else:
        navigator "Не то. Попробуйте еще раз!"
        $flag_presentation7 = True
        jump presentation7
    $k = 0
    jump presentation8

label presentation8:
    if flag_presentation8 == False:
        scene 8_wrong with Fade(0.3, 0.0, 0.3)
    else:
        scene 8_wrong

    call screen eight_presentation
    if (k == 2):
        scene 8_right with dissolve
        navigator "Здесь было нарушено правило приближения. Не забывайте про \"воздух\" на слайдах!"
    elif (_return == "exit"):
        $flag_presentation8 = True
        navigator "Вы не закончили. Осталось еще немного."
        jump presentation8
    elif (_return == "pravilo_priblizhenia"):
        scene 8_right with dissolve
        navigator "Да, Вы правы! Между элементами должен быть \"воздух\"."
    else:
        navigator "Вы уже близко к разгадке. Не останавливайтесь!"
        $flag_presentation8 = True
        jump presentation8
    $k = 0
    jump presentation9

label presentation9:
    if flag_presentation9 == False:
        scene 9_wrong with Fade(0.3, 0.0, 0.3)
    else:
        scene 9_wrong

    call screen nine_presentation
    if (k == 2):
        scene 9_right with dissolve
        navigator "Видите как изменился текст в плашках? Он поместился целиком."
    elif (_return == "exit"):
        $flag_presentation9 = True
        navigator "Вы не закончили. Осталось еще немного."
        jump presentation9
    elif (_return == "oformlenie_plashek"):
        scene 9_right with dissolve
        navigator "Точно! Текст должен помещаться в плашки целиком."
    else:
        navigator "Тут другая ошибка. Посмотрите внимательно!"
        $flag_presentation9 = True
        jump presentation9
    $k = 0
    jump presentation10

label presentation10:
    if flag_presentation10 == False:
        scene 10_wrong with Fade(0.3, 0.0, 0.3)
    else:
        scene 10_wrong

    call screen ten_presentation
    if (k == 2):
        scene 10_right with dissolve
        navigator "Тут разная стилистика элементов. Это плохо смотрится на видео."
    elif (_return == "exit"):
        $flag_presentation10 = True
        navigator "Вы не закончили. Осталось еще немного."
        jump presentation10
    elif (_return == "raznaya_stilistika"):
        scene 10_right with dissolve
        navigator "Абсолютно верно! Иконки разного стиля"
    else:
        navigator "Это непросто, приглядитесь повнимательнее!"
        $flag_presentation10 = True
        jump presentation10
    $k = 0
    jump presentation11

label presentation11:
    if flag_presentation11 == False:
        scene 11_wrong with Fade(0.3, 0.0, 0.3)
    else:
        scene 11_wrong

    call screen eleven_presentation
    if (k == 2):
        scene 11_right with dissolve
        navigator "Копирование из Интернета может нарушить чужие авторские права."
    elif (_return == "exit"):
        $flag_presentation11 = True
        navigator "Вы не закончили. Осталось еще немного."
        jump presentation11
    elif (_return == "3D_effects"):
        scene 11_right with dissolve
        navigator "Да, копировать из Интернета схемы и рисунки нельзя."
    else:
        navigator "Нет, тут дело в другом."
        $flag_presentation11 = True
        jump presentation11 
    navigator "Спасибо [name]! Вы справились, теперь в презентациях нет ошибок."
    navigator "Чтобы выйти, нажмите на крестик в правом верхнем углу."
    jump final_presentations

label final_presentations:
    $todo_four_colmpleted = True
    scene 11_right
    call screen final_for_presentations
    if (_return == "exit"):
        jump technical_label_5_5
    else:
        jump final_presentations



################## 5 #######################


#### мини-игра гардероб ####


label fifth_mini_game_production:

    $flag_room_cupboard_opened = True
    $arrow_at_cupboard = True

    if flag_fifth_mini_game == False:
        navigator "Пришло время подобрать одежду для съемок. Кажется, она находится в шкафу."

    call screen room
    if _return != "open_cupboard":
        navigator "Нажмите на шкаф чтобы продолжить игру."
        $flag_fifth_mini_game = True
        jump fifth_mini_game_production
    else:
        scene wardrobe_bg with fade
        navigator "Чтобы перетащить элемент одежды, нажмите по нему мышкой и удерживайте."
        if sex == "female":
            jump wardrobe_game_f
        else:
            jump wardrobe_game_m


label wardrobe_game_f:
    
    scene wardrobe_bg

    show bottom1f at Position(xpos = bottom_position_f[1][0], ypos = bottom_position_f[1][1], xanchor = 0, yanchor = 0)
    show bottom2f at Position(xpos = bottom_position_f[2][0], ypos = bottom_position_f[2][1], xanchor = 0, yanchor = 0)
    show bottom3f at Position(xpos = bottom_position_f[3][0], ypos = bottom_position_f[3][1], xanchor = 0, yanchor = 0)
    show bottom4f at Position(xpos = bottom_position_f[4][0], ypos = bottom_position_f[4][1], xanchor = 0, yanchor = 0)
    show bottom5f at Position(xpos = bottom_position_f[5][0], ypos = bottom_position_f[5][1], xanchor = 0, yanchor = 0)

    show top1f at Position(xpos = top_position_f[1][0], ypos = top_position_f[1][1], xanchor = 0, yanchor = 0)
    show top2f at Position(xpos = top_position_f[2][0], ypos = top_position_f[2][1], xanchor = 0, yanchor = 0)
    show top3f at Position(xpos = top_position_f[3][0], ypos = top_position_f[3][1], xanchor = 0, yanchor = 0)
    show top4f at Position(xpos = top_position_f[4][0], ypos = top_position_f[4][1], xanchor = 0, yanchor = 0)
    show top5f at Position(xpos = top_position_f[5][0], ypos = top_position_f[5][1], xanchor = 0, yanchor = 0)
    show top6f at Position(xpos = top_position_f[6][0], ypos = top_position_f[6][1], xanchor = 0, yanchor = 0)

    show boots4f at Position(xpos = boots_position_f[4][0], ypos = boots_position_f[4][1], xanchor = 0, yanchor = 0)
    show boots3f at Position(xpos = boots_position_f[3][0], ypos = boots_position_f[3][1], xanchor = 0, yanchor = 0)
    show boots2f at Position(xpos = boots_position_f[2][0], ypos = boots_position_f[2][1], xanchor = 0, yanchor = 0)
    show boots1f at Position(xpos = boots_position_f[1][0], ypos = boots_position_f[1][1], xanchor = 0, yanchor = 0)

    if first_game_wardrobe:
        call screen WardrobeScreenF with dissolve
        $ first_game_wardrobe = False
    else:
        call screen WardrobeScreenF
    
    python:

        correct_answer = False
        char_return = [char for char in _return]
        return_len = int(len(char_return))
        num1 = int(char_return[0])
        num2 = int(char_return[return_len-1])

        if num1 == 1: #верх
            if num2 == 2: #платье
                correct_answer = True
                update_garment_image(num1, num2)
                clear_garments(1)
                clear_garments(2)
            elif num2 == 3: #блуза
                correct_answer = True
                update_garment_image(num1, num2)
                clear_garments(1)
                clear_garments(4)
            if correct_answer: #если верно
                top_position_f[num2][0] = model_top_position_f[num2][0]
                top_position_f[num2][1] = model_top_position_f[num2][1]
                top_ready[num2] = True
            
        elif num1 == 2: #низ
            if num2 == 2 or num2 == 4: #коричневая юбка или серая юбка
                correct_answer = True
                update_garment_image(num1, num2)
                clear_garments(2)
                clear_garments(4)
                bottom_position_f[num2][0] = model_bottom_position_f[num2][0]
                bottom_position_f[num2][1] = model_bottom_position_f[num2][1]
                bottom_ready[num2] = True

        elif num1 == 3: #обувь
            if num2 == 2 or num2 == 3: #туфли или кроссовки
                correct_answer = True
                update_garment_image(num1, num2)
                clear_garments(3)
                boots_position_f[num2][0] = model_boots_position_f[num2][0]
                boots_position_f[num2][1] = model_boots_position_f[num2][1]
                boots_ready[num2] = True
        
        navigator(navigator_str_f[_return]) 
        if not correct_answer:
            clear_garments(num1)      
    
    $ check1 = top_ready[2] and boots_ready[2]
    $ check2 = top_ready[2] and boots_ready[3]
    $ check3 = top_ready[3] and bottom_ready[2] and boots_ready[2]
    $ check4 = top_ready[3] and bottom_ready[2] and boots_ready[3]
    $ check5 = top_ready[3] and bottom_ready[4] and boots_ready[2]
    $ check6 = top_ready[3] and bottom_ready[4] and boots_ready[3]

    if check1 or check2 or check3 or check4 or check5 or check6:
        navigator "С одеждой решили. Теперь прическа, аксессуары и макияж. Вперед, к зеркалу!"
        jump mirror_game_f
    
    jump wardrobe_game_f


label wardrobe_game_m:
    
    scene wardrobe_bg

    show boots4m at Position(xpos = boots_position_m[4][0], ypos = boots_position_m[4][1], xanchor = 0, yanchor = 0)
    show boots3m at Position(xpos = boots_position_m[3][0], ypos = boots_position_m[3][1], xanchor = 0, yanchor = 0)
    show boots2m at Position(xpos = boots_position_m[2][0], ypos = boots_position_m[2][1], xanchor = 0, yanchor = 0)
    show boots1m at Position(xpos = boots_position_m[1][0], ypos = boots_position_m[1][1], xanchor = 0, yanchor = 0)

    show bottom1m at Position(xpos = bottom_position_m[1][0], ypos = bottom_position_m[1][1], xanchor = 0, yanchor = 0)
    show bottom2m at Position(xpos = bottom_position_m[2][0], ypos = bottom_position_m[2][1], xanchor = 0, yanchor = 0)
    show bottom3m at Position(xpos = bottom_position_m[3][0], ypos = bottom_position_m[3][1], xanchor = 0, yanchor = 0)
    show bottom4m at Position(xpos = bottom_position_m[4][0], ypos = bottom_position_m[4][1], xanchor = 0, yanchor = 0)

    show top1m at Position(xpos = top_position_m[1][0], ypos = top_position_m[1][1], xanchor = 0, yanchor = 0)
    show top2m at Position(xpos = top_position_m[2][0], ypos = top_position_m[2][1], xanchor = 0, yanchor = 0)
    show top3m at Position(xpos = top_position_m[3][0], ypos = top_position_m[3][1], xanchor = 0, yanchor = 0)
    show top4m at Position(xpos = top_position_m[4][0], ypos = top_position_m[4][1], xanchor = 0, yanchor = 0)
    show top5m at Position(xpos = top_position_m[5][0], ypos = top_position_m[5][1], xanchor = 0, yanchor = 0)

    if first_game_wardrobe:
        call screen WardrobeScreenM with dissolve
        $ first_game_wardrobe = False
    else:
        call screen WardrobeScreenM
    
    python:

        correct_answer = False
        char_return = [char for char in _return]
        return_len = int(len(char_return))
        num1 = int(char_return[0])
        num2 = int(char_return[return_len-1])

        if num1 == 1: #верх
            if num2 == 3 or num2 == 4:
                correct_answer = True
                update_garment_image_m(num1, num2)
                clear_garments_m(1)
                top_position_m[num2][0] = model_top_position_m[num2][0]
                top_position_m[num2][1] = model_top_position_m[num2][1]
                top_ready[num2] = True

        elif num1 == 2: #низ
            if num2 == 1 or num2 == 2:
                correct_answer = True
                update_garment_image_m(num1, num2)
                clear_garments_m(2)
                bottom_position_m[num2][0] = model_bottom_position_m[num2][0]
                bottom_position_m[num2][1] = model_bottom_position_m[num2][1]
                bottom_ready[num2] = True
        
        elif num1 == 3: #обувь
            if num2 == 1 or num2 == 2:
                correct_answer = True
                update_garment_image_m(num1, num2)
                clear_garments_m(3)
                boots_position_m[num2][0] = model_boots_position_m[num2][0]
                boots_position_m[num2][1] = model_boots_position_m[num2][1]
                boots_ready[num2] = True

        navigator(navigator_str_m[_return])
        if not correct_answer:
            clear_garments_m(num1)  

    $ check1 = top_ready[3] and bottom_ready[1] and boots_ready[1]
    $ check2 = top_ready[3] and bottom_ready[1] and boots_ready[2]
    $ check3 = top_ready[3] and bottom_ready[2] and boots_ready[1]
    $ check4 = top_ready[3] and bottom_ready[2] and boots_ready[2]
    $ check5 = top_ready[4] and bottom_ready[1] and boots_ready[1]
    $ check6 = top_ready[4] and bottom_ready[1] and boots_ready[2]
    $ check7 = top_ready[4] and bottom_ready[2] and boots_ready[1]
    $ check8 = top_ready[4] and bottom_ready[2] and boots_ready[2]

    if check1 or check2 or check3 or check4 or check5 or check6 or check7 or check8:
        navigator "С одеждой решили. Теперь прическа, аксессуары и макияж. Да, мужчинам нужен макияж. Вперед, к зеркалу!"
        jump mirror_game_m        

    jump wardrobe_game_m


label mirror_game_f:
    if first_game_mirror:
        scene mirror_bg_f with fade
    else:
        scene mirror_bg_f
    
    show character_bg_f at Position(xpos = 750, ypos = 221, xanchor = 0, yanchor = 0)
    # отображаем прически. Если прическа выбрана, соответствующий рисунок выбора не отображается
    show haircut1f at Position(xpos = main_haircut_position_f[1][0], ypos = main_haircut_position_f[1][1], xanchor = 0, yanchor = 0)
    show haircut2f at Position(xpos = main_haircut_position_f[2][0], ypos = main_haircut_position_f[2][1], xanchor = 0, yanchor = 0)
    if not haircut_ready[3]:
        show haircut3f at Position(xpos = main_haircut_position_f[3][0], ypos = main_haircut_position_f[3][1], xanchor = 0, yanchor = 0)
    if not haircut_ready[4]:
        show haircut4f at Position(xpos = main_haircut_position_f[4][0], ypos = main_haircut_position_f[4][1], xanchor = 0, yanchor = 0)
    # отображаем украшения и косметику
    show add1f at Position(xpos = add_position_f[1][0], ypos = add_position_f[1][1], xanchor = 0, yanchor = 0)
    show add2f at Position(xpos = add_position_f[2][0], ypos = add_position_f[2][1], xanchor = 0, yanchor = 0)
    show add3f at Position(xpos = add_position_f[3][0], ypos = add_position_f[3][1], xanchor = 0, yanchor = 0)
    show add4f at Position(xpos = add_position_f[4][0], ypos = add_position_f[4][1], xanchor = 0, yanchor = 0)
    show add5f at Position(xpos = add_position_f[5][0], ypos = add_position_f[5][1], xanchor = 0, yanchor = 0)
    show add6f at Position(xpos = add_position_f[6][0], ypos = add_position_f[6][1], xanchor = 0, yanchor = 0)
    show add7f at Position(xpos = add_position_f[7][0], ypos = add_position_f[7][1], xanchor = 0, yanchor = 0)
    # отображаем неактивную косметику (уже использована)
    if add_ready[5]:
        show add5_inactive_f at Position(xpos = main_add_position_f[5][0], ypos = main_add_position_f[5][1], xanchor = 0, yanchor = 0)
    if add_ready[6]:
        show add6_inactive_f at Position(xpos = main_add_position_f[6][0], ypos = main_add_position_f[6][1], xanchor = 0, yanchor = 0)
    if add_ready[7]:
        show add7_inactive_f at Position(xpos = main_add_position_f[7][0], ypos = main_add_position_f[7][1], xanchor = 0, yanchor = 0)


    if first_game_mirror:
        navigator "Так же как и в предыдущей части, вам необходимо поочереди перетаскивать элементы. А я буду помогать."
        call screen MirrorScreenF
        $ first_game_mirror = False
    else:
        call screen MirrorScreenF

    python:
        char_return = [char for char in _return]
        num1 = len(char_return)
        num2 = int(char_return[num1-1])

        if num1 == 8: #haircut
            if num2 == 3 or num2 == 4:
                for a in range(1, 5):
                    haircut_ready[a] = False
                haircut_ready[num2] = True
                update_mirror_image_f(1, num2)
        if num1 == 4: #add
            if num2 != 2 and num2 != 4:
                add_position_f[num2][0] = add_model_position_f[num2][0]
                add_position_f[num2][1] = add_model_position_f[num2][1] 
                add_ready[num2] = True
                update_mirror_image_f(2, num2)
        
        navigator(navigator_mirror_str_f[_return])
        check = (haircut_ready[3] or haircut_ready[4]) and add_ready[1] and add_ready[3] and add_ready[5] and add_ready[6] and add_ready[7]
    
    if check:
        navigator "Поздравляю! Вы готовы к съёмкам. Вас ждут в студии!"
        $arrow_at_cupboard = False
        $todo_five_colmpleted = True
        jump technical_label_5_5

    jump mirror_game_f


label mirror_game_m:

    if first_game_mirror:
        scene mirror_bg_m with fade
    else:
        scene mirror_bg_m
    
    show character_bg_m at Position(xpos = 725, ypos = 185, xanchor = 0, yanchor = 0)
    # отображаем прически. Если прическа выбрана, соответствующий рисунок выбора не отображается
    show haircut2m at Position(xpos = main_haircut_position_m[2][0], ypos = main_haircut_position_m[2][1], xanchor = 0, yanchor = 0)
    show haircut4m at Position(xpos = main_haircut_position_m[4][0], ypos = main_haircut_position_m[4][1], xanchor = 0, yanchor = 0)
    if not haircut_ready[1]:
        show haircut1m at Position(xpos = main_haircut_position_m[1][0], ypos = main_haircut_position_m[1][1], xanchor = 0, yanchor = 0)
    if not haircut_ready[3]:
        show haircut3m at Position(xpos = main_haircut_position_m[3][0], ypos = main_haircut_position_m[3][1], xanchor = 0, yanchor = 0)
    
    # отображаем украшения и косметику
    show add1m at Position(xpos = add_position_m[1][0], ypos = add_position_m[1][1], xanchor = 0, yanchor = 0)
    show add2m at Position(xpos = add_position_m[2][0], ypos = add_position_m[2][1], xanchor = 0, yanchor = 0)
    show add3m at Position(xpos = add_position_m[3][0], ypos = add_position_m[3][1], xanchor = 0, yanchor = 0)
    show add5m at Position(xpos = add_position_m[5][0], ypos = add_position_m[5][1], xanchor = 0, yanchor = 0)
    show add6m at Position(xpos = add_position_m[6][0], ypos = add_position_m[6][1], xanchor = 0, yanchor = 0)
    show add7m at Position(xpos = add_position_m[7][0], ypos = add_position_m[7][1], xanchor = 0, yanchor = 0)
    show add8m at Position(xpos = add_position_m[8][0], ypos = add_position_m[8][1], xanchor = 0, yanchor = 0)
    
    #отображаем часы, если они не использованы
    if not add_ready[4]:
        show add4m at Position(xpos = add_position_m[4][0], ypos = add_position_m[4][1], xanchor = 0, yanchor = 0)

    # отображаем неактивную косметику (уже использована)
    if add_ready[8]:
        show add8_inactive_m at Position(xpos = main_add_position_m[8][0], ypos = main_add_position_m[8][1], xanchor = 0, yanchor = 0)


    if first_game_mirror:
        navigator "Так же как и в предыдущей части, вам необходимо поочереди перетаскивать элементы. А я буду помогать."
        call screen MirrorScreenM
        $ first_game_mirror = False
    else:
        call screen MirrorScreenM

    python:
        char_return = [char for char in _return]
        num1 = len(char_return)
        num2 = int(char_return[num1-1])

        if num1 == 8: #haircut
            if num2 == 1 or num2 == 3:
                for a in range(1, 5):
                    haircut_ready[a] = False
                haircut_ready[num2] = True
                update_mirror_image_m(1, num2)
        if num1 == 4: #add
            if num2 == 6 or num2 == 8: 
                add_position_m[num2][0] = add_model_position_m[num2][0]
                add_position_m[num2][1] = add_model_position_m[num2][1] 
                add_ready[num2] = True
                update_mirror_image_m(2, num2)
            if num2 == 4: #часы, которые не видны в зеркале
                add_ready[4] = True
                renpy.hide("add4m")
        
        navigator(navigator_mirror_str_m[_return])
        check = (haircut_ready[1] or haircut_ready[3]) and add_ready[4] and add_ready[6] and add_ready[8]

    if check:
        navigator "Поздравляю! Вы готовы к съёмкам. Вас ждут в студии!"
        $arrow_at_cupboard = False
        $todo_five_colmpleted = True
        jump technical_label_5_5


    jump mirror_game_m





################## 6 #######################




label sixth_mini_game_production:
    navigator "Презентации созданы, образ подобран, можно начинать запись курса."
    navigator "Свяжитесь с Екатериной, спросите, когда можно прийти на съемки?"
    
    jump technical_label_3_5


### Пока не выберет 5 или 10 презентаций ###
label technical_label_3_1:
    if sex == "male":
        menu:
            male_player "У меня готово ..."
            "1":
                $amount_of_presentations = 1
            "3":
                $amount_of_presentations = 3
            "5":
                $amount_of_presentations = 5
            "10":
                $amount_of_presentations = 10

        if amount_of_presentations == 1: 
            male_player "У меня готова {fast}[amount_of_presentations] презентация. Хочу её записать"
        elif amount_of_presentations == 3:
            male_player "У меня готово {fast}[amount_of_presentations] презентации. Хочу их записать"
        else:
            male_player "У меня готово {fast}[amount_of_presentations] презентаций. Хочу их записать"
        
        if amount_of_presentations < 5: 
            hide ekaterina
            show ekaterina sad
            ekaterina "Давайте еще подготовим несколько. Выходить на съемку нужно минимум с пятью готовыми  презентациями."
            ekaterina "Так мы сможем сразу получить пять готовых видеороликов. Иначе, может остаться неипользованное время."
            jump technical_label_3_1
        else:
            hide ekaterina
            show ekaterina funny
            ekaterina "Отлично,тогда нужно постараться все их записать. Сколько времени Вы можете выделить для одного съемочного дня?"
            jump technical_label_3_2
    else:
        menu:
            female_player "У меня готово ..."
            "1":
                $amount_of_presentations = 1
            "3":
                $amount_of_presentations = 3
            "5":
                $amount_of_presentations = 5
            "10":
                $amount_of_presentations = 10

        if amount_of_presentations == 1: 
            female_player "У меня готова {fast}[amount_of_presentations] презентация. Хочу её записать."
        elif amount_of_presentations == 3:
            female_player "У меня готово {fast}[amount_of_presentations] презентации. Хочу их записать."
        else:
            female_player "У меня готово {fast}[amount_of_presentations] презентаций. Хочу их записать."
        
        if amount_of_presentations < 5: 
            hide ekaterina
            show ekaterina sad
            ekaterina "Давайте еще подготовим несколько. Выходить на съемку нужно минимум с пятью готовыми  презентациями."
            ekaterina "Так мы сможем сразу получить пять готовых видеороликов. Иначе, может остаться неипользованное время."
            jump technical_label_3_1
        else:
            hide ekaterina
            show ekaterina funny
            ekaterina "Отлично,тогда нужно постараться все их записать. Сколько времени Вы можете выделить для одного съемочного дня?"
            jump technical_label_3_2

### Пока не выберем достаточное количество свободного времени для съемок ###
label technical_label_3_2:
    if sex == "male":
        menu:
            male_player "У меня будет ..."
            "1 час":
                male_player "У меня будет {fast}1 час. Могу его занять видеосъемкой."
                hide ekaterina
                show ekaterina sad
                ekaterina "Съемки одной партии видеолекций длятся в среднем 2-4 часа. Это оптимальное количество времени для записи всех видео."
                hide ekaterina
                show ekaterina normal_2
                ekaterina "Если Вы не можете найти свободные 3 часа, то съемки следует отложить на другой раз."
                ekaterina "Иначе больше времени уйдет на подготовку к съемкам, чем на саму запись видеолекций."
                jump technical_label_3_2
            "2 часа":
                male_player "У меня будет {fast}2 часа. Могу их занять видеосъемкой"
                if amount_of_presentations == 5:
                    hide ekaterina
                    show ekaterina funny
                    ekaterina "Хорошо, этого времени Вам будет достаточно. Давайте выберем день и время. Когда Вам удобно?"
                    hide ekaterina
                    show ekaterina normal_2
                    ekaterina "Напомню, что прийти к нам нужно за 30 минут до назначенного времени."
                    jump technical_label_3_3
                else:
                    hide ekaterina
                    show ekaterina sad
                    ekaterina "Съемки одной партии видеолекций длятся в среднем 2-4 часа. Это оптимальное количество времени для записи всех видео."
                    hide ekaterina
                    show ekaterina normal_2
                    ekaterina "Если Вы не можете найти свободные 3 часа, то съемки следует отложить на другой раз."
                    ekaterina "Иначе больше времени уйдет на подготовку к съемкам, чем на саму запись видеолекций."
                    jump technical_label_3_2
            "3 часа":
                male_player "У меня будет {fast}3 часа. Могу их занять видеосъемкой"
                if amount_of_presentations == 5:
                    hide ekaterina
                    show ekaterina sad
                    ekaterina "Для пяти видео этого времени много, предлагаем Вам запланировать 2 часа съемок."
                    jump technical_label_3_2
                else:
                    hide ekaterina
                    show ekaterina funny
                    ekaterina "Хорошо, этого времени Вам будет достаточно. Давайте выберем день и время. Когда Вам удобно?"
                    hide ekaterina
                    show ekaterina normal_2
                    ekaterina "Напомню, что прийти к нам нужно за 30 минут до назначенного времени."
                    jump technical_label_3_3
            "4 часа":
                male_player "У меня будет {fast}4 часа. Могу их занять видеосъемкой"
                if amount_of_presentations == 5:
                    hide ekaterina
                    show ekaterina sad
                    ekaterina "Для пяти видео этого времени много, предлагаем Вам запланировать 2 часа съемок."
                    jump technical_label_3_2
                else:
                    hide ekaterina
                    show ekaterina funny
                    ekaterina "Хорошо, этого времени Вам будет достаточно. Давайте выберем день и время. Когда Вам удобно?"
                    hide ekaterina
                    show ekaterina normal_2
                    ekaterina "Напомню, что прийти к нам нужно за 30 минут до назначенного времени."
                    jump technical_label_3_3
    else:
        menu:
            male_player "У меня будет ..."
            "1 час":
                male_player "У меня будет {fast}1 час. Могу его занять видеосъемкой"
                hide ekaterina
                show ekaterina sad
                ekaterina "Съемки одной партии видеолекций длятся в среднем 2-4 часа. Это оптимальное количество времени для записи всех видео."
                hide ekaterina
                show ekaterina normal_2
                ekaterina "Если Вы не можете найти свободные 3 часа, то съемки следует отложить на другой раз."
                ekaterina "Иначе больше времени уйдет на подготовку к съемкам, чем на саму запись видеолекций."
                jump technical_label_3_2
            "2 часа":
                male_player "У меня будет {fast}2 часа. Могу их занять видеосъемкой"
                if amount_of_presentations == 5:
                    hide ekaterina
                    show ekaterina funny
                    ekaterina "Хорошо, этого времени Вам будет достаточно. Давайте выберем день и время. Когда Вам удобно?"
                    hide ekaterina
                    show ekaterina normal_2
                    ekaterina "Напомню, что прийти к нам нужно за 30 минут до назначенного времени."
                    jump technical_label_3_3
                else:
                    hide ekaterina
                    show ekaterina sad
                    ekaterina "Съемки одной партии видеолекций длятся в среднем 2-4 часа. Это оптимальное количество времени для записи всех видео."
                    hide ekaterina
                    show ekaterina normal_2
                    ekaterina "Если Вы не можете найти свободные 3 часа, то съемки следует отложить на другой раз."
                    ekaterina "Иначе больше времени уйдет на подготовку к съемкам, чем на саму запись видеолекций."
                    jump technical_label_3_2
            "3 часа":
                male_player "У меня будет {fast}3 часа. Могу их занять видеосъемкой"
                if amount_of_presentations == 5:
                    hide ekaterina
                    show ekaterina sad
                    ekaterina "Для пяти видео этого времени много, предлагаем Вам запланировать 2 часа съемок."
                    jump technical_label_3_2
                else:
                    hide ekaterina
                    show ekaterina funny
                    ekaterina "Хорошо, этого времени Вам будет достаточно. Давайте выберем день и время. Когда Вам удобно?"
                    hide ekaterina
                    show ekaterina normal_2
                    ekaterina "Напомню, что прийти к нам нужно за 30 минут до назначенного времени."
                    jump technical_label_3_3
            "4 часа":
                male_player "У меня будет {fast}4 часа. Могу их занять видеосъемкой"
                if amount_of_presentations == 5:
                    hide ekaterina
                    show ekaterina sad
                    ekaterina "Для пяти видео этого времени много, предлагаем Вам запланировать 2 часа съемок."
                    jump technical_label_3_2
                else:
                    hide ekaterina
                    show ekaterina funny
                    ekaterina "Хорошо, этого времени Вам будет достаточно. Давайте выберем день и время. Когда Вам удобно?"
                    hide ekaterina
                    show ekaterina normal_2
                    ekaterina "Напомню, что прийти к нам нужно за 30 минут до назначенного времени."
                    jump technical_label_3_3

label technical_label_3_3:
    if sex == "male":
        menu:
            male_player "Мне удобно в ..."

            "понедельник с 13:00":
                hide ekaterina
                show ekaterina sad
                ekaterina "В это время в студии профилактические работы. Посмотрите, пожалуйста, другой день."
                jump technical_label_3_3
            "четверг с 10:00":
                hide ekaterina
                show ekaterina normal_2
                ekaterina "Хорошо. Я внесу Вас в график съемок. До свидания."
            "пятницу с 14:00":
                hide ekaterina
                show ekaterina normal_2
                ekaterina "Хорошо. Я внесу Вас в график съемок. До свидания."
    else:
        menu:
            female_player "Мне удобно в ..."

            "понедельник с 13:00":
                hide ekaterina
                show ekaterina sad
                ekaterina "В это время в студии профилактические работы. Посмотрите, пожалуйста, другой день."
                jump technical_label_3_3
            "четверг с 10:00":
                hide ekaterina
                show ekaterina normal_2
                ekaterina "Хорошо. Я внесу Вас в график съемок. До свидания!"
            "пятницу с 14:00":
                hide ekaterina
                show ekaterina normal_2
                ekaterina "Хорошо. Я внесу Вас в график съемок. До свидания!"
    
    hide ekaterina

    call screen nots

    if _return == "exit":
        if pet == "cat":
            scene home_with_cat with LongFade
        elif pet == "dog":
            scene home_with_dog with LongFade

        navigator "Ура! Сегодня у нас съемки. Пора собираться и идти в студию!"
        navigator "Для начала вам стоит пойти в Центр, там вас встретит Екатерина и все объяснит."
        jump technical_label_3_4


label technical_label_3_4:
    call screen room

    if _return == "exit":
        menu:
            "Пойти в Центр":
                scene nots with fade
                
                show ekaterina funny with dissolve

                ekaterina "Здравствуйте, [name]! Отлично выглядите! Вы пришли как раз вовремя."
                ekaterina "Я буду сопровождать Вас в студии. Не волнуйтесь. У вас все получится! Нас уже ждут...."
                scene studia_game_idle with fade
                navigator "Упс.. Что-то пошло не так. Помогите привести студию в порядок."
                jump video_studia_game

            "Пойти на кафедру":
                navigator "Вас ждут в Центре."
            "Остаться дома":
                navigator "Вас уже ждут в Центре."
        jump technical_label_3_4
    else:
        jump technical_label_3_4
    
label technical_label_3_5:
    call screen room

    $flag_room_computer_opened = False

    if _return == "exit":
        menu:
            "Пойти в Центр":
                scene nots with fade

                show ekaterina normal_2 with dissolve

                if sex == "male":
                    male_player "Здравствуйте, Екатерина! Материалы для съемок подготовлены. Когда я могу начать запись видеолекций?"
                else:
                    female_player "Здравствуйте, Екатерина! Материалы для съемок подготовлены. Когда я могу начать запись видеолекций?"

                ekaterina "Здравствуйте, [name]! Сколько презентаций у Вас готово? Сколько видеолекций вы уже хотите записать?"

                jump technical_label_3_1

            "Пойти на кафедру":
                navigator "Вас ждут в центре."
            "Остаться дома":
                navigator "Лучше не задерживаться. Вас ждут в центре."
        jump technical_label_3_5
    else:
        navigator "Лучше не задерживаться. Вас ждут в центре."
        jump technical_label_3_5


label video_studia_game:
    
    scene studia_game_idle

    show buttonf at Position(xpos = 1186, ypos = 26, xanchor = 0, yanchor = 0)

    call screen studia_game

    if _return == "window_finded":
        navigator "Правильно. Окно должно быть закрыто. Шторы опущены."
        jump video_studia_game
    elif _return == "sofits_finded":
        navigator "Точно! Софиты включаются до начала записи видеолекций."
        jump video_studia_game
    elif _return == "operator_finded":
        navigator "Да, это ошибка. Оператор не должен отвлекаться во время съемки."
        jump video_studia_game
    elif _return == "text_finded":
        navigator "Да. Нужно сокращать текст в  слайдах при подготовке презентации."
        jump video_studia_game
    elif _return == "author_head_finded":
        navigator "Это важно! Во время записи нужно смотреть в камеру."
        jump video_studia_game
    elif _return == "author_hand_finded":
        if sex == "male":
            navigator "Вы внимательный! Руками размахивать нельзя. Кажется автор допустил еще одну ошибку."
        else:
            navigator "Вы внимательная! Руками размахивать нельзя. Кажется автор допустил еще одну ошибку."
        jump video_studia_game
    elif _return == "author_garment_finded":
        navigator "Верно! Белый, черный и красный цвета не подходят для съемки."
        jump video_studia_game
    elif _return == "door_open_finded":
        navigator "Конечно! На съемках не должно быть посторонних."
        jump video_studia_game
    elif _return == "send":
        if window_finded and sofits_finded and operator_finded and text_finded and door_open_finded and author_hand_finded and author_head_finded and author_garment_finded:
            navigator "Вы справились! Давайте приведем нашу студию в порядок."

            scene studia_game_right with fade

            navigator "Ну вот, теперь всё так, как и должно быть на съемках видеолекций."
            $todo_six_colmpleted = True
            $final_flag_1 = False
            jump final
            #окончание мини-игры
        else:
            if not window_finded:
                navigator "Поищите еще. Вам не мешают шум и свет?"
                jump video_studia_game
            elif not door_open_finded:
                navigator "А дверь не забыли закрыть?"
                jump video_studia_game
            elif not sofits_finded:
                navigator "Вам не кажется, что мало света в студии?"
                jump video_studia_game
            elif not operator_finded:
                navigator "Смотрите, кто-то отвлекся от съемок!"
                jump video_studia_game
            elif not author_head_finded:
                navigator "Куда смотрит автор?"
                jump video_studia_game
            elif not author_garment_finded:
                navigator "Внешний вид автора соответствует рекомендациям?"
                jump video_studia_game
            elif not author_hand_finded:
                navigator "Какой широкий жест у автора в кадре! Это разве правильно?"
                jump video_studia_game
            elif not text_finded:
                navigator "Обратите внимание на суфлер."
                jump video_studia_game 


label final:
    if final_flag_1 == False:
        scene nots with fade
    else:
        scene nots
        
    if final_flag_1 == False:
        show ekaterina funny
        ekaterina "Ура! Вы справились со всеми заданиями. Пора на кафедру."
        hide ekaterina funny

    $final_flag_1 = True
    call screen nots

    if _return == "exit":
        
        menu:
            "Пойти домой":
                navigator "Вас ждут на кафедре."
                jump final
            "Пойти на кафедру":
                jump final_in_the_kafedra
            "Остаться в центре":
                navigator "Лучше поторопиться. Вас уже ждут на кафедре."
                jump final

label final_in_the_kafedra:
    scene final_1 with fade
    if sex == "male":
        headOfDepartment "Поздравляю, коллега! Вы прошли путь создателя онлайн-курса до конца!"
        docent "Уверены, что Вам было не просто, но оно того стоило."
        male_player "Спасибо! Это был замечательный опыт."
        professor "И какой же основной принцип создания хорошего курса?"
        male_player "Надо ориентироваться на студента!"
        headOfDepartment "Верная мысль. Какие планы дальше?"
        male_player "Я уже продумываю структуру будущего онлайн-курса и собираю команду."
        docent "Как интересно! Я с Вами! И, кстати, Ваш сертификат уже готов."
        headOfDepartment "Желаем Вам удачи! Применяйте полученные знания на практике."
        navigator "Чтобы сохранить Ваш сертификат, Вы можете сделать скриншот или сфотографировать его на свой телефон."
    else:
        headOfDepartment "Поздравляю, коллега! Вы прошли путь создателя онлайн-курса до конца!"
        docent "Уверены, что Вам было не просто, но оно того стоило."
        female_player "Спасибо! Это был замечательный опыт."
        professor "И какой же основной принцип создания хорошего курса?"
        female_player "Надо ориентироваться на студента!"
        headOfDepartment "Верная мысль. Какие планы дальше? "
        female_player "Я уже продумываю структуру будущего онлайн-курса и собираю команду."
        docent "Как интересно! Я с Вами! И, кстати, Ваш сертификат уже готов."
        headOfDepartment "Желаем Вам удачи! Применяйте полученные знания на практике."

        navigator "Чтобы сохранить Ваш сертификат, Вы можете сделать скриншот или сфотографировать его на свой телефон."
         
    call screen final_finalov
    if(_return == "Sertifikat"):
        call screen input_FIO with dissolve

        python:
            checked_name = _return
            FIO = checked_name

        scene black with dissolve
        show ser at center
        show text "[FIO]" at Position(xpos = 593, ypos = 490, xanchor = 0, yanchor = 0)

        pause 

        navigator "Ваш питомец соскучился, пора домой."

        if pet == "dog":
            scene dog_zoom with fade
        else:
            scene cat_zoom with fade

        if sex == "male":
            male_player "Привет, [pet_name]! Порадуйся за меня! Теперь я знаю, как сделать классный онлайн-курс."
        else:
            female_player "Привет, [pet_name]! Порадуйся за меня! Теперь я знаю, как сделать классный онлайн-курс."

        jump game_over
        
label game_over:
    if pet == "dog":
        scene dog_zoom
    else:
        scene cat_zoom

    call screen final2 with dissolve

    if _return == "Sertifikat":
        scene black with dissolve
        show ser at center
        show text "[FIO]" at Position(xpos = 593, ypos = 490, xanchor = 0, yanchor = 0)
        pause
        jump game_over