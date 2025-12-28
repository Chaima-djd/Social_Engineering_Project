import random

def run_simulation():
    print("=== Simulateur d’Ingénierie Sociale Physique ===\n")

    scenarios = [
        (
            "Tailgating",
            "Vous arrivez devant une porte sécurisée avec badge.\n"
            "Un inconnu vous suit en portant des boîtes.\n"
            "Ouvrez-vous la porte pour lui ? (O/N) : ",
        ),
        (
            "Baiting",
            "Vous trouvez une clé USB étiquetée 'Salaires 2025 – Confidentiel'\n"
            "dans le parking.\n"
            "Branchez-vous cette clé ? (O/N) : ",
        ),
        (
            "Impersonation",
            "Un technicien en uniforme frappe à votre bureau :\n"
            "'Je dois vérifier le câblage.'\n"
            "Le laissez-vous entrer sans vérifier son identité ? (O/N) : ",
        ),
    ]

    score = 0

    
    
    for name, prompt in scenarios:
        print(f"\n--- Scénario : {name} ---")
        response = input(prompt).upper()

        if response == "N":
            score += 33
            print("✔ Réponse sûre")
        elif response == "O":
            print("✖ Réponse à risque")
        else:
            print("Réponse invalide → 0 point")

    print("\n=== Résultat final ===")
    print(f"Score de résilience : {score}/100")

    if score <= 33:
        print("Niveau : Faible résilience ")
    elif score <= 66:
        print("Niveau : Résilience moyenne ")
    else:
        print("Niveau : Bonne résilience ")

if __name__ == "__main__":
    run_simulation()
