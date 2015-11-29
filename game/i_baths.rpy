init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_BATHS]
    Game.cluesFound[Game.BATHS_WOUND] = False
    Game.state["baths_body_turned"] = False
    Game.state[Game.STATE_TIME_OF_DEATH] = False
    
    def look():
        Game.inputADV( "The body of Henry Augustus Algernon Royaume is in a pool of blood from the wound on his head. He is still in his evening wear, lying face down. " )
    def turn():
        Game.state["baths_body_turned"] = True
        Game.inputADV( "You flip over the body. It looks like there is something in his pocket." )
    body = Clue( "body", [ "look", "turn" ], [ look, turn ] )
    
    def look():
        Game.cluesFound[Game.BATHS_WOUND] = True
        Game.inputADV( "The wound appears to be caused by a heavy metal object." )
    wound = Clue( "wound" , [ "look" ], [ look ])
    
    def look():
        if Game.state["baths_body_turned"]:
            Game.inputADV( "There is something small and round in his pocket, and possibly some glass shards" )
    def open():
        if Game.state["baths_body_turned"]:
            Game.state[Game.STATE_TIME_OF_DEATH] = True
            Game.inputADV( "Inside his pocket is a silver pocket watch. It must have broken when he fell. The face reads 8:42" )
    pocket = Clue( "pocket", [ "look", "open" ], [ look, open ] )
    
    room.addClue(body)
    room.addClue(wound)
    room.addClue(pocket)
    
    def look():
        Game.inputADV( "There's the body" )
    room.addCommand( "look", look )
    
    # clean namespace
    del look
    del body

label i_baths:
    scene bg bathImage
    with fade
    stop music fadeout 2

    python:
        room = Game.rooms[Game.ROOM_BATHS]
        Game.inputADV("Here we are in the [room.name]! What do you want to do?")
        Game.jump(room.label + "_in")
        
label i_baths_in:        
    python:
        # assumption: if all functions of clues are inputADV, then we can loop through this
        Game.checkQuit()
        
        if Game.input == "":
            Game.inputADV( Game.prevPrompt )
        else:
            try:
                room.do(Game.input)
            except:
                Game.narrateADV("I don't know what \"[Game.input]\" means.")
                Game.inputADV( Game.prevPrompt )
        
        Game.jump(room.label + "_in")
