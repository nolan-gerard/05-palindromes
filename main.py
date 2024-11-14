"""
Bonjour, dans cet exercice on vérifie si une chaine de caractère est un palindrome.
Pour cela on va appeller dans une fonction main une fonction is palindrome qui le vérifier.
"""
#### Fonction secondaire


def ispalindrome(p):
    # votre code ici
    """
    Cette méthode enlève les accents en les remplaçant par
    leurs lettres équivalentes et en mettant tout le string en minuscule.
    Puis elle compare le premier caractère avec le dernier,
    puis les deux suivants et ainsi de suite.
    """
    rep=True
    p=p.lower()
    accents=str.maketrans("éèêëàâäîïôöùûüç","eeeeaaaiioouuuc"," ,?;.:/!'()-")
    p=p.translate(accents)
    x=len(p)
    for i in range(0,x):
        a=p[i]
        b=p[x-i-1]
        if a!=b:
            rep=False
    return rep

#### Fonction principale


def main():
    """
    Cette méthode appelle ispalindrome et va afficher le string et son booléen correspondant.
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
