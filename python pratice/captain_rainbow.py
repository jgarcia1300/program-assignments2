checklist = ()

def create(item):
    checklist.append(item)

    return "Added {} to checklist".format(item)

def read(index):

    print(checklist[index])

    return checklist[index] 

def update(index, item):

    old = checklist[index] 

    checklist[index] = item
    return "Changed {} to {}".format(old, item)

def destroy(index):
    checklist.pop(index)

    return "Removed {} from checklist".format(checklist[index])

def all_items():

    items = []
    
    for el in checklist:
        print(el)
        items.append(el)
    return items

def checked(index):
    unchecked = checklist[index] 
    checklist[index] = "√" + unchecked
    return checklist[index]

def user_input(prompt):
    entry = input(prompt)
    return entry 

def user_choice():
    editing = True 
    while editing:

        choice = user_input("Which function would you like to use? Enter C for create, R for read, U for update, D for destroy.")
        
        if choice == "C" or choice == "c":
            item = user_input("What item do you wish to create? Type out the name of your desired item.")
            create(item)
            continue 

        elif choice == "R" or choice == "r":
            item = user_input("What item do you wish to read? Give a number for the position of the item.")
            read(int(index))
            continue 

        elif choice == "U" or choice == "u":
            update_index = user_input("what item do you wish to update?")
            new_item = user_input( "type out the name of your new desired item and a number for its position.")
            update(int(update_index, new_item))
            continue 

        elif choice == "D" or choice == "d":
            delete_index = user_input("What item do you wish to delete? Give a number for the position of teht item.")
            destroy(int(delete_index))
            continue 

        else:
            end = user_input("Do you wish to quit? Enter Y for yes or N for no.")
            if end == "Y" or end == "y":
                print(checklist)
                editing = False

            else:
                continue 
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(all_items())
    print(checked(0))
    print(user_input("is this working"))
    user_choice()

test()
user_choice()