from pyscript import document

def ply(event):
    team=(document.getElementById("me").value)
    pno=0
    tname=""

    if team == 1:
        pno = 0
        tname == "red"
        while pno <= 101:
            pno + 1
            document.getElementById("nuhuh").innerHTML += "Player "+str(pno)+"<br>"
    elif team == 2:
        pno = 100
        tname == "orange"
        while pno <= 201:
            pno + 1
            document.getElementById("nuhuh").innerHTML += "Player "+str(pno)+"<br>"
    elif team == 3:
        pno = 200
        tname == "yellow"
        while pno <= 301:
            pno + 1
            document.getElementById("nuhuh").innerHTML += "Player "+str(pno)+"<br>"
    elif team == 4:
        pno = 300
        tname == "green"
        while pno <= 401:
            pno + 1
            document.getElementById("nuhuh").innerHTML += "Player "+str(pno)+"<br>"
    elif team == 5:
        pno = 400
        tname == "blue"
        while pno <= 501:
            pno + 1
            document.getElementById("nuhuh").innerHTML += "Player "+str(pno)+"<br>"
    elif team == 6:
        pno = 500 
        tname == "purple"
        while pno <= 601:
            pno += 1
            document.getElementById("nuhuh").innerHTML += "Player "+str(pno)+"<br>"
    else:
        document.getElementById("nuhuh").innerText = "Please put an valid id number"


    document.getElementById("eep").innerText = f"List of {tname} team players:"