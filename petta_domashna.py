#Da se napravi programa so klasi Akter i Film.
#Klasata akter da gi slednive podatoci:
#1.Ime
#2.Prezime
#3.Godina na ragjanje
#4.Broj na filmovi
#5.Broj na nagradi
#6.Dali ima dobieno oskar

#Da ima get i set metodi za site podatoci
#So pomos na ciklus da se napravat objekti kolku sto saka korisnikot, i da se najde koj akter dobieno najveke nagradi

class Akter:
   
    def __init__(self, ime, prezime, godina_raganje, br_filmovi, br_nagradi, oskar ):
        self.ime = ime 
        self.prezime = prezime
        self.godina_raganje = godina_raganje
        self.br_filmovi = br_filmovi
        self.br_nagradi = br_nagradi
        self.oskar = oskar

    def promeni_ime(self, novo_ime):#set metod
        self.ime = novo_ime
        print("Imeto e promenet vo {}".format(novo_ime))

    def get_ime(self): #get metod
        return self.ime

    def promeni_prezime(self, novo_prezime):#set metod
        self.prezime = novo_prezime
        print("Prezimeto e promenet vo {}".format(novo_prezime))

    def get_prezime(self): #get metod
        return self.prezime
    
    def promeni_br_filmovi(self, novo_br_filmovi):#set metod
        self.br_filmovi = novo_br_filmovi
        print("Brojot na filmovi e promenet vo {}".format(novo_br_filmovi))

    def get_br_filmovi(self): #get metod
        return self.br_filmovi
    
    def promeni_br_nagradi(self, novo_br_nagradi):#set metod
        self.br_nagradi = novo_br_nagradi
        print("Brojot na nagradi e promenet vo {}".format(novo_br_nagradi))

    def get_br_nagradi(self): #get metod
        return self.br_nagradi
    
    def promeni_oskar(self, novo_oskar):#set metod
        self.oskar = novo_oskar
        print("Brojot na oskar e promenet vo {}".format(novo_oskar))

    def get_oskar(self): #get metod
        return self.oskar


akter = []
while True:
    ime= str(input ("Vnesete ime na akterot : "))
   
    prezime = str( input ("Vnesete prezime: "))
    
    godina_raganje = int(input ("Vnesete godini na raganje: "))
   
    br_filmovi = str(input ("Vnesete broj na filmovi: "))
   
    br_nagradi= int(input ("Vnesete broj na nagradi: "))
   
    oskar= str( input ("Dali ima dobieno oskar: "))
    akter_obj = Akter(ime, prezime, godina_raganje, br_filmovi, br_nagradi, oskar)
    akter.append(akter_obj) 

    #akter.append(Akter(imeAkter, prezimeAkter, godinaAkter, brFilmoviAkter, brNagradiAkter, oskarAkter)) moze da se zapishe i na ovoj nacin 
    da_ne = input("Dali sakate da vnesete drug akter (da/ne): ")
    if (da_ne == 'ne'):
        break
 
print("__" * 25)

for i in akter:
    print("Ime:", i.ime)
    print("Prezime:", i.prezime)
    print("Godina na ragjanje: ", i.godina_raganje)
    print("Broj na filmovi: ", i.br_filmovi)
    print("Broj na nagradi: ", i.br_nagradi)
    print("Dobien Oskar: ", i.oskar)

    print("__" * 25)


najmnogu_nagradi= 0
akter_nagradi=""
for i in akter:
    if i.br_nagradi > najmnogu_nagradi:
       najmnogu_nagradi = br_nagradi
       akter_nagradi=i.ime

print("Brojot na najmnogu nagradi e{} od {}".format(najmnogu_nagradi, i.ime))
    
#ne mi printa sekogash tocen rezultati 