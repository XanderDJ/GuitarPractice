import random


def get_finger_warmup():
    fingers = [1, 2, 3, 4]
    frets = [i for i in range(13)]
    starting_fret = random.choice(frets[:4])
    ending_frets = random.choice(frets[8:])
    schedule = "Use finger sequence: "
    random.shuffle(fingers)
    for finger in fingers:
        schedule += str(finger)
    schedule += "\nfrom fret " + str(starting_fret) + " to fret " + str(ending_frets)
    return schedule


