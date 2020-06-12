def count_substring(string, sub_string):
    count=0
    print(string,sub_string)
    if len(string)==1:
        if sub_string==string:
           count=int(1)
        return count
    else:
      #for a given string it should iterate till the character from which whole length of substring can be fetched
        for i in range(0,len(string)-len(sub_string)+1):
            print(len(string)-len(sub_string)+1)
            #it should be slicing main string to the length of sub string.
            x=string[i:i+len(sub_string)]
            print(x)
            if x==sub_string:
                count=count+1
        return count
