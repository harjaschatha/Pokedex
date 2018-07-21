from pprint import pprint

EFFECTS = {
    "Normal": {
        "0.0": ["Ghost"],
        "0.5": [],
        "1.0": ["Normal", "Fire", "Water","Electric", "Grass", "Ice", "Poison",
            "Flying", "Psychic", "Bug", "Rock", "Dragon", "Dark", "Steel", "Fairy"],
        "2.0": ["Fighting"],
    },
    "Fire": {
        "0.0": [],
        "0.5": ["Fire", "Grass", "Ice", "Bug", "Steel", "Fairy"],
        "1.0": ["Normal", "Electric", "Fighting", "Poison", "Flying",
            "Psychic", "Ghost", "Dragon", "Dark"],
        "2.0": ["Water", "Rock", "Ground"],
    },
    "Water": {
        "0.0": [],
        "0.5": ["Fire", "Water", "Ice", "Steel"],
        "1.0": ["Normal", "Fighting", "Poison", "Ground", "Flying",
                "Psychic", "Bug", "Rock", "Ghost", "Dragon",
                "Dark", "Fairy"],
        "2.0": ["Electric", "Grass"],
    },
    "Electric": {
        "0.0": [],
        "0.5": ["Electric", "Flying", "Steel"],
        "1.0": ["Normal", "Fire", "Water", "Grass", "Ice", "Fighting", "Poison",
                "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Fairy"],
        "2.0": ["Ground"],
    },
    "Grass": {
        "0.0": [],
        "0.5": ["Water", "Electric", "Grass", "Ground"],
        "1.0": ["Normal", "Fighting", "Psychic", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"],
        "2.0": ["Fire", "Ice", "Poison", "Flying", "Bug"],
    },
    "Ice": {
        "0.0": [],
        "0.5": ["Ice",],
        "1.0": ["Normal", "Water",  "Electric", "Grass", "Poison", "Ground",
            "Flying", "Bug", "Psychic", "Ghost", "Dragon", "Dark", "Fairy"],
        "2.0": ["Fire", "Fighting", "Rock", "Steel"],
    },
    "Fighting": {
        "0.0": [],
        "0.5": ["Bug", "Rock", "Dark"],
        "1.0": ["Normal", "Fire", "Water", "Electric", "Grass", "Ice","Fighting", "Poison", "Ground",
                  "Ghost", "Dragon", "Steel"],
        "2.0": [ "Flying", "Psychic", "Fairy"],
    },
    "Poison": {
        "0.0": [],
        "0.5": ["Grass", "Fighting", "Poison", "Bug", "Fairy"],
        "1.0": ["Normal", "Fire", "Water", "Electric", "Ice", "Flying", "Rock", "Ghost", "Dragon", "Dark", "Steel"],
        "2.0": ["Ground", "Psychic"],
    },
    "Ground": {
        "0.0": ["Electric"],
        "0.5": ["Poison", "Rock"],
        "1.0": ["Normal", "Fire", "Fighting", "Ground", "Flying", "Psychic", "Bug", "Ghost", "Dragon","Dark", "Steel", "Fairy"],
        "2.0": [  "Water", "Grass", "Ice"],
    },
    "Flying": {
        "0.0": ["Ground"],
        "0.5": ["Bug", "Fighting", "Grass"],
        "1.0": ["Normal", "Fire", "Water", "Poison", "Flying",
                "Psychic","Ghost", "Dragon","Dark", "Steel", "Fairy"],
        "2.0": ["Electric", "Rock", "Ice"],
    },
    "Psychic": {
        "0.0": [],
        "0.5": ["Fighting", "Psychic"],
        "1.0": ["Normal", "Fire", "Water","Electric", "Grass", "Ice",  "Poison", "Ground", "Flying",
                "Rock", "Dragon", "Steel", "Fairy"],
        "2.0": ["Bug", "Ghost", "Dark"],
    },
    "Bug": {
        "0.0": [],
        "0.5": ["Fighting", "Psychic"],
        "1.0": ["Normal", "Fire", "Water","Electric", "Grass", "Ice",  "Poison", "Ground", "Flying",
                "Rock", "Dragon", "Steel", "Fairy"],
        "2.0": ["Bug", "Ghost", "Dark"],
    },
    "Rock": {
        "0.0": [],
        "0.5": ["Normal", "Fire", "Poison", "Flying"],
        "1.0": ["Electric", "Ice", "Psychic", "Bug", "Rock","Ghost", "Dragon", "Fairy"],
        "2.0": ["Water", "Grass", "Fighting", "Ground", "Steel"],
    },
    "Ghost": {
        "0.0": ["Normal", "Fighting"],
        "0.5": ["Poison", "Fighting"],
        "1.0": ["Fire", "Water", "Electric", "Grass", "Ice", "Ground", "Flying",
                "Psychic", "Rock", "Dragon","Steel", "Fairy"],
        "2.0": ["Ghost", "Dark"],
    },
    "Dragon": {
        "0.0": [],
        "0.5": ["Fire", "Water", "Electric", "Grass"],
        "1.0": ["Normal", "Fighting", "Poison", "Ground", "Flying",
                "Psychic", "Bug", "Rock", "Ghost","Steel"],
        "2.0": ["Ice", "Dragon", "Fairy"],
    },
    "Dark": {
        "0.0": ["Psychic"],
        "0.5": ["Ghost", "Dark"],
        "1.0": ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Poison", "Ground", "Flying",
                "Rock", "Dragon", "Steel"],
        "2.0": ["Fighting", "Bug", "Fairy"],
    },
    "Steel": {
        "0.0": ["Poison"],
        "0.5": ["Normal", "Grass", "Ice", "Flying", "Psychic", "Bug", "Rock", "Dragon", "Steel", "Fairy"],
        "1.0": ["Water", "Electric", "Ghost", "Dark"],
        "2.0": ["Fire", "Fighting", "Ground"],
    },
    "Fairy": {
        "0.0": ["Dragon"],
        "0.5": ["Fighting", "Bug", "Dark"],
        "1.0": ["Normal", "Fire", "Water", "Grass", "Ice", "Ground", "Flying", "Psychic", "Rock", "Ghost", "Fairy"],
        "2.0": ["Poison", "Steel",],
    }
}

def generate_defenses(type1, type2):
    defenses = {
        "0.0": [],
        "0.25": [],
        "0.5": [],
        "1.0": [],
        "2.0": [],
        "4.0": [],
    }

    if type2 == "":
        t1_effects = EFFECTS[type1]
        defenses["0.0"] = t1_effects["0.0"]
        defenses["0.25"] = []
        defenses["0.5"] = t1_effects["0.5"]
        defenses["1.0"] = t1_effects["1.0"]
        defenses["2.0"] = t1_effects["2.0"]
        defenses["4.0"] = []

    else:
        t1_effects = EFFECTS[type1]
        t2_effects = EFFECTS[type2]

        for key_i in t1_effects:
            s1 = set(t1_effects[key_i])
            for key_j in t2_effects:
                bracket = float(key_i) * float(key_j)
                s2 = set(t2_effects[key_j])
                intersect = s1.intersection(s2)

                if len(intersect) > 0:
                    for t in intersect:
                        defenses[str(bracket)] = list(defenses[str(bracket)])
                        defenses[str(bracket)].append(t)
                else:
                    if len(defenses[str(bracket)]) > 0:
                        pass
                    else:
                        defenses[str(bracket)] = set('')

    print("{} x {}\n".format(type1, type2))
    pprint(defenses)
    return defenses