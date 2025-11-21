namespace SpriteKind {
    export const NPC = SpriteKind.create()
}
controller.player4.onButtonEvent(ControllerButton.Up, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite4,
    assets.animation`borv4j`,
    100,
    true
    )
})
controller.player4.onButtonEvent(ControllerButton.Up, ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    mySprite4,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player4.onEvent(ControllerEvent.Connected, function () {
    mySprite4 = sprites.create(img`
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
        `, SpriteKind.Player)
    controller.player4.moveSprite(mySprite4)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `],
    100,
    true
    )
})
controller.player4.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    mySprite4,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player3.onButtonEvent(ControllerButton.Up, ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    mySprite3,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player3.onButtonEvent(ControllerButton.Down, ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    mySprite3,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player4.onButtonEvent(ControllerButton.Down, ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    mySprite4,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    rspons = game.askForString("talk to your buds. say party for a party", 24)
    mySprite.sayText(rspons, 1000, false)
    if (rspons == "party") {
        scene.setBackgroundImage(img`
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
            `)
        music.stopAllSounds()
        pause(100)
        music.play(music.createSong(assets.song`cool DJ lomen`), music.PlaybackMode.LoopingInBackground)
        mySprite5 = sprites.create(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . f f f f f . . . . . . 
            . . . . f e e e e e f . . . . . 
            . . . . f 9 5 5 5 9 f . . . . . 
            . . . . f 5 5 5 5 5 . . . . . . 
            . . . . . 5 5 f 5 5 . . . . . . 
            . . . 7 7 4 4 4 4 4 7 7 . . . . 
            . . . 5 5 4 4 4 4 4 5 5 . . . . 
            . . . 5 5 4 4 4 4 4 5 5 . . . . 
            . . . 5 5 4 4 4 4 4 5 5 . . . . 
            8 8 8 8 f 8 8 f 8 8 8 8 8 8 8 8 
            8 8 8 f 8 f 8 f 8 8 8 8 8 8 8 8 
            8 8 8 f 8 f 8 f 8 8 8 8 8 8 8 8 
            8 8 8 f f 8 8 8 f f 8 8 8 8 8 8 
            `, SpriteKind.NPC)
    }
})
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    rspons = game.askForString("type what you want to say to your friends", 24)
    mySprite2.sayText(rspons, 1000, false)
})
controller.player2.onButtonEvent(ControllerButton.Down, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite2,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.anyButton.onEvent(ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player3.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    mySprite3,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player4.onButtonEvent(ControllerButton.Down, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite4,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player2.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    mySprite2,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player2.onButtonEvent(ControllerButton.Down, ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    mySprite2,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player3.onEvent(ControllerEvent.Connected, function () {
    mySprite3 = sprites.create(img`
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
        `, SpriteKind.Player)
    controller.player3.moveSprite(mySprite3)
})
controller.player2.onButtonEvent(ControllerButton.Up, ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    mySprite2,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player3.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite3,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player2.onButtonEvent(ControllerButton.Up, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite2,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player3.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Released, function () {
    for (let index = 0; index < 1; index++) {
        animation.runImageAnimation(
        mySprite3,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        500,
        true
        )
    }
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player2.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite2,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player4.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    mySprite4,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player2.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Released, function () {
    for (let index = 0; index < 1; index++) {
        animation.runImageAnimation(
        mySprite2,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        500,
        true
        )
    }
})
controller.player4.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    rspons = game.askForString("type what you want to say to your friends", 24)
    mySprite2.sayText(rspons, 1000, false)
})
controller.player2.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite2,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player3.onButtonEvent(ControllerButton.Down, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite3,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.B.onEvent(ControllerButtonEvent.Released, function () {
    for (let index = 0; index < 1; index++) {
        animation.runImageAnimation(
        mySprite,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        500,
        true
        )
    }
})
controller.player4.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite4,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player3.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    rspons = game.askForString("type what you want to say to your friends", 24)
    mySprite2.sayText(rspons, 1000, false)
})
controller.player2.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    mySprite2,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player2.onEvent(ControllerEvent.Connected, function () {
    mySprite2 = sprites.create(img`
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
        `, SpriteKind.Player)
    controller.player2.moveSprite(mySprite2)
})
controller.player4.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite4,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player3.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite3,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player3.onButtonEvent(ControllerButton.Up, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite3,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.player4.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Repeated, function () {
    for (let index = 0; index < 1; index++) {
        animation.runImageAnimation(
        mySprite4,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        500,
        false
        )
    }
})
let mySprite2: Sprite = null
let mySprite5: Sprite = null
let rspons = ""
let mySprite3: Sprite = null
let mySprite4: Sprite = null
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
scene.setBackgroundImage(assets.image`tophattopya`)
music.play(music.createSong(hex`0064000408070200001c00010a006400f40164000004000000000000000000000000000500000406007c008000012405001c000f0a006400f4010a0000040000000000000000000000000000000002c20000000400012c0400080001270c001000012510001400012918001c00012420002400012728002c00012430003400012738003c0001293c004000012544004800012748004c00012450005400012758005c0001275c006000012760006400012764006800012768006c0001276c007000012770007400012774007800012778007c0001247c008000012480008400012788008c00012a90009400031d202498009c0001249c00a0000127a000a4000127a400a8000127a800ac000127ac00b0000127`), music.PlaybackMode.LoopingInBackground)
