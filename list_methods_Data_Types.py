''' list methods in  DataTypes 
A list can be empty 
list can contain several datatypes in it and a list can also contain a list inside it.
List is mutable - can modified the list.
list is sequence        '''

# r = ['hii', 0,3.6,True,False,-256]
# print(r[-3],type(r))    # True
# print(r[8])            # IndexError : list index out of range
# print(r[5])           # -256


# w = ["python programming"]
# print(w[0])         # "python programming"
# w[1] = "Hello"    
# print(w)             # IndexError : list assignment index out of range


''' string examples '''

# e = "coding"
# e[3] = 'f'
# print(e)         # TypeError : 'str' object does not support item assignment.


''' starting with the list methods'''

# d = [3,'hey',3.6,True,[1,'code']]      # append method - will add the values in the end of the string
# d.append([True,None])
# print(d)                # [3,'hey', 3.6, True, [1, 'code'], [True, None]]


# t = [1,2,3,4,5,44,77,89,45,6,1]       # clear - will clear all the elements in the list and will return an empty list
# t.clear()                       # Doubt session
# print(t)          # []

# print(dir(list))


# x = [1,True,False,'Boolean',5,1,1,2,3,6,5,4,5,69,5]     # count- will gives the number of times the specified character has been appeared in the list
# print(x.count(1))     # 4
# print(x.count(True))     # 4
# print(x.count('boolean'))     # 0


# r = [1,2.3,5.6,8]          # extend - this method will helps us to add more than two arguments in the list
# t = ['Hello',55,True,None]
# r.extend(t)
# print(r)             # [1,2.3,5.6,8,'Hello',55,True,None]
# t.extend(r)
# print(t)              # ['Hello',55,True,None,1,2.3,5.6,8]




# s = [1,2,5,8,89,5,4,1]     # index - this method is used to get the index position of that specified character.
# print(s.index(2))       # 1
# print(s.index(1))       # 0
# print(s.index(89))         # 4
# print(s.index(0))           # ValueError: 0 is not in list



# e = [1,2,3.6,"hi",'boolean']       # insert - this method is used to insert the specified character at a specifed position in the list.
# e.insert(-9,5562356)
# e.insert(9,56)                    # [1,2,3.6,'hi','boolean',56]
# print(e)                         # [5562356,1,2,3.6,'hi','boolean',5562356]


# a = [True,'code',56,2.3,False]     # pop - this method is used remove the last character from the list by default by using index positions.
# a.pop()          # [True,'code', 56, 2.3 ]
# a.pop(True)       
# print(a)            # [True, 56, 2.3, False]
# print(a.pop(5))     # IndexError : pop index out of range

# n = [35,'program',-236,True, 23.65]    # remove - this method is used to remove the specified character from the list by calling the character.
# n.remove(35)     # ['program', -236, True, 23.65]
# n.remove(0)        # ValueError : list.remove(x) : x is not in list.
# print(n)



# m = [True,23,0,1,"hello",563256]    # reverse - this method is used to reverse the particular list but cannot be used on strings only
# m.reverse()
# print(m)      

# q = [1,23,.23,5623,89.25,1.021,524.02]   # sort - this method is used to arrange the list of numbers from ascending to descending order
# q.sort()
# print(q)           # [ 0.23, 1, 1.021, 23, 89.25, 524.02, 5623 ]

# q.sort(reverse=False)
# print(q)                 # [ 0.23, 1, 1.021, 23, 89.25, 524.02, 5623 ]

# q.sort(reverse=True)
# print(q)                  # [ 5623, 524.02, 89.25, 23, 1.021, 1, 0.23 ]


''' sort methods with alphabets'''

# v = ['hello','Python','MS','Md','Code']
# v.sort()
# print(v)      # ['Code', 'MS' , 'Md' , 'hello', 'pyhton']


'''TO KNOW THE ASCII VALUES OF THE ALPHABETS WE USE THE BELOW METHOD TO FIND'''

# print(ord('M'))
# print(ord('X'))
# print(ord('p'))
# print(ord('l'))
# print(ord('a'))
# print(ord('Y'))
# print(ord('e'))
# print(ord('r'))



# print(chr(99))
# print(ord(' '))
# print(chr(118))


# print(chr(0))
# print(chr())
