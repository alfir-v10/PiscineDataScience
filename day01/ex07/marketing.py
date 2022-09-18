import sys


def call_center(clients, recipients):
    return list(clients - recipients)


def potential_clients(participants, clients):
    return list(participants - clients)


def loyalty_program(participants, clients):
    return list(clients - participants)


def marketing(task):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
               'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                    'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    clients, participants, recipients = set(clients), set(participants), set(recipients)

    dict_task = {'call_center': [call_center, clients, recipients],
                 'potential_clients': [potential_clients, participants, clients],
                 'loyalty_program': [loyalty_program, participants, clients]}
    to_do = dict_task.get(task)
    if not to_do:
        raise Exception("Invalid argument")
    print(to_do[0](to_do[1], to_do[2]))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        marketing(sys.argv[1])
