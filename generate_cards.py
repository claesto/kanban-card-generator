from kanbancard import KanbanCard

def generate_kanban_cards():
    list_name = "Groceries"

    items = [
        { "item": "Example item", "brand": "Example brand", "store": "Example store", "kanban_level": 2, "order_qty": 1, "list_name": list_name },
        { "item": "Lorem", "brand": "Ipsum", "store": "Dolor sit", "kanban_level": 2, "order_qty": 1, "list_name": list_name }
    ]

    kanban_cards = [KanbanCard(**item) for item in items]
    return kanban_cards

if __name__ == "__main__":
    cards = generate_kanban_cards()

    for card in cards:
        print(vars(card))