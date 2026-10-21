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
    
    my_set = {"apple", "banana", "cherry"}
    print(my_set)
    # Does the order match what you typed? Why or why not?
    #No the order does not match my type. It is because these sets are unordered 

    my_set.add("orange")
    print(my_set)
    # What changed?
    #Orange has been added to the set as the first index

    my_set.add("banana")
    print(my_set)
    #Did anything change? Why or why not?
    #Now banana is in the first index while orange in in the second

    my_set.remove("apple")
    print(my_set)
    # Which item is gone?
    #apple is now gone within the set because of the remove on line 96

    my_set.discard("pear")
    # What happened? Was there an error?
    #there was no error because pear was not origninally in the list

    tropical = {"banana", "mango", "papaya"}
    all_fruits = my_set.union(tropical)
    print(all_fruits)
    # What items are in the result? Any duplicates?
    #this is the end result {'mango', 'orange', 'cherry', 'papaya', 'banana'} there are no duplicates 

    
    my_dict = {"name": "Sam", "age": 16, "grade": "11th"}
    print(my_dict)
    # What keys and values are present?
    # his name, his age, and his grade
    print(my_dict["age"])
    # What value did this return?
    #this returned 16 

   # print(my_dict["school"])
    # What error do you get?
    #I got a my_dict error 

    my_dict["grade"] = "12th"
    print(my_dict)
    # Did the value update?
    #the value of the grade changed to 12th 

    my_dict["school"] = "Central High"
    print(my_dict)
    # What’s the new key and value?
    #The new key is school and central high 

    del my_dict["age"]
    print(my_dict)
    # Which key is missing now?
    #the age is now missing 

    print(my_dict.get("locker"))
    # What value was returned? Was there an error?  
    #None was returned, there was no error 

    for key, value in my_dict.items():
        print(key, "->", value)
    # What got printed? How does this help you read the dictionary?
    #name -> Sam grade -> 12th school -> Central High got printed. It gives us a better layout to read to code. Now the information is verticle, instead of horizontale. 


    







if __name__ == "__main__":
    main()
    
   
