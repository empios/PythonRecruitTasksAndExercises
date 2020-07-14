Student_Dic = {
"Marian": "Polska",
"Brunhilda": "Niemcy",
"Jose": "Meksyk",
"Natasza": "Rosja",
}


def student(imie):
    searchedOutput = Student_Dic.get(imie)
    if (searchedOutput is not None):
        print("Cześć, jestem " + imie + "." + " " + "Mój kraj to: "+Student_Dic[imie])
    else:
        print("Cześć! Co ja tutaj robie?!")


