init:
######### Сведения об игроке #########
    default name = ""
    default sex = "male"
    default pet = "dog"
    default pet_name = ""


######### имя навигатора #########

    default navigator_name = "Навигатор"

######### Внутреигровые настройки #########
    default preferences.text_cps = 32 # скорость воспроизведения текста по умолчанию
    define gui.text_color = "#000000"
    define gui.dialogue_width = 875
    define gui.name_xpos = 675
    define gui.name_ypos = 52
    define gui.dialogue_xpos = 675
    define gui.dialogue_ypos = 119

    define LongFade = Fade(1.0, 1.0, 1.0)

    define config.hard_rollback_limit = 0 # запрет действия "назад"

######### Элементы комнаты #########
    default flag_room_door_opened = True
    default flag_room_album_opened = False
    default flag_room_computer_opened = True
    default flag_room_pet_opened = False
    default flag_room_cupboard_opened = False

    default flag_room_broken = False

    default arrow_at_computer = False
    default arrow_at_door_at_home = False
    default arrow_at_pet = False
    default arrow_at_album = False
    default arrow_at_message_icon = False
    default arrow_at_todo_icon = False
    default arrow_at_cupboard = False
    default arrow_at_close_computer = False
    default arrow_at_door_in_department = False
    default arrow_at_door_in_nots = False

######### Элементы НОЦ #########
    default flag_nots_window_opened = False

######### Элементы кафедры #########
    default flag_department_blackboard_opened = False

######### Элементы компьютера #########
    default show_mail_area = False
    default user_have_new_message = False
    default user_need_to_read_mail = False
    default current_message = ("", "")
    default show_todo_icon = False
    default show_todo_area = False

######### Элементы компьютера #########
    default correct_created_program = False
    default arrow_at_close = True

    default first_todo_hovered = False

######### Вспомогательные переменные для мини-игр #########
    default amount_of_clicks = 0
    default amount_of_presentations = 0
    

    python:
        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]
                self.dist = dist
                self.child = child

            def __call__(self, t, sizes):
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                            time,
                            child,
                            add_sizes=True,
                            **properties)

        Shake = renpy.curry(_Shake)

######### Проверка корректности ввода поля "имя" #########

    python:
        def check_name(text):
            if len(text) == 0:
                return "emptyemptyemptyemptye"
            elif len(text) > 20:
                return "largelargelargelargel"
            else:
                out = " ".join(text.split())

                if len(out) == 0:
                    return "spacesspacesspacesspa"
                else:
                    return out.title()

######### Элементы альбома #########
    image album_bg = "images/album_photos/album.jpg"
    
    default album_photos_selected_1 = False
    default album_photos_selected_2 = False
    default album_photos_selected_3 = False
    default album_photos_selected_4 = False
    default album_photos_selected_5 = False
    default album_photos_selected_6 = False

    ## для мужика ##

    image default_photo1F = "images/album_photos/normal/female_5.jpg"
    image wb_photo1F = "images/album_photos/wb/female_5.jpg"

    image default_photo2F = "images/album_photos/normal/female_4.jpg"
    image wb_photo2F = "images/album_photos/wb/female_4.jpg"

    image default_photo3F = "images/album_photos/normal/female_3.jpg"
    image wb_photo3F = "images/album_photos/wb/female_3.jpg"

    image default_photo4F = "images/album_photos/normal/female_1.jpg"
    image wb_photo4F = "images/album_photos/wb/female_1.jpg"

    image default_photo5F = "images/album_photos/normal/female_2.jpg"
    image wb_photo5F = "images/album_photos/wb/female_2.jpg"

    image default_photo6F = "images/album_photos/normal/female_6.jpg"
    image wb_photo6F = "images/album_photos/wb/female_6.jpg"
    

    ## для девушки ##
    image default_photo1M = "images/album_photos/normal/male_5.jpg"
    image wb_photo1M = "images/album_photos/wb/male_5.jpg"

    image default_photo2M = "images/album_photos/normal/male_4.jpg"
    image wb_photo2M = "images/album_photos/wb/male_4.jpg"

    image default_photo3M = "images/album_photos/normal/male_3.jpg"
    image wb_photo3M = "images/album_photos/wb/male_3.jpg"

    image default_photo4M = "images/album_photos/normal/male_1.jpg"
    image wb_photo4M = "images/album_photos/wb/male_1.jpg"

    image default_photo5M = "images/album_photos/normal/male_2.jpg"
    image wb_photo5M = "images/album_photos/wb/male_2.jpg"

    image default_photo6M = "images/album_photos/normal/male_6.jpg"
    image wb_photo6M = "images/album_photos/wb/male_6.jpg"
    

######### Переменные для составления программы МОК #########

    default show_file_to_make_programm = False

    default making_program_show_one = False
    default making_program_show_two = False
    default making_program_show_three = False
    default making_program_show_four = False
    default making_program_show_five = False
    default making_program_show_six = False
    default making_program_show_seven = False

    default making_program_one_true = "unselected"
    default making_program_two_true = "unselected"
    default making_program_three_true = "unselected"
    default making_program_four_true = "unselected"
    default making_program_five_true = "unselected"
    default making_program_six_true = "unselected"
    default making_program_seven_true = "unselected"

    default todo_one_colmpleted = False
    default todo_two_colmpleted = False
    default todo_three_colmpleted = False
    default todo_four_colmpleted = False
    default todo_five_colmpleted = False
    default todo_six_colmpleted = False

######### Переменные для поиска документов в комнате автора #########
    
    default first_document_finded = False
    default second_document_finded = False
    default third_document_finded = False
    default fourth_document_finded = False
    default fifth_document_finded = False

######### Переменные для переходов #########

    default flag_technical_label_1_2_1 = False
    default flag_technical_label_1_2_2 = False
    default flag_technical_label_1_5_2 = False
    default flag_technical_label_1_5_3 = False
    default flag_choosing_photo_1_5 = False
    default flag_technical_label_1_6 = False
    default flag_technical_label_1_7_1 = False
    default flag_technical_label_1_7_2 = False
    default flag_technical_label_1_8_1_1 = False
    default flag_technical_label_1_8_2 = False
    default flag_technical_label_1_8_3 = False

######### Переменные для мини-игры студия #########

    default window_finded = False
    default door_open_finded = False
    default sofits_finded = False
    default operator_finded = False
    default author_head_finded = False
    default author_garment_finded = False
    default author_hand_finded = False
    default text_finded = False


######### Переменные для мини-игры презентации ########

    default k = 0

    default flag_presentation1 = False
    default flag_presentation2 = False
    default flag_presentation3 = False
    default flag_presentation4 = False
    default flag_presentation5 = False
    default flag_presentation6 = False
    default flag_presentation7 = False
    default flag_presentation8 = False
    default flag_presentation9 = False
    default flag_presentation10 = False
    default flag_presentation11 = False


####### Для игры текст #######
    default flag_text = False

    default z = 0 
    define right_choise = 0
    default popitki = 0
    default game_over = False
    default game_vin = False
    default game_finish = False

    define lst = [False] * 110
    define lst2 = [False] * 110

######### Мини-игра "Авторское право" #########

    default first_game_copyright = True
    
    image text1_image = "images/copyright/level1/CC_BY.png"
    image text2_image = "images/copyright/level1/CC_BY-SA.png"
    image text3_image = "images/copyright/level1/CC_BY-ND.png"
    image text4_image = "images/copyright/level2/CC_BY-NC.png"
    image text5_image = "images/copyright/level2/CC_0.png"
    image text6_image = "images/copyright/level2/CC_BY-NC-ND.png"

    ### готовые ответы для их позиционирования по местам ###


    default text_position = [[0, 0], [0, 0], [0, 0], [0, 0]]
    default answer_full = [False, False, False, False]
    default answer_correct = [False, False, False, False]
    default answer_position = [[0, 0], [58, 507], [680, 507], [1302, 507]]
    default count_of_mistakes = 0
    default copyright_progress = 1
    default default_position = [0, 680, 1302, 58]
    
######### перетаскивание ответов в игре "авторское право" #########

    python:
        def answer_dragged(drags, drop):

            if not drop: #поставили вне поля ответа, возращаем в исходное положение
                if drags[0].drag_name == "CC_BY(1)" or drags[0].drag_name == "CC_BY-NC(1)":
                    return "text_reset1"
                elif drags[0].drag_name == "CC_BY-SA(2)" or drags[0].drag_name == "CC_0(2)":
                    return "text_reset2"
                else:
                    return "text_reset3"

            if drop: #поставили в поле ответа
                if drop.drag_name == "answer1": #поле ответа 1
                    if drags[0].drag_name == "CC_BY(1)" or drags[0].drag_name == "CC_BY-NC(1)":
                        return [1, 1]
                    elif drags[0].drag_name == "CC_BY-SA(2)" or drags[0].drag_name == "CC_0(2)":
                        return [1, 2]
                    else:
                        return [1, 3]
                    

                elif drop.drag_name == "answer2": #поле ответа 2
                    if drags[0].drag_name == "CC_BY-SA(2)" or drags[0].drag_name == "CC_0(2)":
                        return [2, 2]
                    elif drags[0].drag_name == "CC_BY(1)" or drags[0].drag_name == "CC_BY-NC(1)":
                        return [2, 1]
                    else:
                        return [2, 3]
                        
                else: #поле ответа 3
                    if drags[0].drag_name == "CC_BY-ND(3)" or drags[0].drag_name == "CC_BY-NC-ND(3)":
                        return [3, 3]
                    elif drags[0].drag_name == "CC_BY(1)" or drags[0].drag_name == "CC_BY-NC(1)":
                        return [3, 1]
                    else:
                        return [3, 2]


######### Мини-игра Гардероб Ж #########

    define flag_fifth_mini_game = False

    # 3 позиции верхней части одежды: основная, текущая и модельная (на манекене)
    define main_top_position_f = [[0, 0], [900, 118], [1010, 118], [1120, 118], [1240, 124], [1330, 118], [1440, 122]]
    default top_position_f = [[0, 0], [900, 118], [1010, 118], [1120, 118], [1240, 124], [1330, 118], [1440, 122]]
    define model_top_position_f = [[0,0], [0,0], [228, 192], [230, 196], [0,0], [0,0], [0,0]]
    image top1f = "images/wardrobe/female/top1_idle.png"
    image top2f = ConditionSwitch("top_ready[2]", "images/wardrobe/female/ready/top2_ready.png", True, "images/wardrobe/female/top2_idle.png")
    image top3f = ConditionSwitch("top_ready[3]", "images/wardrobe/female/ready/top3_ready.png", True, "images/wardrobe/female/top3_idle.png")
    image top4f = "images/wardrobe/female/top4_idle.png"
    image top5f = "images/wardrobe/female/top5_idle.png"
    image top6f = "images/wardrobe/female/top6_idle.png"

    # 3 позиции нижней части одежды: основная, текущая и модельная (на манекене)
    define main_bottom_position_f = [[0, 0], [945, 514], [1115, 521], [1230, 521], [1345, 520], [1485, 518]]
    default bottom_position_f = [[0, 0], [945, 514], [1115, 521], [1230, 521], [1345, 520], [1485, 518]]
    define model_bottom_position_f = [[0,0], [0,0], [302, 440], [0,0], [243,420], [0,0]]
    image bottom1f = "images/wardrobe/female/bottom1_idle.png"
    image bottom2f = ConditionSwitch("bottom_ready[2]", "images/wardrobe/female/ready/bottom2_ready.png", True, "images/wardrobe/female/bottom2_idle.png")
    image bottom3f = "images/wardrobe/female/bottom3_idle.png"
    image bottom4f = ConditionSwitch("bottom_ready[4]", "images/wardrobe/female/ready/bottom4_ready.png", True, "images/wardrobe/female/bottom4_idle.png")
    image bottom5f = "images/wardrobe/female/bottom5_idle.png"

    # 3 позиции обуви: основная, текущая и модельная (у манекена)
    define main_boots_position_f = [[0, 0], [990, 845], [1115, 875], [1245, 860], [1375, 765]]
    default boots_position_f = [[0, 0], [990, 845], [1115, 875], [1245, 860], [1375, 765]]
    define model_boots_position_f = [[0,0], [0,0], [300, 880], [300, 880], [0,0]]
    image boots1f = "images/wardrobe/female/boots1_idle.png"
    image boots2f = ConditionSwitch("boots_ready[2]", "images/wardrobe/female/ready/boots2_ready.png", True, "images/wardrobe/female/boots2_idle.png")
    image boots3f = ConditionSwitch("boots_ready[3]", "images/wardrobe/female/ready/boots3_ready.png", True, "images/wardrobe/female/boots3_idle.png")
    image boots4f = "images/wardrobe/female/boots4_idle.png"

    # реплики навигатора в зависимости от _return
    define navigator_str_f = {"1top1": "В свитере под софитами будет жарко.  Продолжайте поиск!",
                            "1top2": "Хороший выбор!",
                            "1top3": "Точно!  Эта блуза подойдет для съемок.",
                            "1top4": "Эту вещь поберегите для пляжа.  Поищите другую.",
                            "1top5": "Не подходит! Синий цвет \"не видит\" камера. ",
                            "1top6": "Черный цвет - неудачный выбор. Посмотрите что-то еще!",
                            "2bottom1": "Красивые брюки! Но слишком пестрые. Не берите!",
                            "2bottom2": "Да.  Это удачный выбор!",
                            "2bottom3": "Камера \"не любит\" черный цвет. Такие брюки не для съемки.",
                            "2bottom4": "Неплохо! Можно попробовать.",
                            "2bottom5": "Оттенки синего не рекомендованы. Лучше не рисковать!",
                            "3boots1": "В туфлях на высоких каблуках ноги устанут. Неудачный выбор.",
                            "3boots2": "Отлично! Берем.",
                            "3boots3": "Правильный выбор! Удобно и неслышно.",
                            "3boots4": "Жарко и некомфортно. Не подходит для студии."}


######### мини-игра Гардероб М #########

    # 3 позиции верхней части одежды: основная, текущая и модельная (на манекене)
    define main_top_position_m = [[0, 0], [920, 128], [1030, 128], [1140, 129], [1260, 129], [1360, 128]]
    default top_position_m = [[0, 0], [920, 128], [1030, 128], [1140, 128], [1260, 128], [1360, 128]]
    define model_top_position_m = [[0,0], [0,0], [0,0], [236, 192], [233, 188], [0,0]]
    image top1m = "images/wardrobe/male/top1_idle.png"
    image top2m = "images/wardrobe/male/top2_idle.png"
    image top3m = ConditionSwitch("top_ready[3]", "images/wardrobe/male/ready/top3_ready.png", True, "images/wardrobe/male/top3_idle.png")
    image top4m = ConditionSwitch("top_ready[4]", "images/wardrobe/male/ready/top4_ready.png", True, "images/wardrobe/male/top4_idle.png")
    image top5m = "images/wardrobe/male/top5_idle.png"

    # 3 позиции нижней части одежды: основная, текущая и модельная (на манекене)
    define main_bottom_position_m = [[0, 0], [945, 524], [1115, 523], [1300, 524], [1345, 524]]
    default bottom_position_m = [[0, 0], [945, 524], [1115, 523], [1300, 524], [1450, 524]]
    define model_bottom_position_m = [[0,0], [270, 470], [276, 475], [0,0], [0,0]]
    image bottom1m = ConditionSwitch("bottom_ready[1]", "images/wardrobe/male/ready/bottom1_ready.png", True, "images/wardrobe/male/bottom1_idle.png")
    image bottom2m = ConditionSwitch("bottom_ready[2]", "images/wardrobe/male/ready/bottom2_ready.png", True, "images/wardrobe/male/bottom2_idle.png")
    image bottom3m = "images/wardrobe/male/bottom3_idle.png"
    image bottom4m = "images/wardrobe/male/bottom4_idle.png"
    #поменять!!!

    # 3 позиции обуви: основная, текущая и модельная (на манекене)
    define main_boots_position_m = [[0, 0], [990, 885], [1145, 875], [1275, 890], [1390, 840]]
    default boots_position_m = [[0, 0], [990, 885], [1145, 875], [1275, 890], [1390, 840]]
    define model_boots_position_m = [[0,0], [300, 900], [300, 880], [0,0], [0,0]]
    image boots1m = ConditionSwitch("boots_ready[1]", "images/wardrobe/male/ready/boots1_ready.png", True, "images/wardrobe/male/boots1_idle.png")
    image boots2m = ConditionSwitch("boots_ready[2]", "images/wardrobe/male/ready/boots2_ready.png", True, "images/wardrobe/male/boots2_idle.png")
    image boots3m = "images/wardrobe/male/boots3_idle.png"
    image boots4m = "images/wardrobe/male/boots4_idle.png"

    # реплики навигатора в зависимости от _return
    define navigator_str_m = {"1top1": "Белый цвет для съемок - неудачный выбор. Продолжайте поиск!",
                            "1top2": "Не подходит! Синий цвет \"не видит\" камера. ",
                            "1top3": "Точно!  Эта рубашка подойдет для съемок.",
                            "1top4": "Отличный выбор!",
                            "1top5": "Черный цвет - неудачный выбор. Посмотрите что-то еще!",
                            "2bottom1": "Красивые брюки! И цвет подходящий. Берите!",
                            "2bottom2": "Неплохо! Можно попробовать.",
                            "2bottom3": "Камера \"не любит\" черный цвет. Такие брюки не для съемки.",
                            "2bottom4": "Эту вещь поберегите для пляжа.  Поищите другую.",
                            "3boots1": "Отлично! Берем.",
                            "3boots2": "Правильный выбор! Удобно и неслышно.",
                            "3boots3": "Шумная обувь. Не берите. У Вас есть другие варианты.",
                            "3boots4": "Жарко и некомфортно. Не подходит для студии."}

######### Общее: Гардероб М+Ж #########
    
    default top_ready = [False, False, False, False, False, False, False]
    default bottom_ready = [False, False, False, False, False, False]
    default boots_ready = [False, False, False, False, False]
    default correct_answer = False
    default first_game_wardrobe = True


######### Мини-игра Зеркало Ж #########

    image character_bg_f = ConditionSwitch("haircut_ready[3]", "images/mirror/female/haircut/haircut3_ready.png", 
                                        "haircut_ready[4]", "images/mirror/female/haircut/haircut4_ready.png",
                                        True, "images/mirror/female/character_bg.png")

    define main_haircut_position_f = [[0,0], [615, 430], [668, 95], [1047, 88], [1115, 390]]
    image haircut1f = "images/mirror/female/haircut/haircut1.png"
    image haircut2f = "images/mirror/female/haircut/haircut2.png"
    image haircut3f = "images/mirror/female/haircut/haircut3.png"
    image haircut4f = "images/mirror/female/haircut/haircut4.png"

    # 3 позиции украшений и косметики: основная, текущая и модельная (на персонаже)
    define main_add_position_f = [[0, 0], [559, 669], [547, 276], [1268, 280], [1272, 594], [700, 800], [850, 850], [1100, 790]]
    default add_position_f = [[0, 0], [559, 669], [547, 276], [1268, 280], [1272, 594], [700, 800], [850, 850], [1100, 790]]
    define add_model_position_f = [[0, 0], [750, 221], [0, 0], [750, 221], [0, 0], [750, 221], [750, 221], [750, 221]]
    image add1f = ConditionSwitch("add_ready[1]", "images/mirror/female/add/add1_ready.png", True, "images/mirror/female/add/add1.png")
    image add2f = "images/mirror/female/add/add2.png"
    image add3f = ConditionSwitch("add_ready[3]", "images/mirror/female/add/add3_ready.png", True, "images/mirror/female/add/add3.png")
    image add4f = "images/mirror/female/add/add4.png"
    image add5f = ConditionSwitch("add_ready[5]", "images/mirror/female/add/add5_ready.png", True, "images/mirror/female/add/add5.png")
    image add6f = ConditionSwitch("add_ready[6]", "images/mirror/female/add/add6_ready.png", True, "images/mirror/female/add/add6.png")
    image add7f = ConditionSwitch("add_ready[7]", "images/mirror/female/add/add7_ready.png", True, "images/mirror/female/add/add7.png")
    
    # неактивная косметика
    image add5_inactive_f = "images/mirror/female/add/add5.png"
    image add6_inactive_f = "images/mirror/female/add/add6.png"
    image add7_inactive_f = "images/mirror/female/add/add7.png"

    # реплики навигатора в зависимости от _return
    define navigator_mirror_str_f = { "haircut1": "Волосы должны быть аккуратно уложены. Попробуйте другую прическу!",
                                    "haircut2": "Эту прическу будет трудно повторить. Не подходит!",
                                    "haircut3": "Неплохо! Давайте попробуем.",
                                    "haircut4": "Хороший выбор! Вам идёт!",
                                    "add1": "Отлично! Берем.",
                                    "add2": "Подвески издают ненужный шум.  Возьмите что-то другое!",
                                    "add3": "Да.  Это удачный выбор!",
                                    "add4": "Красиво! Но приберегите такие бусы для другого случая. ",
                                    "add5": "Точно!  Неяркая помада подойдет для съемок. ",
                                    "add6": "Всё верно! ",
                                    "add7": "Вы не ошиблись! Матовая пудра обязательно нужна." }


######### Мини-игра Зеркало М #########

    image character_bg_m = ConditionSwitch( "haircut_ready[1]", "images/mirror/male/haircut/haircut1_ready.png",
                                            "haircut_ready[3]", "images/mirror/male/haircut/haircut3_ready.png",
                                            True, "images/mirror/male/character_bg.png")

    define main_haircut_position_m = [[0,0], [618, 402], [679, 87], [1063, 124], [1125, 387]]
    image haircut1m = "images/mirror/male/haircut/haircut1.png"
    image haircut2m = "images/mirror/male/haircut/haircut2.png"
    image haircut3m = "images/mirror/male/haircut/haircut3.png"
    image haircut4m = "images/mirror/male/haircut/haircut4.png"

    # 3 позиции украшений и косметики: основная, текущая и модельная (на персонаже)
    define main_add_position_m = [[0, 0], [582, 660], [563, 245], [1237, 333], [1267, 610], [658, 855], [824, 880], [1048, 890], [1090, 755]]
    define add_position_m = [[0, 0], [582, 660], [563, 245], [1237, 333], [1267, 610], [658, 855], [824, 880], [1048, 890], [1150, 860]]
    define add_model_position_m = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [725, 185], [0, 0], [755, 180]]
    image add1m = "images/mirror/male/add/add1.png"
    image add2m = "images/mirror/male/add/add2.png"
    image add3m = "images/mirror/male/add/add3.png"
    image add4m = "images/mirror/male/add/add4.png"
    image add5m = "images/mirror/male/add/add5.png"
    image add6m = ConditionSwitch("add_ready[6]", "images/mirror/male/add/add6_ready.png", True, "images/mirror/male/add/add6.png")
    image add7m = "images/mirror/male/add/add7.png"
    image add8m = ConditionSwitch("add_ready[8]", "images/mirror/male/add/add8_ready.png", True, "images/mirror/male/add/add8.png")
    
    # неактивная косметика
    image add8_inactive_m = "images/mirror/male/add/add8.png"


    # реплики навигатора в зависимости от _return
    define navigator_mirror_str_m = { "haircut1": "Да.  Это удачный выбор!",
                                    "haircut2":  "Волосы должны быть аккуратно уложены. Попробуйте другую прическу!",
                                    "haircut3": "Хороший выбор! Вам идёт!",
                                    "haircut4": "Важно в кадре выглядеть опрятно. Такой вариант не подходит!",
                                    "add1": "Красиво! Но приберегите для другого случая.",
                                    "add2": "Камера \"не любит\" оттенки синего и лишний блеск.  Возьмите что-то другое!",
                                    "add3": "Красиво!  Но шумит при движении. Не берите!",
                                    "add4": "Неплохо! Давайте попробуем.",
                                    "add5": "Красный цвет - не лучший выбор. Посмотрите другие варианты.",
                                    "add6": "Отлично! Берем.",
                                    "add7": "Не рекомендуется мелкая полоска. И цвет неудачный для съемок.",
                                    "add8": "Вы не ошиблись! Матовая пудра обязательно нужна." }


######### Общее: Зеркало М+Ж #########

    default haircut_ready = [False, False, False, False, False]
    default add_ready = [False, False, False, False, False, False, False, False, False]
    default first_game_mirror = True
