import random

slova = [
        "potok","pes","přes","oves","zelenou","louku","šel","za","ním","myslivec","péro","na","klobouku","pejsku","100","256","4",
        "náš","co","děláš",",že","si","tak","vesel","stále","řek","bych","vám","nevím","sám","hop","a","skákal","dále","9","420",
        "ale","avšak","a","leč","nýbrž","naopak","jenomže","i","ve","ku","do","za","1","10","50","zaplakala","vysoký","jalovec","já",
        "prší","jen","se","leje","kam","koníčci","pojedeme","na","luka","až","kukačka","zakuká","už","má","panenka","přeskoč","ho","nic",
        "milá","rovnýma","nohama","nepřeskočím","ráda","točím","tebe","šhohajku","zapomenout","musím","jede","poštovský","panáček",
        "jede","vrané","koníčky","tomu","být","obyvytel","bytlit","býk","lyže","lýko","zpytovat","pelyněk","pryž","hlemýžď","kobyla",
        "běžela","ovečka","nahoru","kopečka","ní","beránek","žalovat","zámek","dělat","tom","našem","galánku","uvěje","věneček","rozmarýn",
        "halí","belí","koně","zelí","kůzlátka","petrželi","táto","mámo","komoře","je","myš","pustíme","tam","kocoura","on","tu","vyšťourá",
        "\b\b,","\b\b,","\b\b,","\b\b,","\b\b,","\b\b,","\b\b,","\b\b,","\b\b,",
        ]
       
pocet_odstavcu = int(input("Zadejte požadovaný počet odstavců: "))

#with open("loremupsum.txt", "a", encoding="utf-8") as soubor:

for i in range(pocet_odstavcu):                     #odstavit
    for i in range(random.randint(5,10)):           #odstavit
        veta = ""                                   #odstavit
        for i in range(random.randint(8,40)):       #odstavit
            nahodne_slovo = random.choice(slova)    # odstavit
            veta += nahodne_slovo + " "             # odstavit
        VETA = veta.capitalize()                    # odstavit
        print(VETA + "\b\b.", end=" ")              ## zakomentovat
    print("\n")                                     ## zakomentovat

#            soubor.write(VETA + "\b\b. ")
#        soubor.write("\n\n")


