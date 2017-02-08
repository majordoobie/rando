"""
understanding list comprehension A.K.A. black fucking magic.

"""

numbers = [1, 2, 3, 4, 5]

doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)


doubled_odds = [n * 2 for n in numbers if n % 2 ==1 ]   #voodoo shit

  1) Grab your items from the list; for n in numbers 
  2) run it through a criteria; n % 2 == 1 
  3) if criteria is True add it to the last function in this case multiply that shit by 2, this is also where it gets appended to double


wordlist = [x.upper() for x in list(open('file', 'r').readlines if 'u' in x]

  1) so we grab our items for our list, so we open a file and read each line every line is it's own item in that list. 
  2) take the first item and check if u is in it
  3) if true run it through the last function which is upper() method. then gets appended to wordlist 
           


