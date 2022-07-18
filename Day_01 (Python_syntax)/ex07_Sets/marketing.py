import sys

def get_list(group_name):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 
                'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 
                    'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 
                    'mr@robot.gov', 'eleven@yahoo.com']
    
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    if group_name == 'clients':
        return clients
    elif group_name == 'participants':
        return participants
    else:
        return recipients

def call_center():
    return list(set(get_list('clients')) - set(get_list('recepients')))

def potential_clients():
    return list(set(get_list('participants')) - set(get_list('clients')))

def loyalty_program():
    return list(set(get_list('clients')) - set(get_list('participants')))


def choose_group(marketing_goal):
    if marketing_goal == 'call_center':
        print(call_center())
    elif marketing_goal == 'potential_clients':
        print(potential_clients())
    elif marketing_goal == 'loyalty_program':
        print(loyalty_program())


def main():
    if len(sys.argv) != 2:
        raise ValueError('Wrong number of arguments')
    choose_group(sys.argv[1])
    
if __name__ == '__main__':
    main()