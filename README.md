# Loremipsum
## Co to je?
Lorem ipsum je program pro vytvoření "výplňového textu", který je pouze vzhledově podobný reálnému jazyku.
## Mé zpracování
Při psaní kódu jsem se zaměřil na několik bodů: \
* Měl by vypadat jako čeština
Toho jsem dosáhl díky výběru českých slov při tvoření slovníku
* Stylizace textu
    * Velké písmeno na začátku věty \
Pro to jsem použil funkci 'capitalize()'
    * Tečka na koci vět \
Pro to jsem použil funkci pro úpravu textu '\b +.'
    * Občasné čárky ve větách \
Stejné jako s tečkami '\b + ,'
    * Délka věty a odstvaců\
Tu jsem předem nastavil na vhodné rozmezí. Dalo by so to však velmi jednoduše nastavit na user input. 
## Jak program použít
Když program spustíte, zeptá se vás na počet odstavců, které chcete vygenerovat. Po stisknutí klávesy 'Enter' se váš text vygeneruje do terminálu. Pokud chcete tex vygenerovat do .txt, stačí následovat zakomentované poznámky následovat a následně smazat. Tím se vytvoří nový soubor s názvem 'Text.txt' kde bude váš text. \
**Mé doporuučení je text generovat do terminálu z důvodu nekonečných řádků v textovém souboru, takže by se celý osdtavec vygeneroval na jeden řádek. A textový soubor nepodporuje funkci backspace '\b'.**

