def corresponding_parenthesis(text):
    sobra = text.count("(") - text.count(")")
    if sobra<1:
         sobra = sobra*-1
    
    count = 0
    str_sobra = ""
    while count < sobra:
        if text.count("(") > text.count(")"):
            str_sobra+="("
            count+=1
        else:
          str_sobra+=")"
          count+=1
           
    return str_sobra


print(corresponding_parenthesis(")))((((("))

def remove_more_than_two_repetitions(text):
   new_sentece = text[:2]
   count = 2
   while count < len(text):
       if text[count] != text[count-1] or text[count] != text[count-2]:
        new_sentece+=text[count]
       elif text[count] != text[count-2] and text[count] == text[count-1]:
        new_sentece+=text[count]
       elif count == len(text)-1 and text[count] == text[count-1] and text[count] != text[count-2]:
        new_sentece+=text[count]
       elif count == len(text)-1 and text[count] == text[count-1] and text[count] == text[count-2]:
        pass
       elif text[count] == text[count-1] and text[count] == text[count+1] and text[count-2] !=text[count]:
        new_sentece+=text[count]

       count+=1
   return new_sentece

print(remove_more_than_two_repetitions("aaaabbbbaacaaaxxxxii"))


