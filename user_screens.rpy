screen input_name(): # Ввод имени игрока
    add "images/input/input_name_bg.jpg"

    input default "":
        xpos 950
        ypos 490
        pixel_width 470

        xysize (473, 45)

screen input_FIO(): # Ввод ФИО игрока
    add "images/input/input_FIO_bg.png"

    input default "":
        xpos 950
        ypos 490
        pixel_width 700

        xysize (700, 45)

screen input_sex_and_pet(): # Ввод пола и питомца
    add "images/input/registration_bg.jpg"
    hbox:
        xysize (213, 81)
        xpos 844
        ypos 340

        imagebutton:
            idle ("images/input/male_btn_in_reg_normal.png")
            hover ("images/input/male_btn_in_reg_hover.png" )
            selected_idle ("images/input/male_btn_in_reg_hover.png")

            action [SetVariable("sex", "male"), SelectedIf(sex == "male")]
        imagebutton:
            idle ("images/input/female_btn_in_reg_normal.png")
            hover ("images/input/female_btn_in_reg_hover.png")
            selected_idle ("images/input/female_btn_in_reg_hover.png")

            action [SetVariable("sex", "female"), SelectedIf(sex == "female")]

    hbox:
        xysize(383, 81)
        xpos 760
        ypos 670

        imagebutton:
            idle ("images/input/cat_btn_in_reg_normal.png")
            hover ("images/input/cat_btn_in_reg_hover.png")
            selected_idle ("images/input/cat_btn_in_reg_hover.png")

            action [SetVariable("pet", "cat"), SelectedIf(pet == "cat")]
        imagebutton:
            idle ("images/input/dog_btn_in_reg_normal.png")
            hover ("images/input/dog_btn_in_reg_hover.png")
            selected_idle ("images/input/dog_btn_in_reg_hover.png")

            action [SetVariable("pet", "dog"), SelectedIf(pet == "dog")]

    imagebutton:
        xpos 880
        ypos 850

        idle ("images/input/ok_btn.png")
        hover ("images/input/ok_btn_hover.png")

        action [Return("exit"), SensitiveIf(sex != "" and pet != "")]

screen input_name_of_pet(): # Ввод имени питомца
    add "images/input/input_name_of_pet.png" xalign 0.5 yalign 0.5

    input default "":
        xpos 950
        ypos 540
        pixel_width 470

        xysize (473, 45)


screen room(): # Комната автора

    imagemap:
        if flag_room_broken:    # флаг, возникающий в мини-игре дальше в сюжете
                                # Просто решили сделать один скрин, чтобы его потом вызывать - без копий.
            if pet == "cat":
                ground "images/home/home_broken_with_cat.jpg"
                hover "images/home/home_broken_with_cat_hover.jpg"
            else:
                ground "images/home/home_broken_with_dog.jpg"
                hover "images/home/home_broken_with_dog_hover.jpg"
        else:
            if pet == "cat":
                ground "images/home/home_with_cat.jpg"
                hover "images/home/home_with_cat_hover.jpg"
            else:
                ground "images/home/home_with_dog.jpg"
                hover "images/home/home_with_dog_hover.jpg"

        if flag_room_computer_opened:
            hotspot (522, 403, 283, 231) clicked Return("open_computer") # Комьютер
        if flag_room_cupboard_opened:
            hotspot (1152, 172, 485, 759) clicked Return("open_cupboard") # Шкаф
        if flag_room_door_opened:
            hotspot (1659, 52, 242, 938) clicked Return("exit") # Дверь
        if flag_room_album_opened:
            hotspot (836, 246, 124, 121) clicked Return("open_album") # Альбом
        if flag_room_pet_opened and pet == "cat":
            hotspot (86, 863, 217, 166) clicked Return("touch_pet") # Кошка
        elif flag_room_pet_opened and pet == "dog":
            hotspot (60, 777, 245, 251) clicked Return("touch_pet") # Собака

    # Стрелки контролируются глоб. переменными в файле user_variables и включаются/отключаются тут

    showif arrow_at_computer:
        add "images/arrows/arrow_bottom.png" at arrow_move_vert(0.335, 0.2)

    showif arrow_at_door_at_home:
        add "images/arrows/arrow_right.png" at arrow_move(0.85, 0.5)

    showif arrow_at_pet:
        add "images/arrows/arrow_left.png" at arrow_move(0.2, 0.9)

    showif arrow_at_album:
        add "images/arrows/arrow_right.png" at arrow_move(0.35, 0.25)
    
    showif arrow_at_cupboard:
        add "images/arrows/arrow_right.png" at arrow_move(0.6, 0.5)


screen computer(): # Компьютер

    imagemap:
        ground "images/desktop/desktop_normal.jpg"
        hover "images/desktop/desktop_hover.jpg"

        # Кнопка закрытия компьютера

            # скрин будет возвращать:
                # close_computer - если никакие сюжетные письма не были прочитаны
                # mail_checked - если игрок прочитал письмо в рамках сюжета и нужно двигаться дальше
        hotspot (23, 1008, 66, 65) action [
            SetVariable("show_mail_area", False),
            SetVariable("show_todo_area", False),
            If(not user_have_new_message and user_need_to_read_mail, true=Return("mail_checked"), false=Return("close_computer"))
            ]

    # Кнопка с пометкой "новое сообщение"
    showif user_have_new_message:
        imagebutton:
            xpos 25
            ypos 25

            idle ("images/desktop/mail_icon_new_message.png")
            hover ("images/desktop/mail_icon_hover_new_message.png")

            action [
            ToggleVariable("show_mail_area", True, False),
            SetVariable("user_have_new_message", False),
            SetVariable("show_todo_area", False),
            SetVariable("arrow_at_message_icon", False) # нужно для того, чтобы в первый раз выключить стрелку
            ]

# Кнопка без пометки "новое сообщение"
    showif not user_have_new_message:
        showif arrow_at_close:
            add "images/arrows/arrow_bottom_2.png" at arrow_move_vert(0, 0.89)
        imagebutton:
            xpos 25
            ypos 25

            idle ("images/desktop/mail_icon.png")
            hover ("images/desktop/mail_icon_hover.png")

            action [
            ToggleVariable("show_mail_area", True, False),
            SetVariable("user_have_new_message", False),
            SetVariable("show_todo_area", False),
            ]

# Кнопка ту-ду листа (дальше в сюжете)
    showif show_todo_icon:
        imagebutton:
            xpos 25
            ypos 250

            idle ("images/desktop/todo_icon.png")
            hover ("images/desktop/todo_icon_hover.png")

            action [
            ToggleVariable("show_todo_area", True, False),
            SetVariable("show_mail_area", False),
            SetVariable("arrow_at_todo_icon", False) # нужно для того, чтобы в первый раз выключить стрелку
            ]

# Поле почты
    showif show_mail_area:
        add "images/desktop/mail_area.png" xpos 450 ypos 25
        text current_message[0] style "text_in_message_from_who" xpos 725 ypos 195
        text current_message[1] style "text_in_message" xpos 540 ypos 280 xysize(1170, 500)
        showif show_file_to_make_programm: # в сюжете будет нужно в почте ихобразить "прикреплённый файл" - это для этого случая, по аналогии с room

            imagebutton:
                xpos 1450
                ypos 700

                idle ("images/mini_games_stuff/creating_program/open_attached_file.png")
                hover ("images/mini_games_stuff/creating_program/open_attached_file_hover.png")

                action [
                    Return("open_file"),
                    SetVariable("show_mail_area", False)
                ]

# Ту-ду лист
    showif show_todo_area:
        add "images/desktop/todo_area.png" xpos 219 ypos 27

        vbox:
            xpos 370 ypos 236
            spacing 69
            
            textbutton "        Тексты к видео" text_style "text_as_btn" action [SensitiveIf(not todo_two_colmpleted), Return("2")] # если не завершена эта часть игры, то кнопка активна

            textbutton "        Правовая чистота" text_style "text_as_btn" action [SensitiveIf(not todo_three_colmpleted and todo_two_colmpleted), Return("3")] # /\

            textbutton "        Монтажные презентации" text_style "text_as_btn" action [SensitiveIf(not todo_four_colmpleted and todo_three_colmpleted), Return("4")] # /\

            textbutton "        Внешний образ" text_style "text_as_btn" action [SensitiveIf(not todo_five_colmpleted and todo_four_colmpleted), Return("5")] # /\

            textbutton "        Съёмки" text_style "text_as_btn" action [SensitiveIf(not todo_six_colmpleted and todo_five_colmpleted), Return("6")] # /\

        showif todo_two_colmpleted: # завершенные части закрываются крестиком
            add "images/desktop/gale.png" xpos 368 ypos 235
        showif todo_three_colmpleted:
            add "images/desktop/gale.png" xpos 368 ypos 355
        showif todo_four_colmpleted:
            add "images/desktop/gale.png" xpos 368 ypos 475
        showif todo_five_colmpleted:
            add "images/desktop/gale.png" xpos 368 ypos 596
        showif todo_six_colmpleted:
            add "images/desktop/gale.png" xpos 368 ypos 690

    showif arrow_at_message_icon: # стрелки-указатели в первый раз открытия компьютера 
        add "images/arrows/arrow_left.png" at arrow_move(0.15, 0.08)

    showif arrow_at_todo_icon:
        add "images/arrows/arrow_left.png" at arrow_move(0.15, 0.3)

    showif arrow_at_close_computer:
        add "images/arrows/arrow_bottom_2.png" at arrow_move_vert(0, 0.9)


screen department_door(): # Дверь перед кафедрой
    imagemap:
        ground "images/department/department_door.jpg"
        hover "images/department/department_door_hover.jpg"

        hotspot (681, 77, 559, 854) action[
        SetVariable("amount_of_clicks", amount_of_clicks+1),
        If(amount_of_clicks >= 2, true=Return("go"))
        ]
        # скрин перебрасывает человека дальше в сюжете если нажать на экран 3 раза - счётчик

screen department(): # Кафедра
    imagemap:
        ground "images/department/department.jpg"
        hover "images/department/department_hover.jpg"

        hotspot (15, 94, 242, 908) clicked Return("exit") # дверь
        if flag_department_blackboard_opened:
            hotspot (917, 277, 652, 363) clicked NullAction() # Доска

        showif arrow_at_door_in_department:
            add "images/arrows/arrow_left.png" at arrow_move(0.15, 0.5)


screen nots(): # НОЦ
    imagemap:
        ground "images/nots/nots.jpg"
        hover "images/nots/nots_hover.jpg"

        hotspot (10, 113, 256, 967) clicked Return("exit") # Дверь
        if flag_nots_window_opened:
            hotspot (1675, 53, 245, 735) clicked NullAction() # Окно

        showif arrow_at_door_in_nots:
            add "images/arrows/arrow_left.png" at arrow_move(0.15, 0.5)

screen album(): # Мини-игра на подбор фотографии в альбоме 

    # Есть 6 imageButton'ов, которые заранее выставлены как "верный/неверный ответ", при нажатии на которые
    # либо заканчивается игра, либо игра продолжается и выбранный ответ элиминируется с комментарием

    add "images/album_photos/album.jpg"

    imagebutton:
        xpos 235
        ypos 152

        if sex == "female":
            idle ("images/album_photos/normal/female_5.jpg")
            hover ("images/album_photos/hover/female_5.jpg")
            insensitive ("images/album_photos/wb/female_5.jpg")
        else:
            idle ("images/album_photos/normal/male_5.jpg")
            hover ("images/album_photos/hover/male_5.jpg")
            insensitive ("images/album_photos/wb/male_5.jpg")

        action [SetVariable("album_photos_selected_1", True), Return("uncorrect_1")]
        sensitive not album_photos_selected_1

    imagebutton:
        xpos 597
        ypos 152

        if sex == "female":
            idle ("images/album_photos/normal/female_4.jpg")
            hover ("images/album_photos/hover/female_4.jpg")
            insensitive ("images/album_photos/wb/female_4.jpg")
        else:
            idle ("images/album_photos/normal/male_4.jpg")
            hover ("images/album_photos/hover/male_4.jpg")
            insensitive ("images/album_photos/wb/male_4.jpg")

        action [SetVariable("album_photos_selected_2", True), Return("uncorrect_2")]
        sensitive not album_photos_selected_2

    imagebutton:
        xpos 412
        ypos 561

        if sex == "female":
            idle ("images/album_photos/normal/female_3.jpg")
            hover ("images/album_photos/hover/female_3.jpg")
        else:
            idle ("images/album_photos/normal/male_3.jpg")
            hover ("images/album_photos/hover/male_3.jpg")

        action [SetVariable("album_photos_selected_3", True), Return("correct")]
        sensitive not album_photos_selected_3

    imagebutton:
        xpos 970
        ypos 152

        if sex == "female":
            idle ("images/album_photos/normal/female_1.jpg")
            hover ("images/album_photos/hover/female_1.jpg")
            insensitive ("images/album_photos/wb/female_1.jpg")
        else:
            idle ("images/album_photos/normal/male_1.jpg")
            hover ("images/album_photos/hover/male_1.jpg")
            insensitive ("images/album_photos/wb/male_1.jpg")

        action [SetVariable("album_photos_selected_4", True), Return("uncorrect_3")]
        sensitive not album_photos_selected_4

    imagebutton:
        xpos 1328
        ypos 152

        if sex == "female":
            idle ("images/album_photos/normal/female_2.jpg")
            hover ("images/album_photos/hover/female_2.jpg")
            insensitive ("images/album_photos/wb/female_2.jpg")
        else:
            idle ("images/album_photos/normal/male_2.jpg")
            hover ("images/album_photos/hover/male_2.jpg")
            insensitive ("images/album_photos/wb/male_2.jpg")

        action [SetVariable("album_photos_selected_5", True), Return("uncorrect_4")]
        sensitive not album_photos_selected_5

    imagebutton:
        xpos 1048
        ypos 561

        if sex == "female":
            idle ("images/album_photos/normal/female_6.jpg")
            hover ("images/album_photos/hover/female_6.jpg")
            insensitive ("images/album_photos/wb/female_6.jpg")
        else:
            idle ("images/album_photos/normal/male_6.jpg")
            hover ("images/album_photos/hover/male_6.jpg")
            insensitive ("images/album_photos/wb/male_6.jpg")

        action [SetVariable("album_photos_selected_6", True), Return("uncorrect_5")]
        sensitive not album_photos_selected_6


screen making_program_mini_game(): # Мини-игра на составление программы

    # 7 разделов, при открытии которых появляются 4 варианта ответа. К каждому окну привязана своя переменная

    add "images/mini_games_stuff/creating_program/bg.jpg"

    vbox:
        xpos 105
        ypos 88
        xysize (486, 700)

        button:
            xysize (486, 100)

            imagebutton:
                idle ("images/mini_games_stuff/creating_program/btn_side_static.png")
                hover ("images/mini_games_stuff/creating_program/btn_side_hover.png")
                selected_idle ("images/mini_games_stuff/creating_program/btn_side_selected.png")
                selected_hover ("images/mini_games_stuff/creating_program/btn_side_selected.png")

                action [ToggleVariable("making_program_show_one", True, False),
                SetVariable("making_program_show_two", False),
                SetVariable("making_program_show_three", False),
                SetVariable("making_program_show_four", False),
                SetVariable("making_program_show_five", False),
                SetVariable("making_program_show_six", False),
                SetVariable("making_program_show_seven", False)
                ]
                selected making_program_show_one

            text "Название курса" style "left_btn_text":
                xalign 0.5
                yalign 0.575

            action NullAction()
            selected making_program_show_one

        button:
            xysize (486, 100)

            imagebutton:
                idle ("images/mini_games_stuff/creating_program/btn_side_static.png")
                hover ("images/mini_games_stuff/creating_program/btn_side_hover.png")
                selected_idle ("images/mini_games_stuff/creating_program/btn_side_selected.png")
                selected_hover ("images/mini_games_stuff/creating_program/btn_side_selected.png")

                action [SetVariable("making_program_show_one", False),
                ToggleVariable("making_program_show_two", True, False),
                SetVariable("making_program_show_three", False),
                SetVariable("making_program_show_four", False),
                SetVariable("making_program_show_five", False),
                SetVariable("making_program_show_six", False),
                SetVariable("making_program_show_seven", False)
                ]
                selected making_program_show_two

            text "Краткая аннотация" style "left_btn_text":
                xalign 0.5
                yalign 0.575

            action NullAction()
            selected making_program_show_two

        button:
            xysize (486, 100)

            imagebutton:
                idle ("images/mini_games_stuff/creating_program/btn_side_static.png")
                hover ("images/mini_games_stuff/creating_program/btn_side_hover.png")
                selected_idle ("images/mini_games_stuff/creating_program/btn_side_selected.png")
                selected_hover ("images/mini_games_stuff/creating_program/btn_side_selected.png")

                action [SetVariable("making_program_show_one", False),
                SetVariable("making_program_show_two", False),
                ToggleVariable("making_program_show_three", True, False),
                SetVariable("making_program_show_four", False),
                SetVariable("making_program_show_five", False),
                SetVariable("making_program_show_six", False),
                SetVariable("making_program_show_seven", False)
                ]
                selected making_program_show_three

            text "Цели курса" style "left_btn_text":
                xalign 0.5
                yalign 0.575

            action NullAction()
            selected making_program_show_three

        button:
            xysize (486, 100)

            imagebutton:
                idle ("images/mini_games_stuff/creating_program/btn_side_static.png")
                hover ("images/mini_games_stuff/creating_program/btn_side_hover.png")
                selected_idle ("images/mini_games_stuff/creating_program/btn_side_selected.png")
                selected_hover ("images/mini_games_stuff/creating_program/btn_side_selected.png")

                action [SetVariable("making_program_show_one", False),
                SetVariable("making_program_show_two", False),
                SetVariable("making_program_show_three", False),
                ToggleVariable("making_program_show_four", True, False),
                SetVariable("making_program_show_five", False),
                SetVariable("making_program_show_six", False),
                SetVariable("making_program_show_seven", False)
                ]
                selected making_program_show_four

            text "Трудоёмкость курса" style "left_btn_text":
                xalign 0.5
                yalign 0.575

            action NullAction()
            selected making_program_show_four

        button:
            xysize (486, 100)

            imagebutton:
                idle ("images/mini_games_stuff/creating_program/btn_side_static.png")
                hover ("images/mini_games_stuff/creating_program/btn_side_hover.png")
                selected_idle ("images/mini_games_stuff/creating_program/btn_side_selected.png")
                selected_hover ("images/mini_games_stuff/creating_program/btn_side_selected.png")

                action [SetVariable("making_program_show_one", False),
                SetVariable("making_program_show_two", False),
                SetVariable("making_program_show_three", False),
                SetVariable("making_program_show_four", False),
                ToggleVariable("making_program_show_five", True, False),
                SetVariable("making_program_show_six", False),
                SetVariable("making_program_show_seven", False)
                ]
                selected making_program_show_five

            text "Язык реализации" style "left_btn_text":
                xalign 0.5
                yalign 0.575

            action NullAction()
            selected making_program_show_five

        button:
            xysize (486, 100)

            imagebutton:
                idle ("images/mini_games_stuff/creating_program/btn_side_static.png")
                hover ("images/mini_games_stuff/creating_program/btn_side_hover.png")
                selected_idle ("images/mini_games_stuff/creating_program/btn_side_selected.png")
                selected_hover ("images/mini_games_stuff/creating_program/btn_side_selected.png")

                action [SetVariable("making_program_show_one", False),
                SetVariable("making_program_show_two", False),
                SetVariable("making_program_show_three", False),
                SetVariable("making_program_show_four", False),
                SetVariable("making_program_show_five", False),
                ToggleVariable("making_program_show_six", True, False),
                SetVariable("making_program_show_seven", False)
                ]
                selected making_program_show_six

            text "Результат обучения" style "left_btn_text":
                xalign 0.5
                yalign 0.575

            action NullAction()
            selected making_program_show_six

        button:
            xysize (486, 100)

            imagebutton:
                idle ("images/mini_games_stuff/creating_program/btn_side_static.png")
                hover ("images/mini_games_stuff/creating_program/btn_side_hover.png")
                selected_idle ("images/mini_games_stuff/creating_program/btn_side_selected.png")
                selected_hover ("images/mini_games_stuff/creating_program/btn_side_selected.png")

                action [SetVariable("making_program_show_one", False),
                SetVariable("making_program_show_two", False),
                SetVariable("making_program_show_three", False),
                SetVariable("making_program_show_four", False),
                SetVariable("making_program_show_five", False),
                SetVariable("making_program_show_six", False),
                ToggleVariable("making_program_show_seven", True, False),
                ]
                selected making_program_show_seven

            text "Содержание курса" style "left_btn_text":
                xalign 0.5
                yalign 0.575

            action NullAction()
            selected making_program_show_seven


    # Кнопка "Отправить" завершает миниигру
    button:
        xysize (462, 141)
        xpos 105
        ypos 815

        imagebutton:
            idle ("images/mini_games_stuff/creating_program/btn_send_static.png")
            hover ("images/mini_games_stuff/creating_program/btn_send_hover.png")
            insensitive ("images/mini_games_stuff/creating_program/btn_send_static.png")

            action Return("exit")
            sensitive making_program_one_true != "unselected" and making_program_two_true != "unselected" and making_program_three_true != "unselected" and making_program_four_true != "unselected" and making_program_five_true != "unselected" and making_program_six_true != "unselected" and making_program_seven_true != "unselected"


        text "Отправить" style "send_text": 
            xalign 0.5
            yalign 0.5

# Далее идут по 4 варианта ответа на каждый из 7 разделов (да, треш)

    showif making_program_show_one:
        grid 2 2:
            yalign 0.3
            xalign 0.9
            spacing 50

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_one_true", "correct")
                    selected making_program_one_true == "correct"

                text "Только суть и чем короче, тем лучше видно с мобильного телефона. Максимум 7 слов" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_one_true == "correct"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_one_true", "uncorrect_2")
                    selected making_program_one_true == "uncorrect_2"

                text "Нужно брать формулировку строго по учебному плану" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_one_true == "uncorrect_2"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_one_true", "uncorrect_3")
                    selected making_program_one_true == "uncorrect_3"

                text "Лучше выбрать максимально длинное название, чтобы охватить всю предметную область" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_one_true == "uncorrect_3"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_one_true", "uncorrect_4")
                    selected making_program_one_true == "uncorrect_4"

                text "Неважно какое название у онлайн-курса, оно может быть любое, главное - это содержание" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_one_true == "uncorrect_4"



    showif making_program_show_two:
        grid 2 2:
            yalign 0.3
            xalign 0.9
            spacing 50

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_two_true", "uncorrect_1")
                    selected making_program_two_true == "uncorrect_1"

                text "Цели освоения курса, продолжительность в неделю (до 3 тыс. знаков с пробелами)" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_two_true == "uncorrect_1"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_two_true", "uncorrect_2")
                    selected making_program_two_true == "uncorrect_2"

                text "Нормативные документы, распределение содержания по разделам и темам, виды аттестации (100-200 слов)" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_two_true == "uncorrect_2"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_two_true", "correct")
                    selected making_program_two_true == "correct"

                text "Основное содержание курса в 1-2 предложениях и его отличительные особенности (до 400 печатных знаков без пробелов)" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_two_true == "correct"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_two_true", "uncorrect_4")
                    selected making_program_two_true == "uncorrect_4"

                text "Задачи курса, связь с другими дисциплинами, информация об авторах (не более 400 печатных знаков без пробелов)" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_two_true == "uncorrect_4"

    showif making_program_show_three:
        grid 2 2:
            yalign 0.3
            xalign 0.9
            spacing 50

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_three_true", "uncorrect_1")
                    selected making_program_three_true == "uncorrect_1"

                text "Кратко описываются результаты онлайн-курса в терминах \"знать - уметь - владеть\"" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5
                    xysize (435, 265)

                action NullAction()
                selected making_program_three_true == "uncorrect_1"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_three_true", "correct")
                    selected making_program_three_true == "correct"

                text "Кратко формулируется ответ на вопрос, чему научится студент после прохождения курса" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_three_true == "correct"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_three_true", "uncorrect_3")
                    selected making_program_three_true == "uncorrect_3"

                text "Формулировка цели копируется из рабочей программы дисциплины в полном объеме без сокращений" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_three_true == "uncorrect_3"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_three_true", "uncorrect_4")
                    selected making_program_three_true == "uncorrect_4"

                text "Кратко показывается, какие образовательные технологии использованы при обучении на курсе" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_three_true == "uncorrect_4"

    showif making_program_show_four:
        grid 2 2:
            yalign 0.3
            xalign 0.9
            spacing 50

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_four_true", "uncorrect_1")
                    selected making_program_four_true == "uncorrect_1"

                text "Указывается в зачетных единицах, академических и астрономических часах" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5
                    xysize (450, 285)

                action NullAction()
                selected making_program_four_true == "uncorrect_1"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_four_true", "uncorrect_2")
                    selected making_program_four_true == "uncorrect_2"

                text "Указывается в академических и астрономических часах с примерной учебной нагрузкой в неделю" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5
                    xysize (420, 250)

                action NullAction()
                selected making_program_four_true == "uncorrect_2"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_four_true", "uncorrect_3")
                    selected making_program_four_true == "uncorrect_3"

                text "Указывается в зачетных единицах и в примерной учебной нагрузке в неделю" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5
                    xysize (420, 250)

                action NullAction()
                selected making_program_four_true == "uncorrect_3"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_four_true", "correct")
                    selected making_program_four_true == "correct"

                text "Указывается в зачетных единицах, академических и астрономических часах с примерной учебной нагрузкой в неделю" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5
                    xysize (420, 250)

                action NullAction()
                selected making_program_four_true == "correct"

    showif making_program_show_five:
        grid 2 2:
            yalign 0.3
            xalign 0.9
            spacing 50

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_five_true", "uncorrect_1")
                    selected making_program_five_true == "uncorrect_1"

                text "По умолчанию любой онлайн-курс создается всегда на русском языке" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5
                    xysize (500, 355)

                action NullAction()
                selected making_program_five_true == "uncorrect_1"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_five_true", "correct")
                    selected making_program_five_true == "correct"

                text "Выбор языка делает кафедра, ответственная за реализацию онлайн-курса" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_five_true == "correct"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_five_true", "uncorrect_3")
                    selected making_program_five_true == "uncorrect_3"

                text "Сам автор решает, на каком языке будет создан и реализован курс" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_five_true == "uncorrect_3"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_five_true", "uncorrect_4")
                    selected making_program_five_true == "uncorrect_4"

                text "Курс создается на том же языке, что и вся образовательная программа" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_five_true == "uncorrect_4"

    showif making_program_show_six:
        grid 2 2:
            yalign 0.3
            xalign 0.9
            spacing 50

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_six_true", "uncorrect_1")
                    selected making_program_six_true == "uncorrect_1"

                text "Формулировки результатов в терминах \"знать-уметь-владеть\" и далее в скобках порядковый номер" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_six_true == "uncorrect_1"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_six_true", "uncorrect_2")
                    selected making_program_six_true == "uncorrect_2"

                text "Формулировки результатов обучения копируются в строгом соответствии с рабочей программой дисциплины" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_six_true == "uncorrect_2"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_six_true", "correct")
                    selected making_program_six_true == "correct"

                text "Формулировки результата-действия (объяснение, применение, создание и др.), 7-9 слов и в скобках порядковый номер" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_six_true == "correct"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_six_true", "uncorrect_4")
                    selected making_program_six_true == "uncorrect_4"

                text "Формулировки произвольные, но отражающие суть того, чему учит курс. Количество слов определяет автор" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_six_true == "uncorrect_4"

    showif making_program_show_seven:
        grid 2 2:
            yalign 0.3
            xalign 0.9
            spacing 50

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_seven_true", "correct")
                    selected making_program_seven_true == "correct"

                text "Разделы (главы), подразделы (темы), компоненты (видеолекции и дополнительные материалы), контрольные точки (тесты)" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_seven_true == "correct"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_seven_true", "uncorrect_2")
                    selected making_program_seven_true == "uncorrect_2"

                text "Разделы (главы), подразделы (темы), страницы, компоненты (видеоролики, практикум и задания)" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_seven_true == "uncorrect_2"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_seven_true", "uncorrect_3")
                    selected making_program_seven_true == "uncorrect_3"

                text "Недели, темы, страницы, уроки (видеолекции, ссылки на дополнительные материалы, лонгриды и тесты)" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_seven_true == "uncorrect_3"

            button:
                padding (40, 40)
                xysize (587, 451)

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    idle ("images/mini_games_stuff/creating_program/btn_right_static.png")
                    hover ("images/mini_games_stuff/creating_program/btn_right_hover.png")
                    selected_idle ("images/mini_games_stuff/creating_program/btn_right_selected.png")
                    selected_hover ("images/mini_games_stuff/creating_program/btn_right_selected.png")

                    action SetVariable("making_program_seven_true", "uncorrect_4")
                    selected making_program_seven_true == "uncorrect_4"

                text "Разделы (главы), подразделы (темы), компоненты. Систему оценивания курса автор определяет самостоятельно" style "right_boxes_text":
                    xalign 0.5
                    yalign 0.5

                action NullAction()
                selected making_program_seven_true == "uncorrect_4"

# Мини-игра на поиск документов в разрушенной комнате автора
screen find_all_documents():
    imagemap:
        if pet == "cat":
            ground ("images/home/home_broken_with_cat.jpg")
            hover ("images/home/home_broken_with_cat_hover.jpg")
            insensitive ("images/home/home_broken_with_cat_hover.jpg")
        else:
            ground ("images/home/home_broken_with_dog.jpg")
            hover ("images/home/home_broken_with_dog_hover.jpg")
            insensitive ("images/home/home_broken_with_dog_hover.jpg")

        # 6 предметов - каждому свой хотспот

        hotspot (108, 61, 50, 68) action [SetVariable("first_document_finded", True), 
                                            Return("finded_first")] sensitive not first_document_finded

        hotspot (446, 380, 43, 46) action [SetVariable("second_document_finded", True),
                                            Return("finded_second")] sensitive not second_document_finded

        hotspot (809, 714, 47, 70) action [SetVariable("third_document_finded", True),
                                            Return("finded_third")] sensitive not third_document_finded

        hotspot (1539, 956, 132, 38) action [SetVariable("fourth_document_finded", True),
                                            Return("finded_fourth")] sensitive not fourth_document_finded

        hotspot (1592, 243, 47, 45) action [SetVariable("fifth_document_finded", True), 
                                            Return("finded_fifth")] sensitive not fifth_document_finded

    # Рамки вокруг уже выбранного предмета

    add "images/home/bg_for_icons.png" xalign 0.5

    showif first_document_finded: #
        add "images/home/icon_selected.png" xalign 0.355 yalign 0.03
    else:
        add "images/home/icon_unselected.png" xalign 0.355 yalign 0.03

    showif second_document_finded: 
        add "images/home/icon_uncorrect.png" xalign 0.430 yalign 0.03
    else:
        add "images/home/icon_unselected.png" xalign 0.430 yalign 0.03

    showif third_document_finded: #
        add "images/home/icon_selected.png" xalign 0.505 yalign 0.03
    else:
        add "images/home/icon_unselected.png" xalign 0.505 yalign 0.03

    showif fourth_document_finded: #
        add "images/home/icon_selected.png" xalign 0.580 yalign 0.03
    else:
        add "images/home/icon_unselected.png" xalign 0.580 yalign 0.03

    showif fifth_document_finded: 
        add "images/home/icon_uncorrect.png" xalign 0.655 yalign 0.03
    else:
        add "images/home/icon_unselected.png" xalign 0.655 yalign 0.03

screen studia_game():

    add "images/studia/studia_background.jpg"

    button:  ### дверь
        xysize(236, 938)
        xpos 1678
        ypos 86

        imagebutton:
            idle ("images/studia/objects/door_test.png")
            hover ("images/studia/objects/door_test_hover.png")
            insensitive ("images/studia/objects/door_test.png")

            action [SetVariable("door_open_finded", True),
                            Return ("door_open_finded")] sensitive not door_open_finded

    button:  ### окно
        xysize (337, 629)
        xpos -6
        ypos 76

        imagebutton:
            idle ("images/studia/objects/window_test.png")
            hover ("images/studia/objects/window_test_hover.png")
            insensitive ("images/studia/objects/window_test.png")

            action [SetVariable("window_finded", True),
                            Return ("window_finded")] sensitive not window_finded

                  
    button:  ### правый софит
        xysize(339, 700)
        xpos 1389
        ypos 374

        imagebutton:
            idle ("images/studia/objects/right_sofit_test.png")
            hover ("images/studia/objects/right_sofit_test_hover.png")
            insensitive ("images/studia/objects/right_sofit_test.png")

            action [SetVariable("sofits_finded", True),
                            Return ("sofits_finded")] sensitive not sofits_finded

    button:  ### левые софиты
        xysize(339, 700)
        xpos 129
        ypos 374

        imagebutton:
            idle ("images/studia/objects/left_sofits_test.png")
            hover ("images/studia/objects/left_sofits_test_hover.png")
            insensitive ("images/studia/objects/left_sofits_test.png")

            action [SetVariable("sofits_finded", True),
                            Return ("sofits_finded")] sensitive not sofits_finded

    button: ### суфлер
        xysize (395, 425)
        xpos 1197
        ypos 652

        imagebutton:
            idle ("images/studia/objects/sufler_test.png")
            hover ("images/studia/objects/sufler_test_hover.png")
            insensitive ("images/studia/objects/sufler_test.png")

            action [SetVariable("text_finded", True),
                            Return ("text_finded")] sensitive not text_finded                  

    button: ### Оператор
        xysize (359, 596)
        xpos 358
        ypos 478

        imagebutton: 
            idle ("images/studia/objects/operator1.png")
            hover ("images/studia/objects/operator_hover1.png")
            insensitive ("images/studia/objects/operator1.png")

            action [SetVariable("operator_finded", True),
                                Return ("operator_finded")] sensitive not operator_finded
   
    button: ### Автор - одежда
        xysize (213, 544)
        xpos 1021
        ypos 439

        imagebutton:
            idle ("images/studia/objects/author_garment_idle.png")
            hover ("images/studia/objects/author_garment_hover.png")
            insensitive ("images/studia/objects/author_garment_idle.png")

            action [SetVariable("author_garment_finded", True),
                                Return ("author_garment_finded")] sensitive not author_garment_finded
    
    button: ### Автор - рука
        xysize (199, 91)
        xpos 1150
        ypos 425

        imagebutton:
            idle ("images/studia/objects/author_hand_idle.png")
            hover ("images/studia/objects/author_hand_hover.png")
            insensitive ("images/studia/objects/author_hand_idle.png")

            action [SetVariable("author_hand_finded", True),
                                Return ("author_hand_finded")] sensitive not author_hand_finded

    button: ### Автор - голова
        xysize (129, 142)
        xpos 1048
        ypos 307

        imagebutton:
            idle ("images/studia/objects/author_head_idle.png")
            hover ("images/studia/objects/author_head_hover.png")
            insensitive ("images/studia/objects/author_head_idle.png")

            action [SetVariable("author_head_finded", True),
                                Return ("author_head_finded")] sensitive not author_head_finded

    button: ### Кнопка "Отправить"
        xysize (468, 102)
        xpos 1180
        ypos 20

        imagebutton:
            idle ("images/studia/objects/button_idle.png")
            hover ("images/studia/objects/button_hover.png")
            insensitive ("images/studia/objects/button_idle.png")

            action Return("send")


screen first_presentation(): #выравнивание

    imagemap:
        idle "images/presentations/1_wrong.png"
        hover "images/presentations/1_wrong_hover.png"

        hotspot (1494, 134, 401, 65) action [Return("viravnivanie")]

        hotspot (1494, 214, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_texta")]

        hotspot (1494, 294, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_plashek")]

        hotspot (1494, 375, 401, 65) action [SetVariable("k", k + 1), Return("kolichestvo_texta")]

        hotspot (1494, 456, 401, 65) action [SetVariable("k", k + 1), Return("pravilo_priblizhenia")]

        hotspot (1494, 539, 401, 65) action [SetVariable("k", k + 1), Return("gradient")]

        hotspot (1494, 618, 401, 65) action [SetVariable("k", k + 1), Return("raznaya_stilistika")]

        hotspot (1494, 698, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_vinosok")]

        hotspot (1494, 777, 401, 65) action [SetVariable("k", k + 1), Return("3D_effects")]

        hotspot (1494, 858, 401, 65) action [SetVariable("k", k + 1), Return("lishnie_elementi")]

        hotspot (1494, 939, 401, 65) action [SetVariable("k", k + 1), Return("narushenie_ierarhii")]

        hotspot (1839, 18, 47, 52) action [Return("exit")]

screen second_presentation(): #градиент
   
    imagemap:
        idle "images/presentations/2_wrong.png"
        hover "images/presentations/2_wrong_hover.png"

        hotspot (1494, 134, 401, 65) action [SetVariable("k", k + 1), Return("viravnivanie")]

        hotspot (1494, 214, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_texta")]

        hotspot (1494, 294, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_plashek")]

        hotspot (1494, 375, 401, 65) action [SetVariable("k", k + 1), Return("kolichestvo_texta")]

        hotspot (1494, 456, 401, 65) action [SetVariable("k", k + 1), Return("pravilo_priblizhenia")]

        hotspot (1494, 539, 401, 65) action [Return("gradient")]

        hotspot (1494, 618, 401, 65) action [SetVariable("k", k + 1), Return("raznaya_stilistika")]

        hotspot (1494, 698, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_vinosok")]

        hotspot (1494, 777, 401, 65) action [SetVariable("k", k + 1), Return("3D_effects")]

        hotspot (1494, 858, 401, 65) action [SetVariable("k", k + 1), Return("lishnie_elementi")]

        hotspot (1494, 939, 401, 65) action [SetVariable("k", k + 1), Return("narushenie_ierarhii")]

        hotspot (1839, 18, 47, 52) action [Return("exit")]

screen third_presentation(): #количество текста

    imagemap:

        idle "images/presentations/3_wrong.png"
        hover "images/presentations/3_wrong_hover.png"

        hotspot (1494, 134, 401, 65) action [SetVariable("k", k + 1), Return("viravnivanie")]

        hotspot (1494, 214, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_texta")]

        hotspot (1494, 294, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_plashek")]

        hotspot (1494, 375, 401, 65) action [Return("kolichestvo_texta")]

        hotspot (1494, 456, 401, 65) action [SetVariable("k", k + 1), Return("pravilo_priblizhenia")]

        hotspot (1494, 539, 401, 65) action [SetVariable("k", k + 1), Return("gradient")]

        hotspot (1494, 618, 401, 65) action [SetVariable("k", k + 1), Return("raznaya_stilistika")]

        hotspot (1494, 698, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_vinosok")]

        hotspot (1494, 777, 401, 65) action [SetVariable("k", k + 1), Return("3D_effects")]

        hotspot (1494, 858, 401, 65) action [SetVariable("k", k + 1), Return("lishnie_elementi")]

        hotspot (1494, 939, 401, 65) action [SetVariable("k", k + 1), Return("narushenie_ierarhii")]

        hotspot (1839, 18, 47, 52) action [Return("exit")]

screen fouth_presentation(): #лишние элементы

    imagemap:

        idle "images/presentations/4_wrong.png"
        hover "images/presentations/4_wrong_hover.png"

        hotspot (1494, 134, 401, 65) action [SetVariable("k", k + 1), Return("viravnivanie")]

        hotspot (1494, 214, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_texta")]

        hotspot (1494, 294, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_plashek")]

        hotspot (1494, 375, 401, 65) action [SetVariable("k", k + 1), Return("kolichestvo_texta")]

        hotspot (1494, 456, 401, 65) action [SetVariable("k", k + 1), Return("pravilo_priblizhenia")]

        hotspot (1494, 539, 401, 65) action [SetVariable("k", k + 1), Return("gradient")]

        hotspot (1494, 618, 401, 65) action [SetVariable("k", k + 1), Return("raznaya_stilistika")]

        hotspot (1494, 698, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_vinosok")]

        hotspot (1494, 777, 401, 65) action [SetVariable("k", k + 1), Return("3D_effects")]

        hotspot (1494, 858, 401, 65) action [Return("lishnie_elementi")]

        hotspot (1494, 939, 401, 65) action [SetVariable("k", k + 1), Return("narushenie_ierarhii")]

        hotspot (1839, 18, 47, 52) action [Return("exit")]


screen fifth_presentation(): #нарушение иерархии

    imagemap:

        idle "images/presentations/5_wrong.png"
        hover "images/presentations/5_wrong_hover.png"

        hotspot (1494, 134, 401, 65) action [SetVariable("k", k + 1), Return("viravnivanie")]

        hotspot (1494, 214, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_texta")]

        hotspot (1494, 294, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_plashek")]

        hotspot (1494, 375, 401, 65) action [SetVariable("k", k + 1), Return("kolichestvo_texta")]

        hotspot (1494, 456, 401, 65) action [SetVariable("k", k + 1), Return("pravilo_priblizhenia")]

        hotspot (1494, 539, 401, 65) action [SetVariable("k", k + 1), Return("gradient")]

        hotspot (1494, 618, 401, 65) action [SetVariable("k", k + 1), Return("raznaya_stilistika")]

        hotspot (1494, 698, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_vinosok")]

        hotspot (1494, 777, 401, 65) action [SetVariable("k", k + 1), Return("3D_effects")]

        hotspot (1494, 858, 401, 65) action [SetVariable("k", k + 1), Return("lishnie_elementi")]

        hotspot (1494, 939, 401, 65) action [Return("narushenie_ierarhii")]

        hotspot (1839, 18, 47, 52) action [Return("exit")]

   
screen six_presentation(): #оформление выносок

    imagemap:

        idle "images/presentations/6_wrong.png"
        hover "images/presentations/6_wrong_hover.png"

        hotspot (1494, 134, 401, 65) action [SetVariable("k", k + 1), Return("viravnivanie")]

        hotspot (1494, 214, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_texta")]

        hotspot (1494, 294, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_plashek")]

        hotspot (1494, 375, 401, 65) action [SetVariable("k", k + 1), Return("kolichestvo_texta")]

        hotspot (1494, 456, 401, 65) action [SetVariable("k", k + 1), Return("pravilo_priblizhenia")]

        hotspot (1494, 539, 401, 65) action [SetVariable("k", k + 1), Return("gradient")]

        hotspot (1494, 618, 401, 65) action [SetVariable("k", k + 1), Return("raznaya_stilistika")]

        hotspot (1494, 698, 401, 65) action [Return("oformlenie_vinosok")]

        hotspot (1494, 777, 401, 65) action [SetVariable("k", k + 1), Return("3D_effects")]

        hotspot (1494, 858, 401, 65) action [SetVariable("k", k + 1), Return("lishnie_elementi")]

        hotspot (1494, 939, 401, 65) action [SetVariable("k", k + 1), Return("narushenie_ierarhii")]

        hotspot (1839, 18, 47, 52) action [Return("exit")]


screen seven_presentation(): #оформление текста

    imagemap:

        idle "images/presentations/7_wrong.png"
        hover "images/presentations/7_wrong_hover.png"

        hotspot (1494, 134, 401, 65) action [SetVariable("k", k + 1), Return("viravnivanie")]

        hotspot (1494, 214, 401, 65) action [Return("oformlenie_texta")]

        hotspot (1494, 294, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_plashek")]

        hotspot (1494, 375, 401, 65) action [SetVariable("k", k + 1), Return("kolichestvo_texta")]

        hotspot (1494, 456, 401, 65) action [SetVariable("k", k + 1), Return("pravilo_priblizhenia")]

        hotspot (1494, 539, 401, 65) action [SetVariable("k", k + 1), Return("gradient")]

        hotspot (1494, 618, 401, 65) action [SetVariable("k", k + 1), Return("raznaya_stilistika")]

        hotspot (1494, 698, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_vinosok")]

        hotspot (1494, 777, 401, 65) action [SetVariable("k", k + 1), Return("3D_effects")]

        hotspot (1494, 858, 401, 65) action [SetVariable("k", k + 1), Return("lishnie_elementi")]

        hotspot (1494, 939, 401, 65) action [SetVariable("k", k + 1), Return("narushenie_ierarhii")]

        hotspot (1839, 18, 47, 52) action [Return("exit")]


screen eight_presentation(): #правило приближения

    imagemap:

        idle "images/presentations/8_wrong.png"
        hover "images/presentations/8_wrong_hover.png"

        hotspot (1494, 134, 401, 65) action [SetVariable("k", k + 1), Return("viravnivanie")]

        hotspot (1494, 214, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_texta")]

        hotspot (1494, 294, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_plashek")]

        hotspot (1494, 375, 401, 65) action [SetVariable("k", k + 1), Return("kolichestvo_texta")]

        hotspot (1494, 456, 401, 65) action [Return("pravilo_priblizhenia")]

        hotspot (1494, 539, 401, 65) action [SetVariable("k", k + 1), Return("gradient")]

        hotspot (1494, 618, 401, 65) action [SetVariable("k", k + 1), Return("raznaya_stilistika")]

        hotspot (1494, 698, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_vinosok")]

        hotspot (1494, 777, 401, 65) action [SetVariable("k", k + 1), Return("3D_effects")]

        hotspot (1494, 858, 401, 65) action [SetVariable("k", k + 1), Return("lishnie_elementi")]

        hotspot (1494, 939, 401, 65) action [SetVariable("k", k + 1), Return("narushenie_ierarhii")]

        hotspot (1839, 18, 47, 52) action [Return("exit")]


screen nine_presentation(): #оформление плашек

    imagemap:

        idle "images/presentations/9_wrong.png"
        hover "images/presentations/9_wrong_hover.png"

        hotspot (1494, 134, 401, 65) action [SetVariable("k", k + 1), Return("viravnivanie")]

        hotspot (1494, 214, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_texta")]

        hotspot (1494, 294, 401, 65) action [Return("oformlenie_plashek")]

        hotspot (1494, 375, 401, 65) action [SetVariable("k", k + 1), Return("kolichestvo_texta")]

        hotspot (1494, 456, 401, 65) action [SetVariable("k", k + 1), Return("pravilo_priblizhenia")]

        hotspot (1494, 539, 401, 65) action [SetVariable("k", k + 1), Return("gradient")]

        hotspot (1494, 618, 401, 65) action [SetVariable("k", k + 1), Return("raznaya_stilistika")]

        hotspot (1494, 698, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_vinosok")]

        hotspot (1494, 777, 401, 65) action [SetVariable("k", k + 1), Return("3D_effects")]

        hotspot (1494, 858, 401, 65) action [SetVariable("k", k + 1), Return("lishnie_elementi")]

        hotspot (1494, 939, 401, 65) action [SetVariable("k", k + 1), Return("narushenie_ierarhii")]

        hotspot (1839, 18, 47, 52) action [Return("exit")]


screen ten_presentation(): #разная стилистика

    imagemap:

        idle "images/presentations/10_wrong.png"
        hover "images/presentations/10_wrong_hover.png"

        hotspot (1494, 134, 401, 65) action [SetVariable("k", k + 1), Return("viravnivanie")]

        hotspot (1494, 214, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_texta")]

        hotspot (1494, 294, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_plashek")]

        hotspot (1494, 375, 401, 65) action [SetVariable("k", k + 1), Return("kolichestvo_texta")]

        hotspot (1494, 456, 401, 65) action [SetVariable("k", k + 1), Return("pravilo_priblizhenia")]

        hotspot (1494, 539, 401, 65) action [SetVariable("k", k + 1), Return("gradient")]

        hotspot (1494, 618, 401, 65) action [Return("raznaya_stilistika")]

        hotspot (1494, 698, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_vinosok")]

        hotspot (1494, 777, 401, 65) action [SetVariable("k", k + 1), Return("3D_effects")]

        hotspot (1494, 858, 401, 65) action [SetVariable("k", k + 1), Return("lishnie_elementi")]

        hotspot (1494, 939, 401, 65) action [SetVariable("k", k + 1), Return("narushenie_ierarhii")]

        hotspot (1839, 18, 47, 52) action [Return("exit")]


screen eleven_presentation(): #схемы из интернета

    imagemap:

        idle "images/presentations/11_wrong.png"
        hover "images/presentations/11_wrong_hover.png"

        hotspot (1494, 134, 401, 65) action [SetVariable("k", k + 1), Return("viravnivanie")]

        hotspot (1494, 214, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_texta")]

        hotspot (1494, 294, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_plashek")]

        hotspot (1494, 375, 401, 65) action [SetVariable("k", k + 1), Return("kolichestvo_texta")]

        hotspot (1494, 456, 401, 65) action [SetVariable("k", k + 1), Return("pravilo_priblizhenia")]

        hotspot (1494, 539, 401, 65) action [SetVariable("k", k + 1), Return("gradient")]

        hotspot (1494, 618, 401, 65) action [SetVariable("k", k + 1), Return("raznaya_stilistika")]

        hotspot (1494, 698, 401, 65) action [SetVariable("k", k + 1), Return("oformlenie_vinosok")]

        hotspot (1494, 777, 401, 65) action [Return("3D_effects")]

        hotspot (1494, 858, 401, 65) action [SetVariable("k", k + 1), Return("lishnie_elementi")]

        hotspot (1494, 939, 401, 65) action [SetVariable("k", k + 1), Return("narushenie_ierarhii")]

        hotspot (1839, 18, 47, 52) action [Return("exit")]

screen final_for_presentations():
    imagemap:

        idle "images/presentations/11_right.png"
        hover "images/presentations/11_right.png"

        add "images/arrows/arrow_right_3.png" at arrow_move(0.93, 0.0)
        
        hotspot (1839, 18, 47, 52) action [Return("exit")]

init python:
    def Set_new_value(i, value):
        lst[i] = value

    def text_array_change(col):
        if col:
            for i in range(110):
                if lst[i] and i != 2 and i != 7 and i != 11 and i != 35 and i != 50 and i != 56 and i != 59 and i != 67 and i != 81  and i != 86  and i != 99 and i != 104:
                    lst[i] = False
            for i in range(110):
                lst2[i] = lst[i]


screen text_mini_game():   ##### Мини-игра "Текст" #####
    imagemap:
        idle "images/text/text.png"
        hover "images/text/text_hover2.png"
        selected_idle "images/text/text_red.png"
        selected_hover "images/text/text_hover2.png"
        insensitive "images/text/text_red.png"

        showif game_over:
            add "images/arrows/arrow_right_3.png" at arrow_move(0.93, 0.0)

        hotspot (427, 199, 84, 26) action If(z < 12 or lst[0], [SetVariable("z", If(lst[0], z - 1, z + 1)), 
                                SelectedIf(lst[0] or lst2[0]), Function(Set_new_value, 0, If(lst[0], False, True)), Return("")], [SelectedIf(lst[0] or lst2[0]), Return("")])

        hotspot (522, 205, 109, 20) action If(z < 12 or lst[1], [SetVariable("z", If(lst[1], z - 1, z + 1)), 
                                SelectedIf(lst[1] == True), Function(Set_new_value, 1, If(lst[1], False, True)), Return("")], [SelectedIf(lst[1] or lst2[1]), Return("")])

        hotspot (692, 205, 59, 20) action If(z < 12 or lst[2], [SetVariable("z", If(lst[2], z - 1, z + 1)), SetVariable("right_choise", If(lst[2], right_choise - 1, right_choise + 1)), 
                                SensitiveIf(lst2[2] == False), SelectedIf(lst[2] or lst2[2]), Function(Set_new_value, 2, If(lst[2], False, True)), Return("T")], [SelectedIf(lst[2] or lst2[2]), Return("")])

        hotspot (764, 205, 82, 27) action If(z < 12 or lst[3], [SetVariable("z", If(lst[3], z - 1, z + 1)), 
                                SelectedIf(lst[3] == True), Function(Set_new_value, 3, If(lst[3], False, True)), Return("")], [SelectedIf(lst[3] or lst2[3]), Return("")])

        hotspot (857, 205, 101, 20) action If(z < 12 or lst[4], [SetVariable("z", If(lst[4], z - 1, z + 1)),
                                SelectedIf(lst[4] == True), Function(Set_new_value, 4, If(lst[4], False, True)), Return("")], [SelectedIf(lst[4] or lst2[4]), Return("")])

        hotspot (978, 205, 49, 20) action If(z < 12 or lst[5], [SetVariable("z", If(lst[5], z - 1, z + 1)),
                                SelectedIf(lst[5] == True), Function(Set_new_value, 5, If(lst[5], False, True)), Return("")], [SelectedIf(lst[5] or lst2[5]), Return("")])

        hotspot (1039, 205, 184, 26) action If(z < 12 or lst[6], [SetVariable("z", If(lst[6], z - 1, z + 1)), 
                                SelectedIf(lst[6] == True), Function(Set_new_value, 6, If(lst[6], False, True)), Return("")], [SelectedIf(lst[6] or lst2[6]), Return("")])
                                
        hotspot (1234, 205, 97, 20) action If(z < 12 or lst[7], [SetVariable("z", If(lst[7], z - 1, z + 1)), SensitiveIf(lst2[7] == False), SetVariable("right_choise", If(lst[7], right_choise - 1, right_choise + 1)),
                                SelectedIf(lst[7] or lst2[7]), Function(Set_new_value, 7, If(lst[7], False, True)), Return("T")], [SelectedIf(lst[7] or lst2[7]), Return("")])

        hotspot (1341, 205, 99, 20) action If(z < 12 or lst[8], [SetVariable("z", If(lst[8], z - 1, z + 1)),
                                SelectedIf(lst[8] == True), Function(Set_new_value, 8, If(lst[8], False, True)), Return("")], [SelectedIf(lst[8] or lst2[8]), Return("")])

        hotspot (430, 245, 110, 20) action If(z < 12 or lst[9], [SetVariable("z", If(lst[9], z - 1, z + 1)),
                                SelectedIf(lst[9] == True), Function(Set_new_value, 9, If(lst[9], False, True)), Return("")], [SelectedIf(lst[9] or lst2[9]), Return("")])

        hotspot (614, 245, 127, 20) action If(z < 12 or lst[10], [SetVariable("z", If(lst[10], z - 1, z + 1)),
                                SelectedIf(lst[10] == True), Function(Set_new_value, 10, If(lst[10], False, True)), Return("")], [SelectedIf(lst[10] or lst2[10]), Return("")])

        hotspot (762, 245, 147, 26) action If(z < 12 or lst[11], [SetVariable("z", If(lst[11], z - 1, z + 1)), SensitiveIf(lst2[11] == False), SetVariable("right_choise", If(lst[11], right_choise - 1, right_choise + 1)),
                                SelectedIf(lst[11] or lst2[11]), Function(Set_new_value, 11, If(lst[11], False, True)), Return("T")], [SelectedIf(lst[11] or lst2[11]), Return("")])

        hotspot (930, 245, 18, 20) action If(z < 12 or lst[13], [SetVariable("z", If(lst[13], z - 1, z + 1)),
                                SelectedIf(lst[13] == True), Function(Set_new_value, 13, If(lst[13], False, True)), Return("")], [SelectedIf(lst[13] or lst2[13]), Return("")])

        hotspot (961, 245, 53, 20) action If(z < 12 or lst[14], [SetVariable("z", If(lst[14], z - 1, z + 1)),
                                SelectedIf(lst[14] == True), Function(Set_new_value, 14, If(lst[14], False, True)), Return("")], [SelectedIf(lst[14] or lst2[14]), Return("")])

        hotspot (1024, 245, 186, 20) action If(z < 12 or lst[15], [SetVariable("z", If(lst[15], z - 1, z + 1)),
                                SelectedIf(lst[15] == True), Function(Set_new_value, 15, If(lst[15], False, True)), Return("")], [SelectedIf(lst[15] or lst2[15]), Return("")])

        hotspot (1220, 245, 126, 20) action If(z < 12 or lst[16], [SetVariable("z", If(lst[16], z - 1, z + 1)),
                                SelectedIf(lst[16] == True), Function(Set_new_value, 16, If(lst[16], False, True)), Return("")], [SelectedIf(lst[16] or lst2[16]), Return("")])

        hotspot (1374, 239, 52, 26) action If(z < 12 or lst[17], [SetVariable("z", If(lst[17], z - 1, z + 1)),
                                SelectedIf(lst[17] == True), Function(Set_new_value, 17, If(lst[17], False, True)), Return("")], [SelectedIf(lst[17] or lst2[17]), Return("")])

        hotspot (430, 286, 50, 20) action If(z < 12 or lst[18], [SetVariable("z", If(lst[18], z - 1, z + 1)),
                                SelectedIf(lst[18] == True), Function(Set_new_value, 18, If(lst[18], False, True)), Return("")], [SelectedIf(lst[18] or lst2[18]), Return("")])

        hotspot (492, 286, 42, 20) action If(z < 12 or lst[19], [SetVariable("z", If(lst[19], z - 1, z + 1)),
                                SelectedIf(lst[19] == True), Function(Set_new_value, 19, If(lst[19], False, True)), Return("")], [SelectedIf(lst[19] or lst2[19]), Return("")])

        hotspot (545, 286, 127, 26) action If(z < 12 or lst[20], [SetVariable("z", If(lst[20], z - 1, z + 1)),
                                SelectedIf(lst[20] == True), Function(Set_new_value, 20, If(lst[20], False, True)), Return("")], [SelectedIf(lst[20] or lst2[20]), Return("")])

        hotspot (692, 277, 97, 31) action If(z < 12 or lst[21], [SetVariable("z", If(lst[21], z - 1, z + 1)),
                                SelectedIf(lst[21] == True), Function(Set_new_value, 21, If(lst[21], False, True)), Return("")], [SelectedIf(lst[21] or lst2[21]), Return("")])

        hotspot (801, 286, 144, 20) action If(z < 12 or lst[22], [SetVariable("z", If(lst[22], z - 1, z + 1)),
                                SelectedIf(lst[22] == True), Function(Set_new_value, 22, If(lst[22], False, True)), Return("")], [SelectedIf(lst[22] or lst2[22]), Return("")])

        hotspot (955, 286, 34, 20) action If(z < 12 or lst[23], [SetVariable("z", If(lst[23], z - 1, z + 1)),
                                SelectedIf(lst[23] == True), Function(Set_new_value, 23, If(lst[23], False, True)), Return("")], [SelectedIf(lst[23] or lst2[23]), Return("")])

        hotspot (1000, 279, 283, 33) action If(z < 12 or lst[24], [SetVariable("z", If(lst[24], z - 1, z + 1)),
                                SelectedIf(lst[24] == True), Function(Set_new_value, 24, If(lst[24], False, True)), Return("")], [SelectedIf(lst[24] or lst2[24]), Return("")])

        hotspot (1297, 286, 123, 26) action If(z < 12 or lst[25], [SetVariable("z", If(lst[25], z - 1, z + 1)),
                                SelectedIf(lst[25] == True), Function(Set_new_value, 25, If(lst[25], False, True)), Return("")], [SelectedIf(lst[25] or lst2[25]), Return("")])

        hotspot (455, 319, 167, 26) action If(z < 12 or lst[26], [SetVariable("z", If(lst[26], z - 1, z + 1)),
                                SelectedIf(lst[26] == True), Function(Set_new_value, 26, If(lst[26], False, True)), Return("")], [SelectedIf(lst[26] or lst2[26]), Return("")])

        hotspot (430, 359, 300, 33) action If(z < 12 or lst[27], [SetVariable("z", If(lst[27], z - 1, z + 1)),
                                SelectedIf(lst[27] == True), Function(Set_new_value, 27, If(lst[27], False, True)), Return("")], [SelectedIf(lst[27] or lst2[27]), Return("")])

        hotspot (743,  358, 123, 27) action If(z < 12 or lst[28], [SetVariable("z", If(lst[28], z - 1, z + 1)),
                                SelectedIf(lst[28] == True), Function(Set_new_value, 28, If(lst[28], False, True)), Return("")], [SelectedIf(lst[28] or lst2[28]), Return("")])

        hotspot (880, 366, 128, 26) action If(z < 12 or lst[29], [SetVariable("z", If(lst[29], z - 1, z + 1)),
                                SelectedIf(lst[29] == True), Function(Set_new_value, 29, If(lst[29], False, True)), Return("")], [SelectedIf(lst[29] or lst2[29]), Return("")])

        hotspot (1050, 366, 202, 26) action If(z < 12 or lst[30], [SetVariable("z", If(lst[30], z - 1, z + 1)),
                                SelectedIf(lst[30] == True), Function(Set_new_value, 30, If(lst[30], False, True)), Return("")], [SelectedIf(lst[30] or lst2[30]), Return("")])

        hotspot (1263, 366, 201, 26) action If(z < 12 or lst[31], [SetVariable("z", If(lst[31], z - 1, z + 1)),
                                SelectedIf(lst[31] == True), Function(Set_new_value, 31, If(lst[31], False, True)), Return("")], [SelectedIf(lst[31] or lst2[31]), Return("")])

        hotspot (427, 406, 99, 20) action If(z < 12 or lst[32], [SetVariable("z", If(lst[32], z - 1, z + 1)),
                                SelectedIf(lst[32] == True), Function(Set_new_value, 32, If(lst[32], False, True)), Return("")], [SelectedIf(lst[32] or lst2[32]), Return("")])

        hotspot (550, 398, 323, 34) action If(z < 12 or lst[33], [SetVariable("z", If(lst[33], z - 1, z + 1)),
                                SelectedIf(lst[33] == True), Function(Set_new_value, 33, If(lst[33], False, True)), Return("")], [SelectedIf(lst[33] or lst2[33]), Return("")])

        hotspot (918, 406, 239, 26) action If(z < 12 or lst[34], [SetVariable("z", If(lst[34], z - 1, z + 1)),
                                SelectedIf(lst[34] == True), Function(Set_new_value, 34, If(lst[34], False, True)), Return("")], [SelectedIf(lst[34] or lst2[34]), Return("")])


        hotspot (1172, 406, 290, 26) action If(z < 12 or lst[35], [SetVariable("z", If(lst[35], z - 1, z + 1)), SensitiveIf(lst2[35] == False), SetVariable("right_choise", If(lst[35], right_choise - 1, right_choise + 1)),
                                SelectedIf(lst[35] or lst2[35]), Function(Set_new_value, 35, If(lst[35], False, True)), Return("T")], [SelectedIf(lst[35] or lst2[35]), Return("")])

        hotspot (430, 446, 184, 26) action If(z < 12 or lst[36], [SetVariable("z", If(lst[36], z - 1, z + 1)),
                                SelectedIf(lst[36] == True), Function(Set_new_value, 36, If(lst[36], False, True)), Return("")], [SelectedIf(lst[36] or lst2[36]), Return("")])

        hotspot (627, 440, 278, 25) action If(z < 12 or lst[37], [SetVariable("z", If(lst[37], z - 1, z + 1)),
                                SelectedIf(lst[37] == True), Function(Set_new_value, 37, If(lst[37], False, True)), Return("")], [SelectedIf(lst[37] or lst2[37]), Return("")])

        hotspot (919, 446, 57, 20) action If(z < 12 or lst[38], [SetVariable("z", If(lst[38], z - 1, z + 1)),
                                SelectedIf(lst[38] == True), Function(Set_new_value, 38, If(lst[38], False, True)), Return("")], [SelectedIf(lst[38] or lst2[38]), Return("")])

        hotspot (989, 440, 301, 32) action If(z < 12 or lst[39], [SetVariable("z", If(lst[39], z - 1, z + 1)),
                                SelectedIf(lst[39] == True), Function(Set_new_value, 39, If(lst[39], False, True)), Return("")], [SelectedIf(lst[39] or lst2[39]), Return("")])

        hotspot (1314, 446, 84, 25) action If(z < 12 or lst[40], [SetVariable("z", If(lst[40], z - 1, z + 1)),
                                SelectedIf(lst[40] == True), Function(Set_new_value, 40, If(lst[40], False, True)), Return("")], [SelectedIf(lst[40] or lst2[40]), Return("")])
                                
        hotspot (1413, 440, 50, 26) action If(z < 12 or lst[41], [SetVariable("z", If(lst[41], z - 1, z + 1)),
                                SelectedIf(lst[41] == True), Function(Set_new_value, 41, If(lst[41], False, True)), Return("")], [SelectedIf(lst[41] or lst2[41]), Return("")])

        hotspot (427, 486, 116, 25) action If(z < 12 or lst[42], [SetVariable("z", If(lst[42], z - 1, z + 1)),
                                SelectedIf(lst[42] == True), Function(Set_new_value, 42, If(lst[42], False, True)), Return("")], [SelectedIf(lst[42] or lst2[42]), Return("")])

        hotspot (556, 486, 206, 25) action If(z < 12 or lst[43], [SetVariable("z", If(lst[43], z - 1, z + 1)),
                                SelectedIf(lst[43] == True), Function(Set_new_value, 43, If(lst[43], False, True)), Return("")], [SelectedIf(lst[43] or lst2[43]), Return("")])

        hotspot (794, 480, 101, 25) action If(z < 12 or lst[44], [SetVariable("z", If(lst[44], z - 1, z + 1)),
                                SelectedIf(lst[44] == True), Function(Set_new_value, 44, If(lst[44], False, True)), Return("")], [SelectedIf(lst[44] or lst2[44]), Return("")])

        hotspot (910, 477, 76, 28) action If(z < 12 or lst[45], [SetVariable("z", If(lst[45], z - 1, z + 1)),
                                SelectedIf(lst[45] == True), Function(Set_new_value, 45, If(lst[45], False, True)), Return("")], [SelectedIf(lst[45] or lst2[45]), Return("")])

        hotspot (998, 486, 194, 20) action If(z < 12 or lst[46], [SetVariable("z", If(lst[46], z - 1, z + 1)),
                                SelectedIf(lst[46] == True), Function(Set_new_value, 46, If(lst[46], False, True)), Return("")], [SelectedIf(lst[46] or lst2[46]), Return("")])

        hotspot (1252, 486, 107, 25) action If(z < 12 or lst[47], [SetVariable("z", If(lst[47], z - 1, z + 1)),
                                SelectedIf(lst[47] == True), Function(Set_new_value, 47, If(lst[47], False, True)), Return("")], [SelectedIf(lst[47] or lst2[47]), Return("")])

        hotspot (1370, 486, 115, 26) action If(z < 12 or lst[48], [SetVariable("z", If(lst[48], z - 1, z + 1)),
                                SelectedIf(lst[48] == True), Function(Set_new_value, 48, If(lst[48], False, True)), Return("")], [SelectedIf(lst[48] or lst2[48]), Return("")])

        hotspot (430, 520, 204, 32) action If(z < 12 or lst[49], [SetVariable("z", If(lst[49], z - 1, z + 1)),
                                SelectedIf(lst[49] == True), Function(Set_new_value, 49, If(lst[49], False, True)), Return("")], [SelectedIf(lst[49] or lst2[49]), Return("")])

        hotspot (644, 518, 270, 27) action If(z < 12 or lst[50], [SetVariable("z", If(lst[50], z - 1, z + 1)), SensitiveIf(lst2[50] == False), SetVariable("right_choise", If(lst[50], right_choise - 1, right_choise + 1)),
                                SelectedIf(lst[50] or lst2[50]), Function(Set_new_value, 50, If(lst[50], False, True)), Return("T")], [SelectedIf(lst[50] or lst2[50]), Return("")])

        hotspot (928, 518, 272, 34) action If(z < 12 or lst[51], [SetVariable("z", If(lst[51], z - 1, z + 1)),
                                SelectedIf(lst[51] == True), Function(Set_new_value, 51, If(lst[51], False, True)), Return("")], [SelectedIf(lst[51] or lst2[51]), Return("")])

        hotspot (430, 566, 196, 26) action If(z < 12 or lst[52], [SetVariable("z", If(lst[52], z - 1, z + 1)),
                                SelectedIf(lst[52] == True), Function(Set_new_value, 52, If(lst[52], False, True)), Return("")], [SelectedIf(lst[52] or lst2[52]), Return("")])

        hotspot (647, 566, 51, 20) action If(z < 12 or lst[53], [SetVariable("z", If(lst[53], z - 1, z + 1)),
                                SelectedIf(lst[53] == True), Function(Set_new_value, 53, If(lst[53], False, True)), Return("")], [SelectedIf(lst[53] or lst2[53]), Return("")])

        hotspot (711, 566, 40, 20) action If(z < 12 or lst[54], [SetVariable("z", If(lst[54], z - 1, z + 1)),
                                SelectedIf(lst[54] == True), Function(Set_new_value, 54, If(lst[54], False, True)), Return("")], [SelectedIf(lst[54] or lst2[54]), Return("")])

        hotspot (566, 763, 321, 20) action If(z < 12 or lst[55], [SetVariable("z", If(lst[55], z - 1, z + 1)),
                                SelectedIf(lst[55] == True), Function(Set_new_value, 55, If(lst[55], False, True)), Return("")], [SelectedIf(lst[55] or lst2[55]), Return("")])

        hotspot (898, 558, 74, 27) action If(z < 12 or lst[56], [SetVariable("z", If(lst[56], z - 1, z + 1)), SensitiveIf(lst2[56] == False), SetVariable("right_choise", If(lst[56], right_choise - 1, right_choise + 1)),
                                SelectedIf(lst[56] or lst2[56]), Function(Set_new_value, 56, If(lst[56], False, True)), Return("T")], [SelectedIf(lst[56] or lst2[56]), Return("")])

        hotspot (983, 566, 83, 20) action If(z < 12 or lst[57], [SetVariable("z", If(lst[57], z - 1, z + 1)),
                                SelectedIf(lst[57] == True), Function(Set_new_value, 57, If(lst[57], False, True)), Return("")], [SelectedIf(lst[57] or lst2[57]), Return("")])

        hotspot (1078, 566, 158, 26) action If(z < 12 or lst[58], [SetVariable("z", If(lst[58], z - 1, z + 1)),
                                SelectedIf(lst[58] == True), Function(Set_new_value, 58, If(lst[58], False, True)), Return("")], [SelectedIf(lst[58] or lst2[58]), Return("")])

        hotspot (1256, 566, 169, 26) action If(z < 12 or lst[59], [SetVariable("z", If(lst[59], z - 1, z + 1)), SensitiveIf(lst2[59] == False), SetVariable("right_choise", If(lst[59], right_choise - 1, right_choise + 1)),
                                SelectedIf(lst[59] or lst2[59]), Function(Set_new_value, 59, If(lst[59], False, True)), Return("T")], [SelectedIf(lst[59] or lst2[59]), Return("")])

        hotspot (430, 606, 198, 26) action If(z < 12 or lst[59], [SetVariable("z", If(lst[59], z - 1, z + 1)), SensitiveIf(lst2[59] == False), SetVariable("right_choise", If(lst[59], right_choise - 1, right_choise + 1)),
                                SelectedIf(lst[59] or lst2[59]), Function(Set_new_value, 59, If(lst[59], False, True)), Return("T")], [SelectedIf(lst[59] or lst2[59]), Return("")])

        hotspot (637, 606, 137, 26) action If(z < 12 or lst[60], [SetVariable("z", If(lst[60], z - 1, z + 1)),
                                SelectedIf(lst[60] == True), Function(Set_new_value, 60, If(lst[60], False, True)), Return("")], [SelectedIf(lst[60] or lst2[60]), Return("")])

        hotspot (788, 598, 159, 35) action If(z < 12 or lst[61], [SetVariable("z", If(lst[61], z - 1, z + 1)),
                                SelectedIf(lst[61] == True), Function(Set_new_value, 61, If(lst[61], False, True)), Return("")], [SelectedIf(lst[61] or lst2[61]), Return("")])

        hotspot (999, 606, 65, 26) action If(z < 12 or lst[62], [SetVariable("z", If(lst[62], z - 1, z + 1)),
                                SelectedIf(lst[62] == True), Function(Set_new_value, 62, If(lst[62], False, True)), Return("")], [SelectedIf(lst[62] or lst2[62]), Return("")])

        hotspot (1075, 606, 102, 26) action If(z < 12 or lst[63], [SetVariable("z", If(lst[63], z - 1, z + 1)),
                                SelectedIf(lst[63] == True), Function(Set_new_value, 63, If(lst[63], False, True)), Return("")], [SelectedIf(lst[63] or lst2[63]), Return("")])

        hotspot (1197, 598, 94, 34) action If(z < 12 or lst[64], [SetVariable("z", If(lst[64], z - 1, z + 1)),
                                SelectedIf(lst[64] == True), Function(Set_new_value, 64, If(lst[64], False, True)), Return("")], [SelectedIf(lst[64] or lst2[64]), Return("")])

        hotspot (1304, 606, 164, 26) action If(z < 12 or lst[65], [SetVariable("z", If(lst[65], z - 1, z + 1)),
                                SelectedIf(lst[65] == True), Function(Set_new_value, 65, If(lst[65], False, True)), Return("")], [SelectedIf(lst[65] or lst2[65]), Return("")])

        hotspot (427, 646, 81, 20) action If(z < 12 or lst[66], [SetVariable("z", If(lst[66], z - 1, z + 1)),
                                SelectedIf(lst[66] == True), Function(Set_new_value, 66, If(lst[66], False, True)), Return("")], [SelectedIf(lst[66] or lst2[66]), Return("")])

        hotspot (519, 638, 346, 34) action If(z < 12 or lst[67], [SetVariable("z", If(lst[67], z - 1, z + 1)), SensitiveIf(lst2[67] == False), SetVariable("right_choise", If(lst[67], right_choise - 1, right_choise + 1)),
                                SelectedIf(lst[67] or lst2[67]), Function(Set_new_value, 67, If(lst[67], False, True)), Return("T")], [SelectedIf(lst[67] or lst2[67]), Return("")])

        hotspot (882, 646, 88, 26) action If(z < 12 or lst[68], [SetVariable("z", If(lst[68], z - 1, z + 1)),
                                SelectedIf(lst[68] == True), Function(Set_new_value, 68, If(lst[68], False, True)), Return("")], [SelectedIf(lst[68] or lst2[68]), Return("")])

        hotspot (990, 646, 122, 20) action If(z < 12 or lst[69], [SetVariable("z", If(lst[69], z - 1, z + 1)),
                                SelectedIf(lst[69] == True), Function(Set_new_value, 69, If(lst[69], False, True)), Return("")], [SelectedIf(lst[69] or lst2[69]), Return("")])

        hotspot (1130, 638, 333, 34) action If(z < 12 or lst[70], [SetVariable("z", If(lst[70], z - 1, z + 1)),
                                SelectedIf(lst[70] == True), Function(Set_new_value, 70, If(lst[70], False, True)), Return("")], [SelectedIf(lst[70] or lst2[70]), Return("")])

        hotspot (430, 680, 70, 26) action If(z < 12 or lst[71], [SetVariable("z", If(lst[71], z - 1, z + 1)),
                                SelectedIf(lst[71] == True), Function(Set_new_value, 71, If(lst[71], False, True)), Return("")], [SelectedIf(lst[71] or lst2[71]), Return("")])

        hotspot (512, 686, 61, 26) action If(z < 12 or lst[72], [SetVariable("z", If(lst[72], z - 1, z + 1)),
                                SelectedIf(lst[72] == True), Function(Set_new_value, 72, If(lst[72], False, True)), Return("")], [SelectedIf(lst[72] or lst2[72]), Return("")])

        hotspot (584, 686, 105, 20) action If(z < 12 or lst[73], [SetVariable("z", If(lst[73], z - 1, z + 1)),
                                SelectedIf(lst[73] == True), Function(Set_new_value, 73, If(lst[73], False, True)), Return("")], [SelectedIf(lst[73] or lst2[73]), Return("")])

        hotspot (710, 686, 132, 26) action If(z < 12 or lst[74], [SetVariable("z", If(lst[74], z - 1, z + 1)),
                                SelectedIf(lst[74] == True), Function(Set_new_value, 74, If(lst[74], False, True)), Return("")], [SelectedIf(lst[74] or lst2[74]), Return("")])

        hotspot (855, 686, 167, 20) action If(z < 12 or lst[75], [SetVariable("z", If(lst[75], z - 1, z + 1)),
                                SelectedIf(lst[75] == True), Function(Set_new_value, 75, If(lst[75], False, True)), Return("")], [SelectedIf(lst[75] or lst2[75]), Return("")])

        hotspot (1038, 686, 33, 20) action If(z < 12 or lst[76], [SetVariable("z", If(lst[76], z - 1, z + 1)),
                                SelectedIf(lst[76] == True), Function(Set_new_value, 76, If(lst[76], False, True)), Return("")], [SelectedIf(lst[76] or lst2[76]), Return("")])

        hotspot (1085, 686, 205, 20) action If(z < 12 or lst[77], [SetVariable("z", If(lst[77], z - 1, z + 1)),
                                SelectedIf(lst[77] == True), Function(Set_new_value, 77, If(lst[77], False, True)), Return("")], [SelectedIf(lst[77] or lst2[77]), Return("")])

        hotspot (1302, 678, 158, 27) action If(z < 12 or lst[78], [SetVariable("z", If(lst[78], z - 1, z + 1)),
                                SelectedIf(lst[78] == True), Function(Set_new_value, 78, If(lst[78], False, True)), Return("")], [SelectedIf(lst[78] or lst2[78]), Return("")])

        hotspot (428, 726, 155, 26) action If(z < 12 or lst[79], [SetVariable("z", If(lst[79], z - 1, z + 1)),
                                SelectedIf(lst[79] == True), Function(Set_new_value, 79, If(lst[79], False, True)), Return("")], [SelectedIf(lst[79] or lst2[79]), Return("")])

        hotspot (430, 758, 255, 35) action If(z < 12 or lst[80], [SetVariable("z", If(lst[80], z - 1, z + 1)),
                                SelectedIf(lst[80] == True), Function(Set_new_value, 80, If(lst[80], False, True)), Return("")], [SelectedIf(lst[80] or lst2[80]), Return("")])

        hotspot (708, 758, 139, 34) action If(z < 12 or lst[81], [SetVariable("z", If(lst[81], z - 1, z + 1)), SensitiveIf(lst2[81] == False), SetVariable("right_choise", If(lst[81], right_choise - 1, right_choise + 1)),
                                SelectedIf(lst[81] or lst2[81]), Function(Set_new_value, 81, If(lst[81], False, True)), Return("T")], [SelectedIf(lst[81] or lst2[81]), Return("")])

        hotspot (868, 767, 195, 20) action If(z < 12 or lst[82], [SetVariable("z", If(lst[82], z - 1, z + 1)),
                                SelectedIf(lst[82] == True), Function(Set_new_value, 82, If(lst[82], False, True)), Return("")], [SelectedIf(lst[82] or lst2[82]), Return("")])

        hotspot (1086, 767, 204, 26) action If(z < 12 or lst[83], [SetVariable("z", If(lst[83], z - 1, z + 1)),
                                SelectedIf(lst[83] == True), Function(Set_new_value, 83, If(lst[83], False, True)), Return("")], [SelectedIf(lst[83] or lst2[83]), Return("")])

        hotspot (1309, 767, 85, 26) action If(z < 12 or lst[84], [SetVariable("z", If(lst[84], z - 1, z + 1)),
                                SelectedIf(lst[84] == True), Function(Set_new_value, 84, If(lst[84], False, True)), Return("")], [SelectedIf(lst[84] or lst2[84]), Return("")])

        hotspot (1405, 767, 85, 26) action If(z < 12 or lst[85], [SetVariable("z", If(lst[85], z - 1, z + 1)),
                                SelectedIf(lst[85] == True), Function(Set_new_value, 85, If(lst[85], False, True)), Return("")], [SelectedIf(lst[85] or lst2[85]), Return("")])

        hotspot (428, 807, 104, 20) action If(z < 12 or lst[86], [SetVariable("z", If(lst[86], z - 1, z + 1)), SensitiveIf(lst2[86] == False), SetVariable("right_choise", If(lst[86], right_choise - 1, right_choise + 1)),
                                SelectedIf(lst[86] or lst2[86]), Function(Set_new_value, 86, If(lst[86], False, True)), Return("T")], [SelectedIf(lst[86] or lst2[86]), Return("")])

        hotspot (542, 798, 270, 34) action If(z < 12 or lst[87], [SetVariable("z", If(lst[87], z - 1, z + 1)),
                                SelectedIf(lst[87] == True), Function(Set_new_value, 87, If(lst[87], False, True)), Return("")], [SelectedIf(lst[87] or lst2[87]), Return("")])

        hotspot (825, 807, 161, 20) action If(z < 12 or lst[88], [SetVariable("z", If(lst[88], z - 1, z + 1)),
                                SelectedIf(lst[88] == True), Function(Set_new_value, 88, If(lst[88], False, True)), Return("")], [SelectedIf(lst[88] or lst2[88]), Return("")])

        hotspot (996, 807, 88, 26) action If(z < 12 or lst[89], [SetVariable("z", If(lst[89], z - 1, z + 1)),
                                SelectedIf(lst[89] == True), Function(Set_new_value, 89, If(lst[89], False, True)), Return("")], [SelectedIf(lst[89] or lst2[89]), Return("")])

        hotspot (1098, 799, 111, 35) action If(z < 12 or lst[90], [SetVariable("z", If(lst[90], z - 1, z + 1)),
                                SelectedIf(lst[90] == True), Function(Set_new_value, 90, If(lst[90], False, True)), Return("")], [SelectedIf(lst[90] or lst2[90]), Return("")])

        hotspot (1221, 807, 98, 26) action If(z < 12 or lst[91], [SetVariable("z", If(lst[91], z - 1, z + 1)),
                                SelectedIf(lst[91] == True), Function(Set_new_value, 91, If(lst[91], False, True)), Return("")], [SelectedIf(lst[91] or lst2[91]), Return("")])

        hotspot (478, 847, 60, 20) action If(z < 12 or lst[92], [SetVariable("z", If(lst[92], z - 1, z + 1)),
                                SelectedIf(lst[92] == True), Function(Set_new_value, 92, If(lst[92], False, True)), Return("")], [SelectedIf(lst[92] or lst2[92]), Return("")])
                                
        hotspot (549, 847, 84, 20) action If(z < 12 or lst[93], [SetVariable("z", If(lst[93], z - 1, z + 1)),
                                SelectedIf(lst[93] == True), Function(Set_new_value, 93, If(lst[93], False, True)), Return("")], [SelectedIf(lst[93] or lst2[93]), Return("")])

        hotspot (645, 847, 178, 20) action If(z < 12 or lst[94], [SetVariable("z", If(lst[94], z - 1, z + 1)),
                                SelectedIf(lst[94] == True), Function(Set_new_value, 94, If(lst[94], False, True)), Return("")], [SelectedIf(lst[94] or lst2[94]), Return("")])

        hotspot (430, 880, 184, 33) action If(z < 12 or lst[95], [SetVariable("z", If(lst[95], z - 1, z + 1)),
                                SelectedIf(lst[95] == True), Function(Set_new_value, 95, If(lst[95], False, True)), Return("")], [SelectedIf(lst[95] or lst2[95]), Return("")])

        hotspot (624, 879, 201, 34) action If(z < 12 or lst[96], [SetVariable("z", If(lst[96], z - 1, z + 1)),
                                SelectedIf(lst[96] == True), Function(Set_new_value, 96, If(lst[96], False, True)), Return("")], [SelectedIf(lst[96] or lst2[96]), Return("")])

        hotspot (836, 887, 214, 26) action If(z < 12 or lst[97], [SetVariable("z", If(lst[97], z - 1, z + 1)),
                                SelectedIf(lst[97] == True), Function(Set_new_value, 97, If(lst[97], False, True)), Return("")], [SelectedIf(lst[97] or lst2[97]), Return("")])

        hotspot (1072, 878, 126, 28) action If(z < 12 or lst[98], [SetVariable("z", If(lst[98], z - 1, z + 1)),
                                SelectedIf(lst[98] == True), Function(Set_new_value, 98, If(lst[98], False, True)), Return("")], [SelectedIf(lst[98] or lst2[98]), Return("")])

        hotspot (1216, 878, 265, 34) action If(z < 12 or lst[99], [SetVariable("z", If(lst[99], z - 1, z + 1)), SensitiveIf(lst2[99] == False), SetVariable("right_choise", If(lst[99], right_choise - 1, right_choise + 1)),
                                SelectedIf(lst[99] or lst2[99]), Function(Set_new_value, 99, If(lst[99], False, True)), Return("T")], [SelectedIf(lst[99] or lst2[99]), Return("")])

        hotspot (430, 927, 201, 20) action If(z < 12 or lst[100], [SetVariable("z", If(lst[100], z - 1, z + 1)),
                                SelectedIf(lst[100] == True), Function(Set_new_value, 100, If(lst[100], False, True)), Return("")], [SelectedIf(lst[100] or lst2[100]), Return("")])

        hotspot (643, 927, 73, 20) action If(z < 12 or lst[101], [SetVariable("z", If(lst[101], z - 1, z + 1)),
                                SelectedIf(lst[101] == True), Function(Set_new_value, 101, If(lst[101], False, True)), Return("")], [SelectedIf(lst[101] or lst2[101]), Return("")])
                                
        hotspot (729, 927, 396, 20) action If(z < 12 or lst[102], [SetVariable("z", If(lst[102], z - 1, z + 1)),
                                SelectedIf(lst[102] == True), Function(Set_new_value, 102, If(lst[102], False, True)), Return("")], [SelectedIf(lst[102] or lst2[102]), Return("")])

        hotspot (1136, 927, 92, 26) action If(z < 12 or lst[103], [SetVariable("z", If(lst[103], z - 1, z + 1)),
                                SelectedIf(lst[103] == True), Function(Set_new_value, 103, If(lst[103], False, True)), Return("")], [SelectedIf(lst[103] or lst2[103]), Return("")])
                                
        hotspot (1238, 927, 149, 26) action If(z < 12 or lst[104], [SetVariable("z", If(lst[104], z - 1, z + 1)), SensitiveIf(lst2[104] == False), SetVariable("right_choise", If(lst[104], right_choise - 1, right_choise + 1)),
                                SelectedIf(lst[104] or lst2[104]), Function(Set_new_value, 104, If(lst[104], False, True)), Return("T")], [SelectedIf(lst[104] or lst2[104]), Return("")])

        hotspot (430, 967, 165, 26) action If(z < 12 or lst[105], [SetVariable("z", If(lst[105], z - 1, z + 1)),
                                SelectedIf(lst[105] == True), Function(Set_new_value, 105, If(lst[105], False, True)), Return("")], [SelectedIf(lst[105] or lst2[105]), Return("")])

        hotspot (605, 967, 82, 20) action If(z < 12 or lst[106], [SetVariable("z", If(lst[106], z - 1, z + 1)),
                                SelectedIf(lst[106] == True), Function(Set_new_value, 106, If(lst[106], False, True)), Return("")], [SelectedIf(lst[106] or lst2[106]), Return("")])

        hotspot (699, 967, 205, 20) action If(z < 12 or lst[107], [SetVariable("z", If(lst[107], z - 1, z + 1)),
                                SelectedIf(lst[107] == True), Function(Set_new_value, 107, If(lst[107], False, True)), Return("")], [SelectedIf(lst[107] or lst2[107]), Return("")])

        hotspot (1606, 947, 277, 84) action[SensitiveIf(z >= 12 and game_over == False), Function(text_array_change, True), SetVariable("popitki", popitki + 1), 
        SetVariable("z", right_choise), Return("proverka")]

        hotspot (1839, 18, 47, 52) action[SensitiveIf(game_over), Return("exit")]


screen copyright_law(): # мини-игра Авторское право
    if copyright_progress == 1:
        add "images/copyright/computer_bg.jpg"
    else:
        add "images/copyright/computer_bg2.jpg"
    
    imagebutton:
        if copyright_progress == 1:
            xpos 1329
            ypos 859
        else:
            xpos 1332
            ypos 859

        idle ("images/copyright/buttons/check_btn_idle.png")
        hover ("images/copyright/buttons/check_btn_hover.png") 

        action [SensitiveIf(answer_full[1] and answer_full[2] and answer_full[3]), Return ("next_level")]

    imagebutton:
        if copyright_progress == 1:
            xpos 432
            ypos 80
        else:
            xpos 435
            ypos 80

        idle ("images/copyright/buttons/help_btn_idle.png")
        hover ("images/copyright/buttons/help_btn_hover.png")

        action [Return ("open_help")]
    
    draggroup:

        drag:
            drag_name "answer1"
            child "images/copyright/drop_place.png"
            draggable False
            if answer_full[1]:
                droppable False
            else:
                droppable True
            if copyright_progress == 1:
                xpos 69 ypos 518
            else:
                xpos 71 ypos 518

        drag:
            drag_name "answer2"
            child "images/copyright/drop_place.png"
            if answer_full[2]:
                droppable False
            else:
                droppable True
            droppable True
            if copyright_progress == 1:
                xpos 691 ypos 518
            else:
                xpos 694 ypos 518

        drag:
            drag_name "answer3"
            child "images/copyright/drop_place.png"
            if answer_full[3]:
                droppable False
            else:
                droppable True
            droppable True
            if copyright_progress == 1:
                xpos 1314 ypos 518
            else:
                xpos 1316 ypos 519

        drag:
            drag_name "CC_BY(1)"
            if copyright_progress == 1:
                child "images/copyright/level1/CC_BY.png"
            else:
                child "images/copyright/level2/CC_BY-NC.png"
            if text_position[1][0] != 0:
                xpos text_position[1][0] ypos text_position[1][1]
            else:
                xpos default_position[1] ypos 700
            draggable True 
            droppable False
            dragged answer_dragged
        
        drag:
            drag_name "CC_BY-SA(2)"
            if copyright_progress == 1:
                child "images/copyright/level1/CC_BY-SA.png"
            else:
                child "images/copyright/level2/CC_0.png"
            if text_position[2][0] != 0:
                xpos text_position[2][0] ypos text_position[2][1]
            else:
                xpos default_position[2] ypos 700
            draggable True
            droppable False
            dragged answer_dragged

        drag:
            drag_name "CC_BY-ND(3)"
            if copyright_progress == 1:
                child "images/copyright/level1/CC_BY-ND.png"
            else:
                child "images/copyright/level2/CC_BY-NC-ND.png"
            if text_position[3][0] != 0:
                xpos text_position[3][0] ypos text_position[3][1]
            else:
                xpos default_position[3] ypos 700
            draggable True
            droppable False
            dragged answer_dragged

screen copyright_help_page():
    add "images/copyright/help_bg.jpg"
    imagebutton:
        xpos 0
        ypos 80

        idle ("images/copyright/buttons/return_btn_idle.png")
        hover ("images/copyright/buttons/return_btn_hover.png")

        action[Return ("return_to_game")]

screen copyright_final():
    
    imagemap:
        ground "images/copyright/answers2.png"
        hover "images/copyright/answers2.png" #добавить выделение крестика

        hotspot(1825, 0, 80, 80) clicked Return("exit")
        
        add "images/copyright/arrow_45.png" at arrow_move_45(0.93, 0.1)



############ 5ая игра ################

init python:

    # основной экран гардероба
    def wardrobe_screen_f(_name, _scope, _debug):
        
        ui.add("images/wardrobe/wardrobe_bg.jpg", ypos = -1)
        draggroup = DragGroup()

        # отображение манекена
        model_drag = Drag(d="images/wardrobe/model.jpg", drag_name = "model", draggable = False, droppable = True, xpos = 313, ypos = 180)
        draggroup.add(model_drag)
        ui.add(model_drag, id = "model")

        # отображение нижней части одежды (выбрано / не выбрано)
        for a in range(1, 6):
            if bottom_ready[a] == True:
                drag = Drag(d=f"images/wardrobe/female/ready/bottom{a}_ready.png", drag_name = f"2bottom{a}", draggable = False, droppable = False, xpos = bottom_position_f[a][0], ypos = bottom_position_f[a][1])
            else:
                drag = Drag(d=f"images/wardrobe/female/bottom{a}_idle.png", drag_name = f"2bottom{a}", draggable = True, droppable = False, xpos = bottom_position_f[a][0], ypos = bottom_position_f[a][1], dragged = garment_dragged_f)
            draggroup.add(drag)
            ui.add(drag, id = f"bottom{a}")
        
        # отображение верхней части одежды (выбрано / не выбрано)
        for a in range(1, 7):
            if top_ready[a] == True:
                drag = Drag(d=f"images/wardrobe/female/ready/top{a}_ready.png", drag_name = f"1top{a}", draggable = False, droppable = False, xpos = top_position_f[a][0], ypos = top_position_f[a][1])
            else:
                drag = Drag(d=f"images/wardrobe/female/top{a}_idle.png", drag_name = f"1top{a}", draggable = True, droppable = False, xpos = top_position_f[a][0], ypos = top_position_f[a][1], dragged = garment_dragged_f)
            draggroup.add(drag)
            ui.add(drag, id = f"top{a}")

        # отображение обуви (выбрано / не выбрано)
        for a in range(1, 5):
            if boots_ready[a] == True:
                drag = Drag(d=f"images/wardrobe/female/ready/boots{a}_ready.png", drag_name = f"3boots{a}", draggable = False, droppable = False, xpos = boots_position_f[a][0], ypos = boots_position_f[a][1])
            else:
                drag = Drag(d=f"images/wardrobe/female/boots{a}_idle.png", drag_name = f"3boots{a}", draggable = True, droppable = False, xpos = boots_position_f[a][0], ypos = boots_position_f[a][1], dragged = garment_dragged_f)
            draggroup.add(drag)
            ui.add(drag, id = f"boots{a}")  
        
        ui.add(draggroup, id="wardrobe_draggroup")

    # определение экрана
    renpy.define_screen("WardrobeScreenF", wardrobe_screen_f)

    # поведение одежды при перетаскивании
    def garment_dragged_f(drags, drop):
        char_garment = [char for char in drags[0].drag_name]
        num2 = int(char_garment[len(char_garment)-1])
        num1 = int(char_garment[0])

        # если отпустили в случайном месте, возвращение обратно 
        if not drop:
            if num1 == 1:
                drags[0].snap(main_top_position_f[num2][0], main_top_position_f[num2][1], 0.5) 
            elif num1 == 2:
                drags[0].snap(main_bottom_position_f[num2][0], main_bottom_position_f[num2][1], 0.5)
            elif num1 == 3:
                drags[0].snap(main_boots_position_f[num2][0], main_boots_position_f[num2][1], 0.5)

        # поднимаем объекты к пользователю в нужном порядке
        for a in range(1, 7):
            renpy.get_widget("WardrobeScreenF", f"top{a}").top()
        for a in range(1, 6):
            renpy.get_widget("WardrobeScreenF", f"bottom{a}").top()            

        if drop:
            return drags[0].drag_name

        return

    #очистка текущего положения ранее выбранных предметов одежды (предыдущий объект возвращается в шкаф)
    def clear_garments(num):
            if num == 1:
                for a in range(7):
                    top_position_f[a][0] = main_top_position_f[a][0]
                    top_position_f[a][1] = main_top_position_f[a][1]
                    top_ready[a] = False
            elif num == 2:
                for a in range(6):
                    bottom_position_f[a][0] = main_bottom_position_f[a][0]
                    bottom_position_f[a][1] = main_bottom_position_f[a][1]
                    bottom_ready[a] = False
            elif num == 3:
                for a in range(5):
                    boots_position_f[a][0] = main_boots_position_f[a][0]
                    boots_position_f[a][1] = main_boots_position_f[a][1]
                    boots_ready[a] = False
            else: #специальная очистка для платья
                top_position_f[2][0] = main_top_position_f[2][0]
                top_position_f[2][1] = main_top_position_f[2][1]
                top_ready[2] = False
            return

    # обновление изображения текущей сцены
    def update_garment_image(num1, num2):
        if num1 == 1: #верх
            if num2 == 2:
                for a in range(1, 6): #специально для платья
                    if bottom_ready[a]:
                        hide_name = f"bottom{a}f"
                        renpy.hide(hide_name)

            for a in range(1, 7): #убираем отображение предыдущей одежды на манекене
                if(top_ready[a] and a != num2):
                    hide_name = f"top{a}f"
                    renpy.hide(hide_name)
            str_name = f"top{num2}f"
            garmentTransform = Transform(xpos = model_top_position_f[num2][0], ypos = model_top_position_f[num2][1])

        elif num1 == 2: #низ
            for a in range(1, 6): #убираем отображение предыдущей одежды на манекене
                if(bottom_ready[a] and a != num2):
                    hide_name = f"bottom{a}f"
                    renpy.hide(hide_name)
            if top_ready[2]:
                renpy.hide("top2f")
            str_name = f"bottom{num2}f"
            garmentTransform = Transform(xpos = model_bottom_position_f[num2][0], ypos = model_bottom_position_f[num2][1])

        else: #обувь
            for a in range(1, 5): #убираем отображение предыдущей обуви у манекена
                if(boots_ready[a] and a != num2):
                    hide_name = f"boots{a}f"
                    renpy.hide(hide_name)
            str_name = f"boots{num2}f"
            garmentTransform = Transform(xpos = model_boots_position_f[num2][0], ypos = model_boots_position_f[num2][1])
        
        # отображаем выбранный объект в нужном месте
        renpy.hide(str_name)
        renpy.show(str_name, at_list = [garmentTransform])

        # при наложении одежды верхнюю часть переносим выше
        if num1 == 2 and top_ready[3]:
                garmentTransform = Transform(xpos = model_top_position_f[3][0], ypos = model_top_position_f[3][1])
                renpy.hide(f"top3f")
                renpy.show(f"top3f", at_list = [garmentTransform])
        return

    
######### Мини-игра Гардероб М #########

    def wardrobe_screen_m(_name, _scope, _debug):
        
        ui.add("images/wardrobe/wardrobe_bg.jpg", ypos = -1)
        draggroup = DragGroup()
        
        # отображение манекена
        model_drag = Drag(d="images/wardrobe/model.jpg", drag_name = "model", draggable = False, droppable = True, xpos = 313, ypos = 180)
        draggroup.add(model_drag)
        ui.add(model_drag, id = "model")

        # отображение нижней части одежды (выбрано / не выбрано)
        for a in range(1, 5):
            if bottom_ready[a] == True:
                drag = Drag(d=f"images/wardrobe/male/ready/bottom{a}_ready.png", drag_name = f"2bottom{a}", draggable = False, droppable = False, xpos = bottom_position_m[a][0], ypos = bottom_position_m[a][1])
            else:
                drag = Drag(d=f"images/wardrobe/male/bottom{a}_idle.png", drag_name = f"2bottom{a}", draggable = True, droppable = False, xpos = bottom_position_m[a][0], ypos = bottom_position_m[a][1], dragged = garment_dragged_m)
            draggroup.add(drag)
            ui.add(drag, id = f"bottom{a}")
        
        # отображение верхней части одежды (выбрано / не выбрано)
        for a in range(1, 6):
            if top_ready[a] == True:
                drag = Drag(d=f"images/wardrobe/male/ready/top{a}_ready.png", drag_name = f"1top{a}", draggable = False, droppable = False, xpos = top_position_m[a][0], ypos = top_position_m[a][1])
            else:
                drag = Drag(d=f"images/wardrobe/male/top{a}_idle.png", drag_name = f"1top{a}", draggable = True, droppable = False, xpos = top_position_m[a][0], ypos = top_position_m[a][1], dragged = garment_dragged_m)
            draggroup.add(drag)
            ui.add(drag, id = f"top{a}")

        # отображение обуви (выбрано / не выбрано)
        for a in range(1, 5):
            if boots_ready[a] == True:
                drag = Drag(d=f"images/wardrobe/male/ready/boots{a}_ready.png", drag_name = f"3boots{a}", draggable = False, droppable = False, xpos = boots_position_m[a][0], ypos = boots_position_m[a][1])
            else:
                drag = Drag(d=f"images/wardrobe/male/boots{a}_idle.png", drag_name = f"3boots{a}", draggable = True, droppable = False, xpos = boots_position_m[a][0], ypos = boots_position_m[a][1], dragged = garment_dragged_m)
            draggroup.add(drag)
            ui.add(drag, id = f"boots{a}")  
        
        ui.add(draggroup, id="wardrobe_draggroup")

    # определение экрана
    renpy.define_screen("WardrobeScreenM", wardrobe_screen_m)

    # поведение одежды при перетаскивании
    def garment_dragged_m(drags, drop):
        char_garment = [char for char in drags[0].drag_name]
        num2 = int(char_garment[len(char_garment)-1])
        num1 = int(char_garment[0])

        # если отпустили в случайном месте, возвращение обратно 
        if not drop:
            if num1 == 1:
                drags[0].snap(main_top_position_m[num2][0], main_top_position_m[num2][1], 0.5) 
            elif num1 == 2:
                drags[0].snap(main_bottom_position_m[num2][0], main_bottom_position_m[num2][1], 0.5)
            elif num1 == 3:
                drags[0].snap(main_boots_position_m[num2][0], main_boots_position_m[num2][1], 0.5)
        
        # поднимаем объекты к пользователю в нужном порядке
        for a in range(1, 5):
            renpy.get_widget("WardrobeScreenM", f"bottom{a}").top()
        for a in range(1, 6):
            renpy.get_widget("WardrobeScreenM", f"top{a}").top()        

        if drop:
            return drags[0].drag_name
        
        return

    #очистка текущего положения ранее выбранных предметов одежды (предыдущий объект возвращается в шкаф)
    def clear_garments_m(num):
        if num == 1:
            for a in range(6):
                top_position_m[a][0] = main_top_position_m[a][0]
                top_position_m[a][1] = main_top_position_m[a][1]
                top_ready[a] = False
        elif num == 2:
            for a in range(4): #Добавить недостающий объект
                bottom_position_m[a][0] = main_bottom_position_m[a][0]
                bottom_position_m[a][1] = main_bottom_position_m[a][1]
                bottom_ready[a] = False
        elif num == 3:
            for a in range(5):
                boots_position_m[a][0] = main_boots_position_m[a][0]
                boots_position_m[a][1] = main_boots_position_m[a][1]
                boots_ready[a] = False
        return

    # обновление изображения текущей сцены
    def update_garment_image_m(num1, num2):
        if num1 == 1: #верх
            for a in range(1, 6): #убираем отображение предыдущей одежды на манекене
                if(top_ready[a] and a != num2):
                    hide_name = f"top{a}m"
                    renpy.hide(hide_name)
            str_name = f"top{num2}m"
            garmentTransform = Transform(xpos = model_top_position_m[num2][0], ypos = model_top_position_m[num2][1])

        elif num1 == 2: #низ
            for a in range(1, 5): #убираем отображение предыдущей одежды на манекене
                if(bottom_ready[a] and a != num2):
                    hide_name = f"bottom{a}m"
                    renpy.hide(hide_name)
            str_name = f"bottom{num2}m"
            garmentTransform = Transform(xpos = model_bottom_position_m[num2][0], ypos = model_bottom_position_m[num2][1])

        else: #обувь
            for a in range(1, 5): #убираем отображение предыдущей обуви у манекена
                if(boots_ready[a] and a != num2):
                    hide_name = f"boots{a}m"
                    renpy.hide(hide_name)
            str_name = f"boots{num2}m"
            garmentTransform = Transform(xpos = model_boots_position_m[num2][0], ypos = model_boots_position_m[num2][1])

        # отображаем выбранный объект в нужном месте
        renpy.hide(str_name)
        renpy.show(str_name, at_list = [garmentTransform])
        
        # при наложении одежды верхнюю часть переносим выше
        if num1 == 2:
            for a in range(1, 6):
                if top_ready[a]:
                    garmentTransform = Transform(xpos = model_top_position_m[a][0], ypos = model_top_position_m[a][1])
                    renpy.hide(f"top{a}m")
                    renpy.show(f"top{a}m", at_list = [garmentTransform])
        return


######### Мини-игра Зеркало Ж #########

    # основной экран зеркала
    def mirror_screen_f(_name, _scope, _debug):

        ui.add("images/mirror/female/mirror_bg.jpg", ypos = -1)
        draggroup = DragGroup()

        # отображение персонажа в зависимости от выбранной прически
        if haircut_ready[3]:
            character_drag = Drag(d="images/mirror/female/haircut/haircut3_ready.png", drag_name = "character_drag", draggable = False, droppable = True, xpos = 750, ypos = 221)
        elif haircut_ready[4]:
            character_drag = Drag(d="images/mirror/female/haircut/haircut4_ready.png", drag_name = "character_drag", draggable = False, droppable = True, xpos = 750, ypos = 221)
        else:
            character_drag = Drag(d="images/mirror/female/character_bg.png", drag_name = "character_drag", draggable = False, droppable = True, xpos = 750, ypos = 221)
        draggroup.add(character_drag)
        ui.add(character_drag, id = "character_drag")

        # отображение не выбранных причесок
        for a in range(1, 5):
            if not haircut_ready[a]:
                drag = Drag(d=f"images/mirror/female/haircut/haircut{a}.png", drag_name = f"haircut{a}", draggable = True, droppable = False, xpos = main_haircut_position_f[a][0], ypos = main_haircut_position_f[a][1], dragged = haircut_dragged_f)
                draggroup.add(drag)
                ui.add(drag, id = f"haircut{a}")

        # отображение украшений и косметики
        for a in range(1, 8):
            if add_ready[a]:
                drag = Drag(d=f"images/mirror/female/add/add{a}_ready.png", drag_name = f"add{a}", draggable = False, droppable = False, xpos = add_model_position_f[a][0], ypos = add_model_position_f[a][1])
                if a > 4: #дополнительные объекты для отображения использованной и неактивной косметики
                    drag2 = Drag(d=f"images/mirror/female/add/add{a}.png", drag_name = f"add{a}_inactive", draggable = False, droppable = False, xpos = main_add_position_f[a][0], ypos = main_add_position_f[a][1])
                    draggroup.add(drag2)
                    ui.add(drag2, id = f"add{a}_inactive")
            else:
                drag = Drag(d=f"images/mirror/female/add/add{a}.png", drag_name = f"add{a}", draggable = True, droppable = False, xpos = main_add_position_f[a][0], ypos = main_add_position_f[a][1], dragged = add_dragged_f)
            draggroup.add(drag)
            ui.add(drag, id = f"add{a}")
        
        ui.add(draggroup, id = "mirror_draggroup")

    renpy.define_screen("MirrorScreenF", mirror_screen_f)

    # поведение причесок при перетаскивании
    def haircut_dragged_f(drags, drop):
        char_haircut = [char for char in drags[0].drag_name]
        num = int(char_haircut[7])

        if not drop:
            drags[0].snap(main_haircut_position_f[num][0], main_haircut_position_f[num][1], 0.5)
        
        if drop:
            return drags[0].drag_name
        
        return

    # поведение украшений и косметики при перетаскивании
    def add_dragged_f(drags, drop):
        char_add = [char for char in drags[0].drag_name]
        num = int(char_add[3])

        if not drop:
            drags[0].snap(main_add_position_f[num][0], main_add_position_f[num][1], 0.5)

        if drop:
            return drags[0].drag_name

        return

    # обновление изображения текущей сцены
    def update_mirror_image_f(num1, num2):
        if num1 == 1: #haircut
            if haircut_ready[num2]:
                renpy.hide(f"haircut{num2}f") 
        if num1 == 2: #add
            renpy.hide(f"add{num2}f")
            addTransform = Transform(xpos = add_model_position_f[num2][0], ypos = add_model_position_f[num2][1])
            renpy.show(f"add{num2}f", at_list = [addTransform])


######### Мини-игра Зеркало М #########

    # основной экран зеркала
    def mirror_screen_m(_name, _scope, _debug):

        ui.add("images/mirror/male/mirror_bg.jpg", ypos = -1)
        draggroup = DragGroup()

        # отображение персонажа в зависимости от выбранной прически
        if haircut_ready[1]:
            character_drag = Drag(d="images/mirror/male/haircut/haircut1_ready.png", drag_name = "character_drag", draggable = False, droppable = True, xpos = 725, ypos = 185)
        elif haircut_ready[3]:
            character_drag = Drag(d="images/mirror/male/haircut/haircut3_ready.png", drag_name = "character_drag", draggable = False, droppable = True, xpos = 725, ypos = 185)
        else:
            character_drag = Drag(d="images/mirror/male/character_bg.png", drag_name = "character_drag", draggable = False, droppable = True, xpos = 725, ypos = 185)
        draggroup.add(character_drag)
        ui.add(character_drag, id = "character_drag")

        # отображение не выбранных причесок
        for a in range(1, 5):
            if not haircut_ready[a]:
                drag = Drag(d=f"images/mirror/male/haircut/haircut{a}.png", drag_name = f"haircut{a}", draggable = True, droppable = False, xpos = main_haircut_position_m[a][0], ypos = main_haircut_position_m[a][1], dragged = haircut_dragged_m)
                draggroup.add(drag)
                ui.add(drag, id = f"haircut{a}")

        # отображение украшений и косметики
        for a in range(1, 9):
            if add_ready[a]:
                if a != 4: #часы под номером 4 не видны в зеркале
                    drag = Drag(d=f"images/mirror/male/add/add{a}_ready.png", drag_name = f"add{a}", draggable = False, droppable = False, xpos = add_model_position_m[a][0], ypos = add_model_position_m[a][1])
                if a == 8: #дополнительный объект для отображения использованной и неактивной туши
                        drag2 = Drag(d=f"images/mirror/male/add/add8.png", drag_name = f"add8_inactive", draggable = False, droppable = False, xpos = main_add_position_m[a][0], ypos = main_add_position_m[a][1])
                        draggroup.add(drag2)
                        ui.add(drag2, id = f"add8_inactive")
            else:
                drag = Drag(d=f"images/mirror/male/add/add{a}.png", drag_name = f"add{a}", draggable = True, droppable = False, xpos = main_add_position_m[a][0], ypos = main_add_position_m[a][1], dragged = add_dragged_m)
            draggroup.add(drag)
            ui.add(drag, id = f"add{a}")
        
        ui.add(draggroup, id = "mirror_draggroup")

    renpy.define_screen("MirrorScreenM", mirror_screen_m)

    # поведение причесок при перетаскивании
    def haircut_dragged_m(drags, drop):
        char_haircut = [char for char in drags[0].drag_name]
        num = int(char_haircut[7])

        if not drop:
            drags[0].snap(main_haircut_position_m[num][0], main_haircut_position_m[num][1], 0.5)
        
        if drop:
            return drags[0].drag_name
        
        return

    # поведение украшений и косметики при перетаскивании
    def add_dragged_m(drags, drop):
        char_add = [char for char in drags[0].drag_name]
        num = int(char_add[3])

        if not drop:
            drags[0].snap(main_add_position_m[num][0], main_add_position_m[num][1], 0.5)

        if drop:
            return drags[0].drag_name

        return

    # обновление изображения текущей сцены
    def update_mirror_image_m(num1, num2):
        if num1 == 1: #haircut
            if haircut_ready[num2]:
                renpy.hide(f"haircut{num2}m") 
        if num1 == 2: #add
            renpy.hide(f"add{num2}m")
            addTransform = Transform(xpos = add_model_position_m[num2][0], ypos = add_model_position_m[num2][1])
            renpy.show(f"add{num2}m", at_list = [addTransform])

screen final_finalov():
    
    imagebutton:   
        xpos 0.4
        ypos 0.8
        idle ("images/final/btn_ser_idle.png")
        hover ("images/final/btn_ser_hover.png")
        action [Return("Sertifikat")]

screen final2():
    imagebutton:   
        xpos 0.4
        ypos 0.8
        idle ("images/final/btn_finish_idle.png")
        hover ("images/final/btn_finish_hover.png")
        action [Return("")]
    imagebutton:
        xpos 0.75
        ypos 0
        idle ("images/final/btn_ser_idle.png")
        hover ("images/final/btn_ser_hover.png")
        action [Return("Sertifikat")]