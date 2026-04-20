def text_editor(text = ""):
    stack = [text]
    while True:
        action = input("Enter action (type/undo/delete/exit): ").lower().strip()
        if action == "type":
            new_text = input("Enter a text: ")
            text = text + new_text
            stack.append(text)

        elif action == "delete":
            try:
                k = int(input("Enter number of characters to delete: "))
                text = text[:-k]
                stack.append(text)
            except:
                print("Please enter a valid number.")
        elif action == "print":
            print(text)
        elif action == "undo":
            if len(stack) > 1:
                stack.pop()
                text = stack[-1]
                print("Last action undone.")
            else:
                print("Nothing left to undo!")

        elif action == "exit":
            break     
        else:
            print("Invalid action.")
text_editor()