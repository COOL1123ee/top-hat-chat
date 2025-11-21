@namespace
class SpriteKind:
    NPC = SpriteKind.create()

def on_player4_button_up_pressed():
    animation.run_image_animation(mySprite4,
        assets.animation("""
            borv4j
            """),
        100,
        True)
controller.player4.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player4_button_up_pressed)

def on_player4_button_up_released():
    animation.run_image_animation(mySprite4,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 5 . . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 5 5 5 5 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 5 . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 5 5 5 5 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player4.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.RELEASED,
    on_player4_button_up_released)

def on_player4_connected():
    global mySprite4
    mySprite4 = sprites.create(img("""
            . . . . . . f f f f f . . . . .
            . . . . . . f f f f f . . . . .
            . . . . . . f f f f f . . . . .
            . . . . . . 5 5 5 5 5 . . . . .
            . . . . . f f f f f f f . . . .
            . . . . . . 5 5 5 5 5 . . . . .
            . . . . . 5 5 5 5 5 5 5 . . . .
            . . . . . 5 9 9 f 9 9 5 . . . .
            . . . . 5 5 9 9 f 9 9 5 5 . . .
            . . . 5 . 5 5 5 5 5 5 5 . 5 . .
            . . . 5 . 5 5 f f f 5 5 . 5 . .
            . . . . . . 5 5 5 5 5 . . . . .
            . . . . . . 5 . . . 5 . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.player)
    controller.player4.move_sprite(mySprite4)
controller.player4.on_event(ControllerEvent.CONNECTED, on_player4_connected)

def on_up_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . 4 4 4 4 4 4 4 . 4 . . .
                . . . . 4 4 4 4 4 4 4 . 4 . . .
                . . . 4 4 4 4 4 4 4 4 4 . . . .
                . . 4 . 4 4 4 4 4 4 4 . . . . .
                . . 4 . 4 4 4 4 4 4 4 . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . . 4 . . . 4 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . 4 . 4 4 4 4 4 4 4 . . . . .
                . . 4 . 4 4 4 4 4 4 4 . . . . .
                . . . 4 4 4 4 4 4 4 4 4 . . . .
                . . . . 4 4 4 4 4 4 4 . 4 . . .
                . . . . 4 4 4 4 4 4 4 . 4 . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . . 4 . . . 4 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        100,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_player4_button_left_released():
    animation.run_image_animation(mySprite3,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 5 . . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 5 5 5 5 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 5 . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 5 5 5 5 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player4.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.RELEASED,
    on_player4_button_left_released)

def on_player3_button_up_released():
    animation.run_image_animation(mySprite3,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 7 7 7 7 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . . . . .
                . . . . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                . . 7 . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 7 7 7 7 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . . . . .
                . . . . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                . . 7 . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 7 7 7 7 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 7 . . 7 7 7 7 7 . . . . . .
                . . 7 . 7 7 7 7 7 7 7 . . . . .
                . . 7 . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . . . 7 7 7 7 7 7 7 . 7 . . .
                . . . . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 7 7 7 7 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 7 . 7 7 7 7 7 . . . . . .
                . . 7 . 7 7 7 7 7 7 7 . . . . .
                . . 7 . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . . . 7 7 7 7 7 7 7 . 7 . . .
                . . . . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 7 7 7 7 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . . . . .
                . . . . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                . . 7 . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player3.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.RELEASED,
    on_player3_button_up_released)

def on_player4_button_b_released():
    animation.run_image_animation(mySprite2,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 5 . . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 5 5 5 5 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 5 . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 5 5 5 5 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player4.on_button_event(ControllerButton.B,
    ControllerButtonEvent.RELEASED,
    on_player4_button_b_released)

def on_player3_button_down_released():
    animation.run_image_animation(mySprite3,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 7 7 7 7 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . . . . .
                . . . . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                . . 7 . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 7 7 7 7 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . . . . .
                . . . . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                . . 7 . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 7 7 7 7 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 7 . . 7 7 7 7 7 . . . . . .
                . . 7 . 7 7 7 7 7 7 7 . . . . .
                . . 7 . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . . . 7 7 7 7 7 7 7 . 7 . . .
                . . . . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 7 7 7 7 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 7 . 7 7 7 7 7 . . . . . .
                . . 7 . 7 7 7 7 7 7 7 . . . . .
                . . 7 . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . . . 7 7 7 7 7 7 7 . 7 . . .
                . . . . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 7 7 7 7 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . . . . .
                . . . . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                . . 7 . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player3.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.RELEASED,
    on_player3_button_down_released)

def on_player4_button_down_released():
    animation.run_image_animation(mySprite4,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 5 . . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 5 5 5 5 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 5 . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 5 5 5 5 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player4.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.RELEASED,
    on_player4_button_down_released)

def on_a_pressed():
    global rspons
    rspons = game.ask_for_string("talk to your buds. say party for a party", 24)
    mySprite.say_text(rspons, 1000, False)
    if rspons == "party":
        scene.set_background_image(img("""
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbbbbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbb2bbbbbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbb2bbbbbbbbbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbbbbbbbbbbbbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbbbbbb2bbbbbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbb222bbbbb2bbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbb2bbbb2bb2bbbbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbb2bbbbbbbbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffb2bbbbbbbbb2bbbbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbbb2bbbbb2bbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbbbbbbbb2bbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbb2b2bb2bb2bb2bbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbbb2bbbbbbbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbbb2b2bbbbbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbb2bbbbbb2bbbbbbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbbbbbbbbbbbbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbb2bbbbbbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbbbbbbbbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbbbbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            f555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf888888888888888888888888888888888888888888ff
            f555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf888888888888888888888888888888888888888888ff
            f555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf888888888888888888888888888888888888888888ff
            f555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf888888888888888888888888888888888888888888ff
            f555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf888888888888888888888888888888888888888888ff
            f555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf888888888888888888888888888888888888888888ff
            f555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf888888888888888888888888888888888888888888ff
            f555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf888888888888888888888888888888888888888888ff
            f555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf888888888888888888888888888888888888888888ff
            f555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf888888888888888888888888888888888888888888ff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf55555555555555555555555555555555555555555555555555555555555555555555faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf88888888888888888888888888888888888888888888888888888888888888888888f555555555555555555555555555555555555555555f2
            faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf88888888888888888888888888888888888888888888888888888888888888888888f555555555555555555555555555555555555555555f2
            faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf88888888888888888888888888888888888888888888888888888888888888888888f555555555555555555555555555555555555555555f2
            faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf88888888888888888888888888888888888888888888888888888888888888888888f555555555555555555555555555555555555555555f2
            faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf88888888888888888888888888888888888888888888888888888888888888888888f555555555555555555555555555555555555555555f2
            faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf88888888888888888888888888888888888888888888888888888888888888888888f555555555555555555555555555555555555555555f2
            faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf88888888888888888888888888888888888888888888888888888888888888888888f555555555555555555555555555555555555555555f2
            faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf88888888888888888888888888888888888888888888888888888888888888888888f555555555555555555555555555555555555555555f2
            faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf88888888888888888888888888888888888888888888888888888888888888888888f555555555555555555555555555555555555555555f2
            faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf88888888888888888888888888888888888888888888888888888888888888888888f555555555555555555555555555555555555555555f2
            faafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            faaf888888888888888888888888888888888888888888faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            faaf888888888888888888888888888888888888888888faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            faaf888888888888888888888888888888888888888888faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            faaf888888888888888888888888888888888888888888faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            faaf888888888888888888888888888888888888888888faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            faaf888888888888888888888888888888888888888888faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            faaf888888888888888888888888888888888888888888faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            faaf888888888888888888888888888888888888888888faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            faaf888888888888888888888888888888888888888888faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            faaf888888888888888888888888888888888888888888faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff
            faafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2
            """))
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 4 4 4 4 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . . . 4 4 4 4 4 4 4 . . . . .
                    . . . . 4 9 9 f 9 9 4 . . . . .
                    . . . 4 4 9 9 f 9 9 4 4 . . . .
                    . . 4 . 4 4 4 4 4 4 4 . 4 . . .
                    . . 4 . 4 4 f f f 4 4 . 4 . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . . . . 4 . . . 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 4 4 4 4 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . 4 . 4 4 4 4 4 4 4 . 4 . . .
                    . . 4 . 4 9 9 f 9 9 4 . 4 . . .
                    . . . 4 4 9 9 f 9 9 4 4 . . . .
                    . . . . 4 4 4 4 4 4 4 . . . . .
                    . . . . 4 4 f f f 4 4 . . . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . . . . 4 . . . 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 4 4 4 4 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . . . 4 4 4 4 4 4 4 . . . . .
                    . . . . 4 9 9 f 9 9 4 . . . . .
                    . . . 4 4 9 9 f 9 9 4 4 . . . .
                    . . 4 . 4 4 4 4 4 4 4 . 4 . . .
                    . . 4 . 4 4 f f f 4 4 . 4 . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . . . . 4 . . . 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 4 4 4 4 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . . . 4 4 4 4 4 4 4 . . . . .
                    . . . . 4 9 9 f 9 9 4 . . . . .
                    . . . 4 4 9 9 f 9 9 4 4 . . . .
                    . . 4 . 4 4 4 4 4 4 4 . 4 . . .
                    . . 4 . 4 4 f f f 4 4 . 4 . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . . . . 4 . . . 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 4 4 4 4 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . 4 . 4 4 4 4 4 4 4 . 4 . . .
                    . . 4 . 4 9 9 f 9 9 4 . 4 . . .
                    . . . 4 4 9 9 f 9 9 4 4 . . . .
                    . . . . 4 4 4 4 4 4 4 . . . . .
                    . . . . 4 4 f f f 4 4 . . . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . . . . 4 . . . 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 4 4 4 4 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . . . 4 4 4 4 4 4 4 . 4 . . .
                    . . . . 4 9 9 f 9 9 4 . 4 . . .
                    . . . 4 4 9 9 f 9 9 4 4 . . . .
                    . . 4 . 4 4 4 4 4 4 4 . . . . .
                    . . 4 . 4 4 f f f 4 4 . . . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . . . . 4 . . . 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . 4 . 4 4 4 4 4 4 4 . . . . .
                    . . 4 . 4 9 9 f 9 9 4 . . . . .
                    . . . 4 4 9 9 f 9 9 4 4 . . . .
                    . . . . 4 4 4 4 4 4 4 . 4 . . .
                    . . . . 4 4 f f f 4 4 . 4 . . .
                    . . . . . 4 4 4 4 4 . . . . . .
                    . . . . . 4 . . . 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f . . . . . . . .
                    . . . . . . 4 4 . . . . . . . .
                    . . . . . f f f f f . . . . . .
                    . . . . . . 4 4 . . . . . . . .
                    . . . . 4 . 4 4 . . . . . . . .
                    . . . . . 4 4 4 4 . . . . . . .
                    . . . . . . 4 4 . 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f . . . . . . . .
                    . . . . . . 4 4 . . . . . . . .
                    . . . . . f f f f f . . . . . .
                    . . . . . . 4 4 . . . . . . . .
                    . . . . . . 4 4 . 4 . . . . . .
                    . . . . . 4 4 4 4 . . . . . . .
                    . . . . 4 . 4 4 . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """)],
            500,
            True)
        animation.run_image_animation(mySprite2,
            [img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 3 3 3 3 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 3 3 3 3 3 . . . . . .
                    . . . . 3 3 3 3 3 3 3 . . . . .
                    . . . . 3 9 9 f 9 9 3 . . . . .
                    . . . 3 3 9 9 f 9 9 3 3 . . . .
                    . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                    . . 3 . 3 3 f f f 3 3 . 3 . . .
                    . . . . . 3 3 3 3 3 . . . . . .
                    . . . . . 3 . . . 3 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 3 3 3 3 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 3 3 3 3 3 . . . . . .
                    . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                    . . 3 . 3 9 9 f 9 9 3 . 3 . . .
                    . . . 3 3 9 9 f 9 9 3 3 . . . .
                    . . . . 3 3 3 3 3 3 3 . . . . .
                    . . . . 3 3 f f f 3 3 . . . . .
                    . . . . . 3 3 3 3 3 . . . . . .
                    . . . . . 3 . . . 3 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 3 3 3 3 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 3 3 3 3 3 . . . . . .
                    . . . . 3 3 3 3 3 3 3 . . . . .
                    . . . . 3 9 9 f 9 9 3 . . . . .
                    . . . 3 3 9 9 f 9 9 3 3 . . . .
                    . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                    . . 3 . 3 3 f f f 3 3 . 3 . . .
                    . . . . . 3 3 3 3 3 . . . . . .
                    . . . . . 3 . . . 3 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                    . . 5 . 5 9 9 f 9 9 5 . 5 . . .
                    . . . 5 5 9 9 f 9 9 5 5 . . . .
                    . . . . 5 5 5 5 5 5 5 . . . . .
                    . . . . 5 5 f f f 5 5 . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . . 5 . . . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . 5 5 5 5 5 5 5 . . . . .
                    . . . . 5 9 9 f 9 9 5 . . . . .
                    . . . 5 5 9 9 f 9 9 5 5 . . . .
                    . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                    . . 5 . 5 5 f f f 5 5 . 5 . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . . 5 . . . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . 5 5 5 5 5 5 5 . 5 . . .
                    . . . . 5 9 9 f 9 9 5 . 5 . . .
                    . . . 5 5 9 9 f 9 9 5 5 . . . .
                    . . 5 . 5 5 5 5 5 5 5 . . . . .
                    . . 5 . 5 5 f f f 5 5 . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . . 5 . . . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . 5 . 5 5 5 5 5 5 5 . . . . .
                    . . 5 . 5 9 9 f 9 9 5 . . . . .
                    . . . 5 5 9 9 f 9 9 5 5 . . . .
                    . . . . 5 5 5 5 5 5 5 . 5 . . .
                    . . . . 5 5 f f f 5 5 . 5 . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . . 5 . . . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f . . . . . . . .
                    . . . . . . 5 5 . . . . . . . .
                    . . . . . f f f f f . . . . . .
                    . . . . . . 5 5 . . . . . . . .
                    . . . . 5 . 5 5 . . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . . . 5 5 . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f . . . . . . . .
                    . . . . . . 5 5 . . . . . . . .
                    . . . . . f f f f f . . . . . .
                    . . . . . . 5 5 . . . . . . . .
                    . . . . . . 5 5 . 5 . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . 5 . 5 5 . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """)],
            500,
            True)
        animation.run_image_animation(mySprite3,
            [img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 7 7 7 7 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . . . 7 7 7 7 7 7 7 . . . . .
                    . . . . 7 9 9 f 9 9 7 . . . . .
                    . . . 7 7 9 9 f 9 9 7 7 . . . .
                    . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                    . . 7 . 7 7 f f f 7 7 . 7 . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . . . . 7 . . . 7 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 7 7 7 7 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                    . . 7 . 7 9 9 f 9 9 7 . 7 . . .
                    . . . 7 7 9 9 f 9 9 7 7 . . . .
                    . . . . 7 7 7 7 7 7 7 . . . . .
                    . . . . 7 7 f f f 7 7 . . . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . . . . 7 . . . 7 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 7 7 7 7 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . . . 7 7 7 7 7 7 7 . . . . .
                    . . . . 7 9 9 f 9 9 7 . . . . .
                    . . . 7 7 9 9 f 9 9 7 7 . . . .
                    . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                    . . 7 . 7 7 f f f 7 7 . 7 . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . . . . 7 . . . 7 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 7 7 7 7 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                    . . 7 . 7 9 9 f 9 9 7 . 7 . . .
                    . . . 7 7 9 9 f 9 9 7 7 . . . .
                    . . . . 7 7 7 7 7 7 7 . . . . .
                    . . . . 7 7 f f f 7 7 . . . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . . . . 7 . . . 7 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 7 7 7 7 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . . . 7 7 7 7 7 7 7 . . . . .
                    . . . . 7 9 9 f 9 9 7 . . . . .
                    . . . 7 7 9 9 f 9 9 7 7 . . . .
                    . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                    . . 7 . 7 7 f f f 7 7 . 7 . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . . . . 7 . . . 7 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 7 7 7 7 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . . . 7 7 7 7 7 7 7 . 7 . . .
                    . . . . 7 9 9 f 9 9 7 . 7 . . .
                    . . . 7 7 9 9 f 9 9 7 7 . . . .
                    . . 7 . 7 7 7 7 7 7 7 . . . . .
                    . . 7 . 7 7 f f f 7 7 . . . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . . . . 7 . . . 7 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 7 7 7 7 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . 7 . 7 7 7 7 7 7 7 . . . . .
                    . . 7 . 7 9 9 f 9 9 7 . . . . .
                    . . . 7 7 9 9 f 9 9 7 7 . . . .
                    . . . . 7 7 7 7 7 7 7 . 7 . . .
                    . . . . 7 7 f f f 7 7 . 7 . . .
                    . . . . . 7 7 7 7 7 . . . . . .
                    . . . . . 7 . . . 7 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f . . . . . . . .
                    . . . . . . 7 7 . . . . . . . .
                    . . . . . f f f f f . . . . . .
                    . . . . . . 7 7 . . . . . . . .
                    . . . . 7 . 7 7 . . . . . . . .
                    . . . . . 7 7 7 7 . . . . . . .
                    . . . . . . 7 7 . 7 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f . . . . . . . .
                    . . . . . . 7 7 . . . . . . . .
                    . . . . . f f f f f . . . . . .
                    . . . . . . 7 7 . . . . . . . .
                    . . . . . . 7 7 . 7 . . . . . .
                    . . . . . 7 7 7 7 . . . . . . .
                    . . . . 7 . 7 7 . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """)],
            500,
            True)
        animation.run_image_animation(mySprite4,
            [img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . 5 5 5 5 5 5 5 . . . . .
                    . . . . 5 9 9 f 9 9 5 . . . . .
                    . . . 5 5 9 9 f 9 9 5 5 . . . .
                    . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                    . . 5 . 5 5 f f f 5 5 . 5 . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . . 5 . . . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                    . . 5 . 5 9 9 f 9 9 5 . 5 . . .
                    . . . 5 5 9 9 f 9 9 5 5 . . . .
                    . . . . 5 5 5 5 5 5 5 . . . . .
                    . . . . 5 5 f f f 5 5 . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . . 5 . . . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . 5 5 5 5 5 5 5 . . . . .
                    . . . . 5 9 9 f 9 9 5 . . . . .
                    . . . 5 5 9 9 f 9 9 5 5 . . . .
                    . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                    . . 5 . 5 5 f f f 5 5 . 5 . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . . 5 . . . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                    . . 5 . 5 9 9 f 9 9 5 . 5 . . .
                    . . . 5 5 9 9 f 9 9 5 5 . . . .
                    . . . . 5 5 5 5 5 5 5 . . . . .
                    . . . . 5 5 f f f 5 5 . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . . 5 . . . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . 5 5 5 5 5 5 5 . . . . .
                    . . . . 5 9 9 f 9 9 5 . . . . .
                    . . . 5 5 9 9 f 9 9 5 5 . . . .
                    . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                    . . 5 . 5 5 f f f 5 5 . 5 . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . . 5 . . . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . 5 5 5 5 5 5 5 . 5 . . .
                    . . . . 5 9 9 f 9 9 5 . 5 . . .
                    . . . 5 5 9 9 f 9 9 5 5 . . . .
                    . . 5 . 5 5 5 5 5 5 5 . . . . .
                    . . 5 . 5 5 f f f 5 5 . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . . 5 . . . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . f f f f . . . . . . .
                    . . . . . f f f f . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . 5 . 5 5 5 5 5 5 5 . . . . .
                    . . 5 . 5 9 9 f 9 9 5 . . . . .
                    . . . 5 5 9 9 f 9 9 5 5 . . . .
                    . . . . 5 5 5 5 5 5 5 . 5 . . .
                    . . . . 5 5 f f f 5 5 . 5 . . .
                    . . . . . 5 5 5 5 5 . . . . . .
                    . . . . . 5 . . . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f . . . . . . . .
                    . . . . . . 5 5 . . . . . . . .
                    . . . . . f f f f f . . . . . .
                    . . . . . . 5 5 . . . . . . . .
                    . . . . 5 . 5 5 . . . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . . . 5 5 . 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f . . . . . . . .
                    . . . . . . 5 5 . . . . . . . .
                    . . . . . f f f f f . . . . . .
                    . . . . . . 5 5 . . . . . . . .
                    . . . . . . 5 5 . 5 . . . . . .
                    . . . . . 5 5 5 5 . . . . . . .
                    . . . . 5 . 5 5 . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """)],
            500,
            True)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_player2_button_a_pressed():
    global rspons
    rspons = game.ask_for_string("type what you want to say to your friends", 24)
    mySprite2.say_text(rspons, 1000, False)
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_player2_button_down_pressed():
    animation.run_image_animation(mySprite2,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . . 3 3 3 3 3 3 3 3 3 . . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . 3 3 3 3 3 3 3 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                """)],
        500,
        True)
controller.player2.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player2_button_down_pressed)

def on_button_released():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 4 4 4 4 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . 4 4 4 4 4 4 4 . . . . .
                . . . . 4 9 9 f 9 9 4 . . . . .
                . . . 4 4 9 9 f 9 9 4 4 . . . .
                . . 4 . 4 4 4 4 4 4 4 . 4 . . .
                . . 4 . 4 4 f f f 4 4 . 4 . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . . 4 . . . 4 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 4 4 4 4 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . 4 4 4 4 4 4 4 . . . . .
                . . . . 4 9 9 f 9 9 4 . . . . .
                . . . 4 4 9 9 f 9 9 4 4 . . . .
                . . 4 . 4 4 4 4 4 4 4 . 4 . . .
                . . 4 . 4 4 f f f 4 4 . 4 . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . . 4 . . . 4 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 4 4 4 4 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 4 . . 4 4 4 4 4 . . . . . .
                . . 4 . 4 4 4 4 4 4 4 . . . . .
                . . 4 . 4 9 9 f 9 9 4 . . . . .
                . . . 4 4 9 9 f 9 9 4 4 . . . .
                . . . . 4 4 4 4 4 4 4 . 4 . . .
                . . . . 4 4 f f f 4 4 . 4 . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . . 4 . . . 4 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 4 4 4 4 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 4 . 4 4 4 4 4 . . . . . .
                . . 4 . 4 4 4 4 4 4 4 . . . . .
                . . 4 . 4 9 9 f 9 9 4 . . . . .
                . . . 4 4 9 9 f 9 9 4 4 . . . .
                . . . . 4 4 4 4 4 4 4 . 4 . . .
                . . . . 4 4 f f f 4 4 . 4 . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . . 4 . . . 4 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 4 4 4 4 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . 4 4 4 4 4 4 4 . . . . .
                . . . . 4 9 9 f 9 9 4 . . . . .
                . . . 4 4 9 9 f 9 9 4 4 . . . .
                . . 4 . 4 4 4 4 4 4 4 . 4 . . .
                . . 4 . 4 4 f f f 4 4 . 4 . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . . 4 . . . 4 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.any_button.on_event(ControllerButtonEvent.RELEASED, on_button_released)

def on_player3_button_right_released():
    animation.run_image_animation(mySprite3,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 7 7 7 7 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . . . . .
                . . . . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                . . 7 . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 7 7 7 7 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . . . . .
                . . . . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                . . 7 . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 7 7 7 7 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 7 . . 7 7 7 7 7 . . . . . .
                . . 7 . 7 7 7 7 7 7 7 . . . . .
                . . 7 . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . . . 7 7 7 7 7 7 7 . 7 . . .
                . . . . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 7 7 7 7 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 7 . 7 7 7 7 7 . . . . . .
                . . 7 . 7 7 7 7 7 7 7 . . . . .
                . . 7 . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . . . 7 7 7 7 7 7 7 . 7 . . .
                . . . . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 7 7 7 7 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . . . . .
                . . . . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                . . 7 . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player3.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.RELEASED,
    on_player3_button_right_released)

def on_player4_button_down_pressed():
    animation.run_image_animation(mySprite4,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . . 5 5 5 5 5 5 5 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . 5 5 5 5 5 5 5 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                """)],
        500,
        True)
controller.player4.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player4_button_down_pressed)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . 4 4 4 . . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . . 4 4 4 . . . . . .
                . . . . . . 4 4 4 9 . . . . . .
                . . . . . 4 . 4 4 4 . . . . . .
                . . . . . . . 4 4 4 . . . . . .
                . . . . . . . 4 . . 4 . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . 4 4 4 . . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . . 4 4 4 . . . . . .
                . . . . . . 4 4 4 9 . . . . . .
                . . . . . . . 4 4 4 . . . . . .
                . . . . . . . 4 4 4 . . . . . .
                . . . . . . 4 . . 4 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_player2_button_left_released():
    animation.run_image_animation(mySprite2,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 3 . . 3 3 3 3 3 . . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . 3 . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 3 3 3 3 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 3 . 3 3 3 3 3 . . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . 3 . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 3 3 3 3 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player2.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.RELEASED,
    on_player2_button_left_released)

def on_player2_button_down_released():
    animation.run_image_animation(mySprite2,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 3 . . 3 3 3 3 3 . . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . 3 . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 3 3 3 3 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 3 . 3 3 3 3 3 . . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . 3 . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 3 3 3 3 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player2.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.RELEASED,
    on_player2_button_down_released)

def on_player3_connected():
    global mySprite3
    mySprite3 = sprites.create(img("""
            . . . . . . f f f f f . . . . .
            . . . . . . f f f f f . . . . .
            . . . . . . f f f f f . . . . .
            . . . . . . 7 7 7 7 7 . . . . .
            . . . . . f f f f f f f . . . .
            . . . . . . 7 7 7 7 7 . . . . .
            . . . . . 7 7 7 7 7 7 7 . . . .
            . . . . . 7 9 9 f 9 9 7 . . . .
            . . . . 7 7 9 9 f 9 9 7 7 . . .
            . . . 7 . 7 7 7 7 7 7 7 . 7 . .
            . . . 7 . 7 7 f f f 7 7 . 7 . .
            . . . . . . 7 7 7 7 7 . . . . .
            . . . . . . 7 . . . 7 . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.player)
    controller.player3.move_sprite(mySprite3)
controller.player3.on_event(ControllerEvent.CONNECTED, on_player3_connected)

def on_player2_button_up_released():
    animation.run_image_animation(mySprite2,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 3 . . 3 3 3 3 3 . . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . 3 . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 3 3 3 3 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 3 . 3 3 3 3 3 . . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . 3 . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 3 3 3 3 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.RELEASED,
    on_player2_button_up_released)

def on_player3_button_right_pressed():
    animation.run_image_animation(mySprite3,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . 7 7 7 . . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . . 7 7 7 . . . . . . .
                . . . . . . 9 7 7 7 . . . . . .
                . . . . . . 7 7 7 . 7 . . . . .
                . . . . . . 7 7 7 . . . . . . .
                . . . . . 7 . . 7 . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . 7 7 7 . . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . . 7 7 7 . . . . . . .
                . . . . . . 9 7 7 7 . . . . . .
                . . . . . . 7 7 7 . . . . . . .
                . . . . . . 7 7 7 . . . . . . .
                . . . . . . 7 . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player3.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player3_button_right_pressed)

def on_player2_button_up_pressed():
    animation.run_image_animation(mySprite2,
        [img("""
                . . . . . . f f f f f . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . 3 3 3 3 3 . . . . .
                . . . . . f f f f f f f . . . .
                . . . . . . 3 3 3 3 3 . . . . .
                . . . 3 . 3 3 3 3 3 3 3 . . . .
                . . . 3 . 3 3 3 3 3 3 3 . . . .
                . . . . 3 3 3 3 3 3 3 3 3 . . .
                . . . . . 3 3 3 3 3 3 3 . 3 . .
                . . . . . 3 3 3 3 3 3 3 . 3 . .
                . . . . . . 3 3 3 3 3 . . . . .
                . . . . . . 3 . . . 3 . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . f f f f f . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . 3 3 3 3 3 . . . . .
                . . . . . f f f f f f f . . . .
                . . . . . . 3 3 3 3 3 . . . . .
                . . . . . 3 3 3 3 3 3 3 . 3 . .
                . . . . . 3 3 3 3 3 3 3 . 3 . .
                . . . . 3 3 3 3 3 3 3 3 3 . . .
                . . . 3 . 3 3 3 3 3 3 3 . . . .
                . . . 3 . 3 3 3 3 3 3 3 . . . .
                . . . . . . 3 3 3 3 3 . . . . .
                . . . . . . 3 . . . 3 . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player2_button_up_pressed)

def on_player3_button_b_released():
    animation.run_image_animation(mySprite2,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 7 7 7 7 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . . . . .
                . . . . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                . . 7 . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 7 7 7 7 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . . . . .
                . . . . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                . . 7 . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 7 7 7 7 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 7 . . 7 7 7 7 7 . . . . . .
                . . 7 . 7 7 7 7 7 7 7 . . . . .
                . . 7 . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . . . 7 7 7 7 7 7 7 . 7 . . .
                . . . . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 7 7 7 7 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 7 . 7 7 7 7 7 . . . . . .
                . . 7 . 7 7 7 7 7 7 7 . . . . .
                . . 7 . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . . . 7 7 7 7 7 7 7 . 7 . . .
                . . . . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 7 7 7 7 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . . . . .
                . . . . 7 9 9 f 9 9 7 . . . . .
                . . . 7 7 9 9 f 9 9 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . 7 . . .
                . . 7 . 7 7 f f f 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player3.on_button_event(ControllerButton.B,
    ControllerButtonEvent.RELEASED,
    on_player3_button_b_released)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . 4 4 4 . . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . . 4 4 4 . . . . . . .
                . . . . . . 9 4 4 4 . . . . . .
                . . . . . . 4 4 4 . 4 . . . . .
                . . . . . . 4 4 4 . . . . . . .
                . . . . . 4 . . 4 . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . 4 4 4 . . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . . 4 4 4 . . . . . . .
                . . . . . . 9 4 4 4 . . . . . .
                . . . . . . 4 4 4 . . . . . . .
                . . . . . . 4 4 4 . . . . . . .
                . . . . . . 4 . . 4 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_player2_button_right_pressed():
    animation.run_image_animation(mySprite2,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . 3 3 3 . . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . . 3 3 3 . . . . . . .
                . . . . . . 9 3 3 3 . . . . . .
                . . . . . . 3 3 3 . 3 . . . . .
                . . . . . . 3 3 3 . . . . . . .
                . . . . . 3 . . 3 . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . 3 3 3 . . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . . 3 3 3 . . . . . . .
                . . . . . . 9 3 3 3 . . . . . .
                . . . . . . 3 3 3 . . . . . . .
                . . . . . . 3 3 3 . . . . . . .
                . . . . . . 3 . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player2.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_right_pressed)

def on_player3_button_left_released():
    animation.run_image_animation(mySprite4,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 5 . . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 5 5 5 5 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 5 . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 5 5 5 5 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player3.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.RELEASED,
    on_player3_button_left_released)

def on_player4_button_right_released():
    animation.run_image_animation(mySprite4,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 5 5 5 5 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 5 . . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 5 5 5 5 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 5 . 5 5 5 5 5 . . . . . .
                . . 5 . 5 5 5 5 5 5 5 . . . . .
                . . 5 . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . . . 5 5 5 5 5 5 5 . 5 . . .
                . . . . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 5 5 5 5 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . 5 5 5 5 5 5 5 . . . . .
                . . . . 5 9 9 f 9 9 5 . . . . .
                . . . 5 5 9 9 f 9 9 5 5 . . . .
                . . 5 . 5 5 5 5 5 5 5 . 5 . . .
                . . 5 . 5 5 f f f 5 5 . 5 . . .
                . . . . . 5 5 5 5 5 . . . . . .
                . . . . . 5 . . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player4.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.RELEASED,
    on_player4_button_right_released)

def on_down_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . 4 . . . 4 . . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . 4 . 4 4 4 4 4 4 4 . . . . .
                . . 4 . 4 4 4 4 4 4 4 . . . . .
                . . . 4 4 4 4 4 4 4 4 4 . . . .
                . . . . 4 4 4 4 4 4 4 . 4 . . .
                . . . . 4 4 4 4 4 4 4 . 4 . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . 4 . . . 4 . . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . 4 4 4 4 4 4 4 . 4 . . .
                . . . . 4 4 4 4 4 4 4 . 4 . . .
                . . . 4 4 4 4 4 4 4 4 4 . . . .
                . . 4 . 4 4 4 4 4 4 4 . . . . .
                . . 4 . 4 4 4 4 4 4 4 . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 4 4 4 4 4 . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                """)],
        500,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_player2_button_b_released():
    animation.run_image_animation(mySprite2,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 3 . . 3 3 3 3 3 . . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . 3 . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 3 3 3 3 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 3 . 3 3 3 3 3 . . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . 3 . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 3 3 3 3 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.RELEASED,
    on_player2_button_b_released)

def on_player4_button_a_pressed():
    global rspons
    rspons = game.ask_for_string("type what you want to say to your friends", 24)
    mySprite2.say_text(rspons, 1000, False)
controller.player4.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player4_button_a_pressed)

def on_player2_button_left_pressed():
    animation.run_image_animation(mySprite2,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . 3 3 3 . . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . . 3 3 3 . . . . . .
                . . . . . . 3 3 3 9 . . . . . .
                . . . . . 3 . 3 3 3 . . . . . .
                . . . . . . . 3 3 3 . . . . . .
                . . . . . . . 3 . . 3 . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . 3 3 3 . . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . . 3 3 3 . . . . . .
                . . . . . . 3 3 3 9 . . . . . .
                . . . . . . . 3 3 3 . . . . . .
                . . . . . . . 3 3 3 . . . . . .
                . . . . . . 3 . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player2.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_left_pressed)

def on_player3_button_down_pressed():
    animation.run_image_animation(mySprite3,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . 7 . 7 7 7 7 7 7 7 . . . . .
                . . 7 . 7 7 7 7 7 7 7 . . . . .
                . . . 7 7 7 7 7 7 7 7 7 . . . .
                . . . . 7 7 7 7 7 7 7 . 7 . . .
                . . . . 7 7 7 7 7 7 7 . 7 . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . 7 . . . 7 . . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . 7 7 7 7 7 7 7 . 7 . . .
                . . . . 7 7 7 7 7 7 7 . 7 . . .
                . . . 7 7 7 7 7 7 7 7 7 . . . .
                . . 7 . 7 7 7 7 7 7 7 . . . . .
                . . 7 . 7 7 7 7 7 7 7 . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 7 7 7 7 7 . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . f f f f f . . . . . .
                """)],
        500,
        True)
controller.player3.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player3_button_down_pressed)

def on_player4_button_left_pressed():
    animation.run_image_animation(mySprite4,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . 5 5 5 . . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . . 5 5 5 . . . . . .
                . . . . . . 5 5 5 9 . . . . . .
                . . . . . 5 . 5 5 5 . . . . . .
                . . . . . . . 5 5 5 . . . . . .
                . . . . . . . 5 . . 5 . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . 5 5 5 . . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . . 5 5 5 . . . . . .
                . . . . . . 5 5 5 9 . . . . . .
                . . . . . . . 5 5 5 . . . . . .
                . . . . . . . 5 5 5 . . . . . .
                . . . . . . 5 . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player4.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player4_button_left_pressed)

def on_player3_button_a_pressed():
    global rspons
    rspons = game.ask_for_string("type what you want to say to your friends", 24)
    mySprite2.say_text(rspons, 1000, False)
controller.player3.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player3_button_a_pressed)

def on_player2_button_right_released():
    animation.run_image_animation(mySprite2,
        [img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . f f f f . . . . . . . .
                . . . . f f f f . . . . . . . .
                . . . . 3 3 3 3 . . . . . . . .
                . . . f f f f f f . . . . . . .
                . . 3 . . 3 3 3 3 3 . . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . 3 . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 3 3 3 3 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . 3 . 3 3 3 3 3 . . . . . .
                . . 3 . 3 3 3 3 3 3 3 . . . . .
                . . 3 . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . . . 3 3 3 3 3 3 3 . 3 . . .
                . . . . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . 3 3 3 3 . . . . . . .
                . . . . f f f f f f f . . . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . 3 3 3 3 3 3 3 . . . . .
                . . . . 3 9 9 f 9 9 3 . . . . .
                . . . 3 3 9 9 f 9 9 3 3 . . . .
                . . 3 . 3 3 3 3 3 3 3 . 3 . . .
                . . 3 . 3 3 f f f 3 3 . 3 . . .
                . . . . . 3 3 3 3 3 . . . . . .
                . . . . . 3 . . . 3 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player2.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.RELEASED,
    on_player2_button_right_released)

def on_player2_connected():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . . . . . f f f f f . . . . .
            . . . . . . f f f f f . . . . .
            . . . . . . f f f f f . . . . .
            . . . . . . 3 3 3 3 3 . . . . .
            . . . . . f f f f f f f . . . .
            . . . . . . 3 3 3 3 3 . . . . .
            . . . . . 3 3 3 3 3 3 3 . . . .
            . . . . . 3 9 9 f 9 9 3 . . . .
            . . . . 3 3 9 9 f 9 9 3 3 . . .
            . . . 3 . 3 3 3 3 3 3 3 . 3 . .
            . . . 3 . 3 3 f f f 3 3 . 3 . .
            . . . . . . 3 3 3 3 3 . . . . .
            . . . . . . 3 . . . 3 . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.player)
    controller.player2.move_sprite(mySprite2)
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

def on_player4_button_right_pressed():
    animation.run_image_animation(mySprite4,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . 5 5 5 . . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . . 5 5 5 . . . . . . .
                . . . . . . 9 5 5 5 . . . . . .
                . . . . . . 5 5 5 . 5 . . . . .
                . . . . . . 5 5 5 . . . . . . .
                . . . . . 5 . . 5 . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . f f f . . . . . . .
                . . . . . . 5 5 5 . . . . . . .
                . . . . . f f f f f . . . . . .
                . . . . . . 5 5 5 . . . . . . .
                . . . . . . 9 5 5 5 . . . . . .
                . . . . . . 5 5 5 . . . . . . .
                . . . . . . 5 5 5 . . . . . . .
                . . . . . . 5 . . 5 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player4.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player4_button_right_pressed)

def on_player3_button_left_pressed():
    animation.run_image_animation(mySprite3,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . 7 7 7 . . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . . 7 7 7 . . . . . .
                . . . . . . 7 7 7 9 . . . . . .
                . . . . . 7 . 7 7 7 . . . . . .
                . . . . . . . 7 7 7 . . . . . .
                . . . . . . . 7 . . 7 . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . 7 7 7 . . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . . 7 7 7 . . . . . .
                . . . . . . 7 7 7 9 . . . . . .
                . . . . . . . 7 7 7 . . . . . .
                . . . . . . . 7 7 7 . . . . . .
                . . . . . . 7 . . 7 . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player3.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player3_button_left_pressed)

def on_player3_button_up_pressed():
    animation.run_image_animation(mySprite3,
        [img("""
                . . . . . . f f f f f . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . 7 7 7 7 7 . . . . .
                . . . . . f f f f f f f . . . .
                . . . . . . 7 7 7 7 7 . . . . .
                . . . 7 . 7 7 7 7 7 7 7 . . . .
                . . . 7 . 7 7 7 7 7 7 7 . . . .
                . . . . 7 7 7 7 7 7 7 7 7 . . .
                . . . . . 7 7 7 7 7 7 7 . 7 . .
                . . . . . 7 7 7 7 7 7 7 . 7 . .
                . . . . . . 7 7 7 7 7 . . . . .
                . . . . . . 7 . . . 7 . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . f f f f f . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . f f f f f . . . . .
                . . . . . . 7 7 7 7 7 . . . . .
                . . . . . f f f f f f f . . . .
                . . . . . . 7 7 7 7 7 . . . . .
                . . . . . 7 7 7 7 7 7 7 . 7 . .
                . . . . . 7 7 7 7 7 7 7 . 7 . .
                . . . . 7 7 7 7 7 7 7 7 7 . . .
                . . . 7 . 7 7 7 7 7 7 7 . . . .
                . . . 7 . 7 7 7 7 7 7 7 . . . .
                . . . . . . 7 7 7 7 7 . . . . .
                . . . . . . 7 . . . 7 . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        500,
        True)
controller.player3.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player3_button_up_pressed)

rspons = ""
mySprite2: Sprite = None
mySprite3: Sprite = None
mySprite4: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . f f f f f . . . . .
        . . . . . . f f f f f . . . . .
        . . . . . . f f f f f . . . . .
        . . . . . . 4 4 4 4 4 . . . . .
        . . . . . f f f f f f f . . . .
        . . . . . . 4 4 4 4 4 . . . . .
        . . . . . 4 4 4 4 4 4 4 . . . .
        . . . . . 4 9 9 f 9 9 4 . . . .
        . . . . 4 4 9 9 f 9 9 4 4 . . .
        . . . 4 . 4 4 4 4 4 4 4 . 4 . .
        . . . 4 . 4 4 f f f 4 4 . 4 . .
        . . . . . . 4 4 4 4 4 . . . . .
        . . . . . . 4 . . . 4 . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.player)
controller.move_sprite(mySprite)
scene.set_background_image(assets.image("""
    tophattopya
    """))
music.play(music.create_song(hex("""
        0064000408070200001c00010a006400f40164000004000000000000000000000000000500000406007c008000012405001c000f0a006400f4010a0000040000000000000000000000000000000002c20000000400012c0400080001270c001000012510001400012918001c00012420002400012728002c00012430003400012738003c0001293c004000012544004800012748004c00012450005400012758005c0001275c006000012760006400012764006800012768006c0001276c007000012770007400012774007800012778007c0001247c008000012480008400012788008c00012a90009400031d202498009c0001249c00a0000127a000a4000127a400a8000127a800ac000127ac00b0000127
        """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)