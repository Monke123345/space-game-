controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . 3 . . . . . . . . . . 
        . . . . 3 3 3 3 3 . . . . . . . 
        . . . . 3 . . . 3 3 . . . . . . 
        . . . 3 . . 3 3 . 3 . . . . . . 
        . . . 3 . . . 3 . 3 . . . . . . 
        . . . 3 . . . 3 . 3 . . . . . . 
        . . . . 3 . . 3 . 3 . . . . . . 
        . . . . 3 . 3 3 . 3 . . . . . . 
        . . . . 3 3 . . . 3 . . . . . . 
        . . . . 3 3 3 3 3 3 . . . . . . 
        `, mySprite, 0, -50)
    music.pewPew.play()
})
let poopoo: Sprite = null
let projectile: Sprite = null
let mySprite: Sprite = null
effects.starField.startScreenEffect()
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.setPosition(77, 111)
controller.moveSprite(mySprite, 100, 0)
mySprite.setStayInScreen(true)
game.onUpdateInterval(1000, function () {
    poopoo = sprites.createProjectileFromSide(img`
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
        `, 0, 50)
    poopoo.x = randint(0, scene.screenWidth())
    poopoo.setKind(SpriteKind.Enemy)
})
