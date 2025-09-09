# write a program to check if list contains a palindrome of element.
# use copy() method to copy the list and reverse the copied list.
# compare the original list with the reversed list.
# if both are same then list contains palindrome of element otherwise not.
# example: 
list=[1,2,3,2,1]
copy_list=list.copy()
copy_list.reverse()
print(copy_list)
if (list==copy_list):
    print("list contains palindrome of element")
else:
    print("list does not contains palindrome of element")