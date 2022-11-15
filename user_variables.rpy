init:
######### Сведения об игроке #########
    default name = ""
    default sex = ""
    default pet = ""
    default pet_name = "???"

######### имя навигатора #########

    default navigator_name = "???"

######### Внутреигровые настройки #########
    default preferences.text_cps = 32 # скорость воспроизведения текста по умолчанию
    define gui.text_color = "#000000"
    define gui.dialogue_width = 875
    define gui.name_xpos = 675
    define gui.name_ypos = 52
    define gui.dialogue_xpos = 675
    define gui.dialogue_ypos = 119

    define config.hard_rollback_limit = 0 # запрет действия "назад"

######### Элементы комнаты #########
    default flag_room_door_opened = False
    default flag_room_album_opened = False
    default flag_room_computer_opened = False
    default flag_room_pet_opened = False
    default flag_room_cupboard_opened = False

    default flag_room_broken = False

    default arrow_at_computer = False
    default arrow_at_door_at_home = False
    default arrow_at_pet = False
    default arrow_at_album = False
    default arrow_at_message_icon = False
    default arrow_at_todo_icon = False

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

######### Вспомогательные переменные для мини-игр #########
    default amount_of_clicks = 0

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