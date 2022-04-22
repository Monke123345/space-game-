def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        50,
        50)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

poopoo: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
effects.star_field.start_screen_effect()
mySprite = sprites.create(img("""
        . . . . . . . 3 3 . . . . . . . 
            . . . . . . 3 3 3 3 . . . . . . 
            . . . . . 3 3 3 3 3 3 . . . . . 
            . . . . 3 3 3 3 3 3 3 3 . . . . 
            . . . 3 3 3 3 3 3 3 3 3 3 . . . 
            . . . 3 3 3 3 3 3 3 3 3 3 . . . 
            . . . 3 f f f 3 f f f 3 3 . . . 
            . . . 3 f f f 3 f f f 3 3 . . . 
            . . . 3 f 3 3 3 f 3 3 3 3 . . . 
            . . . 3 f 3 3 3 f 3 3 3 3 . . . 
            . . . 3 3 3 3 3 3 3 3 3 3 . . . 
            . . . 3 3 3 3 3 3 3 3 3 3 . . . 
            . . . 3 3 3 3 3 3 3 3 3 3 . . . 
            . . . 3 3 3 3 3 3 3 3 3 3 . . . 
            . . . 3 3 3 3 3 3 3 3 3 3 . . . 
            . . . 3 3 3 3 3 3 3 3 3 3 . . .
    """),
    SpriteKind.player)
mySprite.set_position(77, 111)
controller.move_sprite(mySprite, 100, 0)
mySprite.set_stay_in_screen(True)

def on_update_interval():
    global poopoo
    poopoo = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . e . . . . . . 
                    . . . . . . . f e e . . . . . . 
                    . . . . . . e e f f f . . . . . 
                    . . . . . e e e e e e . . . . . 
                    . . . . . f f f e e e f . . . . 
                    . . . . e e e f f f f f . . . . 
                    . . . e e e e e e e e e e . . . 
                    . . e f f f f e e e e e e e . . 
                    . . e e e e f f f f f f f f . . 
                    . . f f e e e e e e e e e e . . 
                    . . . e f f f e e e e e e e . .
        """),
        0,
        50)
    poopoo.x = randint(0, scene.screen_width())
    poopoo.set_kind(SpriteKind.enemy)
game.on_update_interval(1000, on_update_interval)
