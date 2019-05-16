def verifieUseFonctionalite():

    while True:
        value = input('choisir parmi les fontion suivante  celle qui vous convient (generer,modifier,recuperer,afficher) tous les mots de passe:   ')
        if value == 'generer':
            print("vous vouler generer un mot de passe")
            break
        elif value == 'modifier':
            print("vous vouler modifier un mot de passe")
            break
        elif value == 'recuperer':
            print("vous vouler recuperer un mot de passe")
            break
        elif value == 'afficher':
            print("vous vouler tout afficher les mots de passe")
            break
        else :
            print("nous ne disposons pas de cette option")
verifieUseFonctionalite()

