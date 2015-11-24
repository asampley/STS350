label i_cockpit:
    scene bg cockPitImage
    with fade
    stop music
    play sound "click.ogg"

    python:
        room = Game.rooms[Game.ROOM_COCKPIT]
        
        Game.inputNVL("Here we are in the [room.name]! What do you want to do?")
        Game.checkQuit()
        Game.narrateNVL("I don't know what \"[Game.input]\" means.")
        Game.jump(room.label)