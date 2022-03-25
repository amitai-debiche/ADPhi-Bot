def song_return(number):
    switcher = {
        1: '```Would you know the lights that fairest \nDeck the azure sky \nThere\'s the star and silvry crescent \nOf our ADPhi \nWindow lights in heaven\'s bright mansion \nGleaming throught the night \nTheir soft rays oer Alpha Delta \nShed a golden light \nBeam oer us, Star and Crecent\nGuide us till we die\nEach a brother loving truly, Alpha Delta Phi```',
        2: "two",
    }

    return switcher.get(number, "```SONG NOT FOUND```")

def title_return(number):
    switcher = {
        1: 'Would You Know',
        2: "two",
    }
    return switcher.get(number, "```SONG NOT FOUND```")

def mp3_return(number):
    switcher = {
        1: "no idea how to do this yet",
        2: "two",
    }
    return switcher.get(number, "```SONG NOT FOUND```")
