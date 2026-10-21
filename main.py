def main():
    print("hello world")
    my_list = ["h", "e", "l", "l", "o"] 
    print(my_list)    
    # What do you see? Record it here:
    #I printed out my each indiviual letter as my list, and when I printed it in the terminal I got ['k', 'y', 'a', 'n', 'n', 'i']
    my_list.append("!") 
    print(my_list)
    # What changed? Describe the difference between the original and updated list: The only thing that changed was the addiotional character within my list or after the i. 
    print(len(my_list))
    # How many elements are there? Record it: there are 6 elements 
    print(my_list[4:6])
    # What values were returned? Why do those indexes work? The last two characters are returned 
    print(my_list[4:])
    # What do you notice? Is the result the same as above? 
    # I notice that nothing changed and printed out the exact code above
    print(my_list[-2:])
    # What does this do? Why is it useful?
    # It kept the same code as above, nothing changed 
    my_list.remove("l")
    print(my_list)
    # What changed? Where did it remove the "l" from?
    #One l was removed from the hello and has now printed ['h', 'e', 'l', 'o', '!']

    my_list.insert(2, "l")
    print(my_list)
    #Did it go where you expected? What is at index 2 now? 
    #in index two there is an added l because the code told it to add it in.
   
    del my_list[0]
    print(my_list)
    # What item got removed?
    #the H got removed because it was the first element 

    last_item = my_list.pop()
    print(last_item)
    print(my_list)
    # What item was removed? What’s left in the list?
    #The h is still not there, and now the ! has been removed from the list 

    print(my_list[2])
    # What is it? It is l
    print("!" in my_list)
    # True or False? Why?
    #False because it is and has been removed 

    my_list.sort(reverse=True)
    print(my_list)
    # What is the new order? Did sort() return anything?
    # The new order is ['o', 'l', 'l', 'e'] and no sort did not return anything other than it in reverse and put an e at the end 
    print(sorted(my_list))
    print(my_list)
    # Did the original change? What’s the difference between sorted() and sort()? 
    #Yes, the difference between sorted() and sort() is one list gets sorted the "correct way" while the other gets sorted() "reversely"

    my_tuple = ("red", "green", "blue")
    print(my_tuple)
    # What values are inside this tuple?
    #strings are inside this tuple
    
    print(my_tuple[0])
    print(my_tuple[-1])
    # What was printed in each case? Why does negative indexing work? #Both red and blue have been printed, negative indexing works because it turns it positive in the length

    #my_tuple[1] = "yellow"
    # What happens? What error do you get?
    #you get an error because the first index is not yellow it is green 
    
    one_item = ("hello",)
    print(one_item)
    # What do you notice about the syntax?
    # it has gone away and has now printed hello

    colors = ("red", "blue", "red", "green", "red")
    print(colors.count("red"))
    # How many "red" entries are there? There are 3 red entries 

    print(colors.index("green"))
    # What position is "green" in the tuple? The position is 3 
    


    






if __name__ == "__main__":
    main()
    
   
