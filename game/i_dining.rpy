init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_DINING]
    Game.cluesFound[Game.DINING_SPECTACLES] = False
    
    def look():
        Game.narrateADV("The dining tables are covered with immaculate white tablecloths where the passengers are served in some of the most expensive crockery. The floor is installed with soft and beautifully textured carpet.")
        Game.narrateADV("Though the tables have been cleaned since supper, left near the edge of the table are a pair of small {b}spectacles{/b}")
    room.addCommand("look", look)
    
    def look():
        Game.narrateADV( "If you recall correctly, which you always do, Rector Esgob sat in this spot, wearing these same {b}spectacles{/b}" )
        Game.cluesFound[Game.DINING_SPECTACLES] = True
    spectacles = Clue( "spectacles", [ "look" ], [ look ] )
    glasses = Clue( "glasses", [ "look" ], [ look ] )
    
    room.addClue(spectacles)
    room.addClue(glasses)

label i_dining:
    scene bg diningImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_DINING]
        
        # Opening description of the room
        Game.narrateADV("The dining hall is a massive room with big windows on the side providing a very beautiful view of the countryside - or they would, if it weren't the middle of the night.")
        Game.narrateADV("The dining tables are covered with pure white tablecloths, and the table is immaculately laid for the next meal. The floor is installed with soft and beautifully textured carpet.")
        Game.jump(room.label + "_in")
        
label i_dining_in:        
    python:
        # assumption: if all functions of clues are narrateADV, then we can loop through this
        Game.prevNarrate = "What do you want to do?"
        Game.inputADV( Game.prevNarrate )
        Game.checkQuit(room.label + "_in")
        
        try:
            room.do(Game.input)
        except:
            Game.narrateADV("I don't know what \"[Game.input]\" means.")
        
        Game.jump(room.label + "_in")
