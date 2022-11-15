screen input_name: # Ввод имени игрока
    add "images/input/input_name_bg.jpg"

    input default "":
        xpos 950
        ypos 490
        pixel_width 470

        xysize (473, 45)

screen input_sex_and_pet: # Ввод пола и питомца
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

screen input_name_of_pet: # Ввод имени питомца
    add "images/input/input_name_of_pet.png" xalign 0.5 yalign 0.5

    input default "":
        xpos 950
        ypos 540
        pixel_width 470

        xysize (473, 45)


screen room: # Комната автора

    imagemap:
        if flag_room_broken: # флаг, возникающий в мини-игре дальше в сюжете
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
            hotspot (1152, 172, 485, 759) clicked NullAction() # Шкаф
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

screen computer: # Компьютер

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
        imagebutton:
            xpos 25
            ypos 25

            idle ("images/desktop/mail_icon.png")
            hover ("images/desktop/mail_icon_hover.png")

            action [
            ToggleVariable("show_mail_area", True, False),
            SetVariable("user_have_new_message", False),
            SetVariable("show_todo_area", False)
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
        add "images/desktop/todo_area.png" xpos 380 ypos 50

        text "Список задач:" style "title_of_todo_text" xpos  450 ypos 120

        hbox:
            vbox:
                xpos 500 ypos 250
                spacing 50

                button style "tasks_todo_bar_button":
                    maximum (500, 75)
                    minimum (500, 75)

                    text "План видео" at center

                    action [SensitiveIf(not todo_one_colmpleted), Return("1")] # если не завершена эта часть игры, то кнопка активна

                button style "tasks_todo_bar_button":
                    maximum (500, 75)
                    minimum (500, 75)

                    text "Тексты к видео" at center

                    action [SensitiveIf(not todo_two_colmpleted), Return("2")] # /\

                button style "tasks_todo_bar_button":
                    maximum (500, 75)
                    minimum (500, 75)

                    text "Правовая чистота" at center

                    action [SensitiveIf(not todo_three_colmpleted), Return("3")] # /\

            vbox:
                xpos 750 ypos 250
                spacing 50

                button style "tasks_todo_bar_button":
                    maximum (500, 75)
                    minimum (500, 75)

                    text "Монтажные презентации" at center

                    action [SensitiveIf(not todo_four_colmpleted), Return("4")] # /\

                button style "tasks_todo_bar_button":
                    maximum (500, 75)
                    minimum (500, 75)

                    text "Внешний образ" at center

                    action [SensitiveIf(not todo_five_colmpleted), Return("5")] # /\

                button style "tasks_todo_bar_button":
                    maximum (500, 75)
                    minimum (500, 75)

                    text "Съёмки" at center

                    action [SensitiveIf(not todo_six_colmpleted), Return("6")] # /\

        showif todo_one_colmpleted: # завершенные части закрываются крестиком
            add "images/desktop/crest.png" xpos 475 ypos 225
        showif todo_two_colmpleted:
            add "images/desktop/crest.png" xpos 475 ypos 350
        showif todo_three_colmpleted:
            add "images/desktop/crest.png" xpos 475 ypos 475
        showif todo_four_colmpleted:
            add "images/desktop/crest.png" xpos 1225 ypos 225
        showif todo_five_colmpleted:
            add "images/desktop/crest.png" xpos 1225 ypos 350
        showif todo_six_colmpleted:
            add "images/desktop/crest.png" xpos 1225 ypos 475

    showif arrow_at_message_icon: # стрелки-указатели в первый раз открытия компьютера 
        add "images/arrows/arrow_left.png" at arrow_move(0.15, 0.08)

    showif arrow_at_todo_icon:
        add "images/arrows/arrow_left.png" at arrow_move(0.15, 0.3)


screen department_door: # Дверь перед кафедрой
    imagemap:
        ground "images/department/department_door.jpg"
        hover "images/department/department_door_hover.jpg"

        hotspot (681, 77, 559, 854) action[
        SetVariable("amount_of_clicks", amount_of_clicks+1),
        If(amount_of_clicks >= 2, true=Return("go"))
        ]
        # скрин перебрасывает человека дальше в сюжете если нажать на экран 3 раза - счётчик

screen department: # Кафедра
    imagemap:
        ground "images/department/department.jpg"
        hover "images/department/department_hover.jpg"

        hotspot (15, 94, 242, 908) clicked Return("exit") # дверь
        if flag_department_blackboard_opened:
            hotspot (917, 277, 652, 363) clicked NullAction() # Доска


screen nots: # НОЦ
    imagemap:
        ground "images/nots/nots.jpg"
        hover "images/nots/nots_hover.jpg"

        hotspot (10, 113, 256, 967) clicked Return("exit") # Дверь
        if flag_nots_window_opened:
            hotspot (1675, 53, 245, 735) clicked NullAction() # Окно

screen album: # Мини-игра на подбор фотографии в альбоме

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
         selected_idle
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

      action [Return("correct")]

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

      action [SetVariable("album_photos_selected_3", True), Return("uncorrect_3")]
      sensitive not album_photos_selected_3

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

      action [SetVariable("album_photos_selected_4", True), Return("uncorrect_4")]
      sensitive not album_photos_selected_4

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

      action [SetVariable("album_photos_selected_5", True), Return("uncorrect_5")]
      sensitive not album_photos_selected_5


screen making_program_mini_game: # Мини-игра на составление программы

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
screen find_all_documents:
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
