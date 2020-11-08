# Denne fil indeholder nu kun de genanvendelige dele

import pickle

filename = 'betalinger.pk'
with open(filename, 'rb') as infile:
    payments = pickle.load(infile)

# Samlet indbetaling pr. person i øre
total_amount = 450000 / len(payments)


# Jeg har valgt at bruge mellemliggende funktioner til at interagere med dict'et så det eventuelt ville kune skiftes ud
# med en anden datatype uden at påvirke dem som er afhængige af det
def paid(name: str):
    return payments[name]


def paid_all():
    return payments.items()


def names():
    return payments.keys()


def sort_by_amount(items: [()], reverse: bool = False):
    return sorted(items, key=lambda item: item[1], reverse=reverse)


def worst_payers(number: int):
    sorted_items = sort_by_amount(payments.items())
    return sorted_items[:number]


def validate_amount(name: str, amount_string: str):
    try:
        converted_amount = round(float(amount_string) * 100)
    except ValueError:
        valid = False
        error = "Beløbet er ikke gyldigt"
    else:
        summed_amount = payments[name] + converted_amount

        if summed_amount > total_amount:
            remaining_amount = total_amount - payments[name]
            valid = False
            error = f"Det indtastede beløb overskrider det resterende beløb på {remaining_amount / 100} kr. \n"

        elif summed_amount < 0:
            valid = False
            error = f"Tilbageførslen overskrider det samlede indbetalte beløb på {payments[name] / 100} kr."

        else:
            valid = True
            error = None

    return valid, error


def deposit(name: str, amount: int):
    payments[name] += amount


def save():
    with open(filename, 'wb') as outfile:
        pickle.dump(payments, outfile)
