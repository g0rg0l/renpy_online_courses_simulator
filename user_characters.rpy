init 2:

    ######## Навигатор ########

    define navigator = DynamicCharacter("navigator_name",
    image = "navigator_icon",
    color="#00008B")

    image side navigator_icon = "images/characters/navigator/icon.png"



    ######## Декан ########

    define headOfDepartment = Character("Заведующий кафедры",
    image="headOfDepartment_icon",
    color="#00008B")

    image side headOfDepartment_icon = "images/characters/headOfDepartment/headOfDepartment_icon.png"

    image headOfDepartment normal = "images/characters/headOfDepartment/head_of_department_normal.png"
    image headOfDepartment funny = "images/characters/headOfDepartment/head_of_department_funny.png"
    image headOfDepartment medium_funny = "images/characters/headOfDepartment/head_of_department_medium_funny.png"
    image headOfDepartment sad = "images/characters/headOfDepartment/head_of_department_sad.png"




    ######## Екатерина ########

    define ekaterina_hiden = Character("Сотрудник Центра",
    image="ekaterina_icon",
    color="#00008B")

    define ekaterina = Character("Екатерина",
    image="ekaterina_icon",
    color="#00008B")

    image ekaterina normal_1 = "images/characters/ekaterina/ekaterina_normal_1.png"
    image ekaterina normal_2 = "images/characters/ekaterina/ekaterina_normal_2.png"
    image ekaterina funny = "images/characters/ekaterina/ekaterina_funny.png"
    image ekaterina sad = "images/characters/ekaterina/ekaterina_sad.png"
    image ekaterina pry = "images/characters/ekaterina/ekaterina_pry.png"

    image side ekaterina_icon = "images/characters/ekaterina/ekaterina_icon.png"



    ######## Игрок ########

    define male_player = Character("[name]",
    image="player_icon_male")

    define female_player = Character("[name]",
    image="player_icon_female")

    image side player_icon_male = "images/characters/player/male_icon.png"
    image side player_icon_female = "images/characters/player/female_icon.png"



    ######## Питомцы ########

    define cat = Character("[pet_name]",
    image="cat_icon",
    color="#00008B")

    define dog = Character("[pet_name]",
    image="dog_icon",
    color="#00008B")

    image side cat_icon = "images/characters/cat/cat_icon.png"
    
    image side dog_icon = "images/characters/dog/dog_icon.png"



