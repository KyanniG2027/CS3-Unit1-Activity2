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
    






if __name__ == "__main__":
    main()
    
   
