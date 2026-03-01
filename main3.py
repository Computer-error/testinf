from pyscript import document

import random

def generate_random_integer(start, end):
    try:
        return random.randint(start, end)
    except ValueError:
        print("systemerror")
        return None

def allow(event):
    med = (document.getElementById("me"))
    reg = (document.getElementById("pw"))
    gr = (document.getElementById("gr"))
    sc = (document.getElementById("sc"))
    rand_int = 0
    result = ""
    team = ""

    if reg == 1:
        if med == 1:
            result = "✅ Your username and password are valid, account successfully created."
            if sum(char.isdigit() for char in gr)+sum(char.isalpha() for char in gr) == 1 and sum(char.isalpha() for char in sc)  == 1:
                result = "✅ You have successfully registered for the intramurals, see you there!"
                rand_int = generate_random_integer(1, 7)
                if rand_int == 1:
                    team += " You have been selected for the red team!"
                elif rand_int == 2:
                    team += " You have been selected for the blue team!"
                elif rand_int == 3:
                    team += " You have been selected for the green team!"
                elif rand_int == 4:
                    team += " You have been selected for the yellow team!"
                elif rand_int == 5:
                    team += " You have been selected for the orange team!"
                else:
                    team += " You have been selected for the purple team!"
            else:
                result = "❌ Please make sure you have entered your grade and section."
        else:
            result = "❌ Please make sure your you have submitted a medical certificate."
    else:
        result = "❌ Please make sure your you have registered before doing this."

    document.getElementById("ver").innerHTML = f"{result}<br>{team}"