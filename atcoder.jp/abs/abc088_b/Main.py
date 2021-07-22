number_of_cards = int(input())
cards_list = list(map(int, input().split()))


def pop_max_element(cards_list):
    return cards_list.pop(cards_list.index(max(cards_list)))


alice_cards_list = []
bob_cards_list = []
while cards_list:
    alice_cards_list.append(pop_max_element(cards_list))
    if not cards_list:
        break
    bob_cards_list.append(pop_max_element(cards_list))

print(sum(alice_cards_list)-sum(bob_cards_list))
