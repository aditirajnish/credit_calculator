from math import log, ceil
import sys

def raiseError():
    print("Incorrect parameters")


def calculateDiff(P, n, i):
    total_payment = 0
    for m in range(1, n + 1):
        a = ceil((P / n) + (i * (P - ((P * (m - 1)) / n))))
        total_payment += a
        print(f"Month {m}: paid out {a}")
    o = int(total_payment - principal)
    print(f"Overpayment = {o}")

def calculateAnnuity(P, a, n, i):
    if P == -1:
        P = int(a / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1)))
        o = int(n * a - P)
        print(f"Your credit principal = {P}!")
        print(f"Overpayment = {o}")
    elif a == -1:
        a = ceil(P * ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1)))
        o = int(n * a - P)
        print(f"Your annuity payment = {a}!")
        print(f"Overpayment = {o}")
    else:
        n = ceil(log((a / (a - i * P)), (1 + i)))
        years = n // 12
        months = n % 12
        if years == 0 and months > 1:
            print(f"You need {months} months to repay this credit!")
        elif years == 0 and months == 1:
            print(f"You need 1 month to repay this credit!")
        elif months == 0 and years >= 1:
            print(f"You need {years} years to repay this credit!")
        elif months == 0 and years == 1:
            print("You need 1 year to repay this credit!")
        else:
            print(f"You need {years} years and {months} months to repay this credit!")
        o = int(n * a - P)
        print(f"Overpayment = {o}")

args = sys.argv[1:]
diff_correct_params = {"type", "principal", "periods", "interest"}
annuity_correct_params = {"principal", "payment", "periods", "interest"}

if len(args) < 4:
    raiseError()
else:
    params = {}
    for arg in args:
        parameter = arg.split("=")
        param = parameter[0].lstrip("--")
        value = parameter[1]
        params[param] = value
    if "type" not in params.keys():
        raiseError()
    elif params["type"] != "annuity" and params["type"] != "diff":
        raiseError()
    else:
        if params["type"] == "annuity":
            if "interest" not in params.keys():
                raiseError()
            else:
                number_of_incorrect_params = 0
                correct = True
                for param, value in params.items():
                    if param != "type":
                        if param not in annuity_correct_params:
                            number_of_incorrect_params += 1
                        if float(value) < 0 or number_of_incorrect_params > 1:
                            raiseError()
                            correct = False
                            break
                if correct:
                    interest = float(params["interest"]) / (12 * 100)
                    if "principal" not in params.keys():
                        principal = -1
                        payment = float(params["payment"])
                        periods = int(params["periods"])
                    elif "payment" not in params.keys():
                        payment = -1
                        principal = float(params["principal"])
                        periods = int(params["periods"])
                    else:
                        periods = -1
                        payment = float(params["payment"])
                        principal = float(params["principal"])
                    calculateAnnuity(principal, payment, periods, interest)
        else:
            if set(params.keys()) != diff_correct_params:
                raiseError()
            else:
                principal = float(params["principal"])
                periods = int(params["periods"])
                interest = float(params["interest"]) / (12 * 100)
                if principal < 0 or periods < 0 or interest < 0:
                    raiseError()
                else:
                    calculateDiff(principal, periods, interest)