# date fiind dataseturile clients.json și transactions.csv
#
# 1) creăm clase care să reprezinte datele
class Client:
    pass
# cu câmpurile:
# - name
# - email
# - accounts

class Account:
    pass
# cu câmpurile
# - id
# - client
# - overdraft
# - balance


class Transaction:
    pass
# cu câmpurile
# - account_id
# - transaction_type
# - amount


# 2) să încărcăm json-ul:
#    pentru fiecare client din json
#    adăugați la o listă `clients`
#    un obiect Client

# ignorând momentan pe "bank_accounts"

import json


class Client:
    def __init__(self, name, email, accounts=None):
        self.name = name
        self.email = email
        self.accounts = [] if accounts is None else accounts

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"

    @classmethod
    def load_from_json(cls, fname):
        clients = []

        with open(CLIENTS_JSON, encoding="utf-8") as fp:
            dataset = json.load(fp)
            for cl in dataset:
                client = Client(
                    name=cl['name'],
                    email=cl['email_address'],
                )
                clients.append(client)

        return clients


CLIENTS_JSON = "data/clients.json"


class Account:
    # TODO: id se autogenerează
    def __init__(self, id, client, overdraft=0):
        self.id = id
        self.client = client
        self.overdraft = overdraft
        self.balance = 0
 
class Transaction:
    def __init__(self, account_id, type, amount):
        self.account_id = account_id
        self.type = type
        self.amount = amount

