import fodboldtur


# En decorator som vedhæfter en forklaring til en funktion
def described(description: str):

    def decorator(target: callable):
        target.description = description
        return target

    return decorator


@described("Vis hvor meget hver person har indbetalt")
def print_payments():
    for name, paid in fodboldtur.paid_all():
        if paid < fodboldtur.total_amount:
            print(f"{name}: indebetalt: {paid / 100} kr., manglende: {(fodboldtur.total_amount - paid) / 100} kr.")
        else:
            print(f"{name}: indebetalt: {paid / 100} kr., fuldt betalt!")


@described("Vis dem som har betalt mindst")
def print_worst_payers():
    # Jeg har valgt at lade brugeren vælge hvor mange personer de vil se

    def input_how_many():
        try:
            number = int(input("Antal personer: "))
        except ValueError:
            print("Antallet er ikke gyldigt")
            return input_how_many()
        else:
            if number <= 0:
                print("Antal skal være over 0")
                return input_how_many()

            else:
                return number

    how_many = input_how_many()
    worst = fodboldtur.worst_payers(how_many)

    for name, paid in worst:
        if paid == 0:
            print(f"{name} har ikke betalt noget som helst!")
        else:
            print(f"{name} har kun betalt {paid / 100} kr.")

    print("Puuuha, det er simpelthen for dårligt!")


@described("Indbetal eller tilbagefør beløb")
def deposit():
    # Jeg har valgt at tillade negative indbetalinger

    def input_amount() -> int:
        amount_string = input("Beløb (kr.): ")
        valid, error = fodboldtur.validate_amount(name, amount_string)

        if not valid:
            print(error)
            return input_amount()

        else:
            converted_amount = round(float(amount_string) * 100)
            return converted_amount

    def input_name() -> str:
        name_input = input("Navn: ")
        if name_input not in fodboldtur.names():
            print("Navn findes ikke")
            return input_name()
        else:
            return name_input

    name = input_name()
    amount = input_amount()
    fodboldtur.deposit(name, amount)
    print(
        f"{name} har i alt indbetalt {fodboldtur.paid(name) / 100} kr., "
        f"og mangler dermed at betale {(fodboldtur.total_amount - fodboldtur.paid(name)) / 100} kr."
    )


@described("Gem og afslut")
def save_and_quit():
    fodboldtur.save()
    print("Programmet er afsluttet!")
    quit()


def menu():
    commands = {
        "1": print_payments,
        "2": print_worst_payers,
        "3": deposit,
        "4": save_and_quit
    }

    def input_command():
        input_string = input("Indtast dit valg: ")

        if input_string in commands:
            return input_string
        else:
            print("Denne kommando er ikke gyldig")
            return input_command()

    while True:
        print("\nMENU")
        for key, function in commands.items():
            print(f"{key}: {function.description}")

        command = input_command()
        function = commands[command]
        function()


if __name__ == "__main__":
    menu()
