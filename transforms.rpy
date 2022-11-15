init 4:

### Движение стрелок ###

    transform arrow_move(x, y):
        xalign x
        yalign y

        linear 0.8 xalign x + 0.02
        linear 0.8 xalign x
        
        repeat

    transform arrow_move_vert(x, y):
        xalign x
        yalign y

        linear 0.8 yalign y + 0.02
        linear 0.8 yalign y

        repeat

### Эффект исчезновения ###

    transform dslv(x=0.5):

        align(x, 1.0)

        on show:
            alpha 0.0
            linear 0.1 alpha 1.0
        on hide:
            linear 0.1 alpha 0.0