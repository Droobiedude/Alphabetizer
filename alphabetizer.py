def alphabetizing_tool():
    items = []
    
    while True:
        # Prompt the user for input
        item = input("Enter a name/item (type 'b' to stop): ").strip()
        
        # Break the loop if 'b' is entered
        if item.lower() == 'b':
            break
        
        # Add the entered item to the list
        items.append(item)
    
    # Sort the list alphabetically
    sorted_items = sorted(items)
    
    # Display the sorted list
    print("\nHere are the sorted names/items:")
    for i in sorted_items:
        print(i)

# Run the tool
alphabetizing_tool()
