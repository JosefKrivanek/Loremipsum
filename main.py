import random

slova = ["skakal","pes","přes","oves","zelenou","louku","šel","za","ním","myslivec","péro","na","klobouku",]


pocet_odstavcu = int(input("Zadejte požadovaný počet odstavců: "))
for i in range(pocet_odstavcu):
    for i in range(random.randint(5,10)):
        veta = ""
        for i in range(random.randint(8,30)):
            nahodne_slovo = random.choice(slova)
            veta += nahodne_slovo + " "
        VETA = veta.capitalize()
        print(VETA + ".")
    print("\n")



#def generuj_lorem_ipsum(slova=50):
#    lorem_ipsum_text = ""
#    for _ in range(delka):
#        nahodna_veta = random.choice(slova)
#        lorem_ipsum_text += nahodna_veta + " "
#    return lorem_ipsum_text

#lorem_ipsum = generuj_lorem_ipsum()
#print(lorem_ipsum)


#def text (dleka):
#    for i in range(random.randint(5, 15)):
#        nahodne_slovo = random.choice(slova)
#        veta += nahodne_slovo + " "
#    return text
#lorem_ipsum = text()
#print(lorem_ipsum)

#Maaaaan fuck this shiiii Imma bout to get a f anyyway