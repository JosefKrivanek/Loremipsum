import random

slova = ["kokot","kříž"]
slabiky = []

def generuj_lorem_ipsum(pocet_vet=5):
    lorem_ipsum_text = "."
    for _ in range(pocet_vet):
        nahodne_slovo = random.choice(slova)
        lorem_ipsum_text += nahodne_slovo + " "

    return lorem_ipsum_text.strip()


lorem_ipsum = generuj_lorem_ipsum()
print(lorem_ipsum)


#Maaaaan fuck this shiiii Imma bout to get a f anyyway