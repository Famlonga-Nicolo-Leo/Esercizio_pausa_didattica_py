import random

# Classe Pokémon
class Pokemon:
    def __init__(self, nome, tipo, attacco, difesa, velocità, mosse):
        self.nome = nome
        self.tipo = tipo
        self.attacco = attacco
        self.difesa = difesa
        self.velocità = velocità
        self.mosse = mosse
        self.ps = 100  # Punti salute iniziali

    def subisci_danno(self, danno):
        self.ps -= danno
        if self.ps < 0:
            self.ps = 0

    def è_vivo(self):
        return self.ps > 0

    def usa_mossa(self, mossa, avversario):
        danno = mossa.calcola_danno(self, avversario)
        avversario.subisci_danno(danno)
        return danno


# Classe Mossa
class Mossa:
    def __init__(self, nome, tipo, potenza):
        self.nome = nome
        self.tipo = tipo
        self.potenza = potenza

    def calcola_danno(self, attaccante, difensore):
        danno_base = (attaccante.attacco / difensore.difesa) * self.potenza
        danno_finale = max(0, danno_base)  # Non può essere negativo
        return danno_finale


# Funzione per scegliere un Pokémon
def scegli_pokemon(pokemon_lista):
    print("Scegli un Pokémon:")
    for i, p in enumerate(pokemon_lista):
        print(f"{i + 1}. {p.nome}")
    scelta = int(input("Inserisci il numero del Pokémon: ")) - 1
    return pokemon_lista[scelta]


# Funzione per scegliere una mossa
def scegli_mossa(pokemon):
    print(f"\n{pokemon.nome} può usare le seguenti mosse:")
    for i, mossa in enumerate(pokemon.mosse):
        print(f"{i + 1}. {mossa.nome} (Tipo: {mossa.tipo}, Potenza: {mossa.potenza})")
    while True:
        try:
            scelta = int(input("Scegli una mossa (numero): ")) - 1
            if 0 <= scelta < len(pokemon.mosse):
                return pokemon.mosse[scelta]
            else:
                print("Scelta non valida. Riprova.")
        except ValueError:
            print("Per favore inserisci un numero valido.")


# Funzione per gestire il combattimento
def combattimento(pokemon1, pokemon2):
    turno = 0
    while pokemon1.è_vivo() and pokemon2.è_vivo():
        turno += 1
        print(f"\nTurno {turno}")

        # Giocatore 1 sceglie la mossa
        print(f"\n{pokemon1.nome}'s turn:")
        mossa1 = scegli_mossa(pokemon1)
        danno1 = pokemon1.usa_mossa(mossa1, pokemon2)
        print(f"{pokemon1.nome} usa {mossa1.nome}!")
        print(f"{pokemon2.nome} subisce {danno1:.2f} danni! (PS: {pokemon2.ps:.2f})")

        if not pokemon2.è_vivo():
            print(f"{pokemon2.nome} è stato sconfitto!")
            break

        # Giocatore 2 sceglie la mossa
        print(f"\n{pokemon2.nome}'s turn:")
        mossa2 = scegli_mossa(pokemon2)
        danno2 = pokemon2.usa_mossa(mossa2, pokemon1)
        print(f"{pokemon2.nome} usa {mossa2.nome}!")
        print(f"{pokemon1.nome} subisce {danno2:.2f} danni! (PS: {pokemon1.ps:.2f})")

        if not pokemon1.è_vivo():
            print(f"{pokemon1.nome} è stato sconfitto!")
            break


# Creiamo delle mosse
tuono = Mossa("Tuono", "Eletrico", 90)
lanciafiamme = Mossa("Lanciafiamme", "Fuoco", 90)
puntura = Mossa("Puntura", "Veleno", 35)
graffio = Mossa("Graffio", "Normale", 40)
morso = Mossa("Morso", "Normale", 50)  # Aggiunta mossa "Morso" per Charmander
idropompa = Mossa("Idropompa", "Acqua", 90)
vampata = Mossa("Vampata", "Fuoco", 100)
frustata = Mossa("Frustata", "Normale", 30)
sintesi = Mossa("Sintesi", "Erba", 0)  # Cura il Pokémon
abbaglio = Mossa("Abbaglio", "Normale", 60)
frana = Mossa("Frana", "Terra", 80)
volo = Mossa("Volo", "Volante", 75)
scoppio = Mossa("Scoppio", "Fuoco", 110)
scivolata = Mossa("Scivolata", "Acciaio", 65)
vapore = Mossa("Vapore", "Acqua", 70)
colpo = Mossa("Colpo", "Normale", 50)

# Creiamo dei Pokémon
pikachu = Pokemon("Pikachu", "Eletrico", 55, 40, 90, [tuono, puntura, graffio])
charmander = Pokemon("Charmander", "Fuoco", 52, 43, 65, [lanciafiamme, graffio, morso])
bulbasaur = Pokemon("Bulbasaur", "Erba", 49, 49, 45, [frustata, sintesi, graffio])
squirtle = Pokemon("Squirtle", "Acqua", 48, 65, 43, [idropompa, graffio, sintesi])
jigglypuff = Pokemon("Jigglypuff", "Normale", 45, 48, 50, [abbaglio, frustata, graffio])
rattata = Pokemon("Rattata", "Normale", 56, 35, 72, [colpo, graffio, frustata])
pidgey = Pokemon("Pidgey", "Volante", 45, 40, 56, [volo, graffio, abbaglio])
eevee = Pokemon("Eevee", "Normale", 55, 50, 55, [frustata, graffio, colpo])
meowth = Pokemon("Meowth", "Normale", 45, 35, 90, [graffio, abbaglio, colpo])
sandshrew = Pokemon("Sandshrew", "Terra", 75, 85, 40, [frana, graffio, colpo])
koffing = Pokemon("Koffing", "Veleno", 60, 50, 35, [puntura, scivolata, graffio])
caterpie = Pokemon("Caterpie", "Insetto", 30, 35, 45, [graffio, frustata])
bellsprout = Pokemon("Bellsprout", "Erba", 50, 35, 40, [frustata, sintesi, graffio])
spearow = Pokemon("Spearow", "Volante", 60, 30, 70, [volo, graffio, abbaglio])
diglett = Pokemon("Diglett", "Terra", 55, 25, 90, [frana, colpo, graffio])
chikorita = Pokemon("Chikorita", "Erba", 49, 49, 45, [sintesi, frustata, graffio])
totodile = Pokemon("Totodile", "Acqua", 65, 55, 43, [idropompa, graffio, scivolata])
cyndaquil = Pokemon("Cyndaquil", "Fuoco", 58, 40, 65, [vampata, morso, graffio])
slugma = Pokemon("Slugma", "Fuoco", 40, 40, 20, [vampata, scoppio, graffio])
lugia = Pokemon("Lugia", "Psichico", 80, 90, 110, [volo, scivolata, frana])
hooh = Pokemon("Ho-oh", "Fuoco", 130, 90, 90, [scoppio, vampata, colpo])
grimer = Pokemon("Grimer", "Veleno", 60, 50, 40, [puntura, scivolata, colpo])
magikarp = Pokemon("Magikarp", "Acqua", 10, 55, 80, [graffio, frustata])
gyarados = Pokemon("Gyarados", "Acqua", 125, 79, 81, [idropompa, scivolata, scoppio])
tropius = Pokemon("Tropius", "Erba", 68, 83, 51, [frustata, frana, volo])
luxray = Pokemon("Luxray", "Eletrico", 120, 79, 70, [tuono, scivolata, graffio])
garchomp = Pokemon("Garchomp", "Drago", 130, 95, 92, [frana, scivolata, scoppio])
snorlax = Pokemon("Snorlax", "Normale", 110, 65, 30, [colpo, frustata, graffio])

# Lista di Pokémon da scegliere per i giocatori
pokemon_giocatore1 = [pikachu, bulbasaur, squirtle, jigglypuff, eevee, sandshrew, meowth, diglett, chikorita, totodile]
pokemon_giocatore2 = [charmander, rattata, pidgey, koffing, caterpie, bellsprout, spearow, slugma, cyndaquil, grimer]

# Giocatori scelgono i Pokémon
giocatore1_pokemon = scegli_pokemon(pokemon_giocatore1)
giocatore2_pokemon = scegli_pokemon(pokemon_giocatore2)

# Inizia il combattimento
combattimento(giocatore1_pokemon, giocatore2_pokemon)
