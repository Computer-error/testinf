from pyscript import document

def reveal(event):
    un = (document.getElementById("me"))
    pw = (document.getElementById("pw"))
    char_countun = len(un)
    digit_countpw = round(sum(char.isdigit() for char in pw))
    alpha_countpw = round(sum(char.isalpha() for char in pw))
    countpw = len(pw)
    result = "none"

    if countpw >=10 and char_countun >=7:
        if alpha_countpw >=1 and digit_countpw >=1:
            result = "✅ Your username and password are valid, account successfully created."
        else:
            result = "❌ Your password must contain at least one letter or one digit."
    else:
        result = "❌Please make sure your username is at least 7 characters long and your password is at least 10 characters long."

    document.getElementById("veri").innerText = result