 # Description: This script practices opening, writing, and appending to files

#  Create and close about_me.txt
f = open('about_me.txt', 'a')
f.close()


#  Reopen and write perfect night out
f = open('about_me.txt', 'a')

f.write('\n')
f.write('Perfect night out:\n')
f.write('I would go to a rooftop restaurant for dinner,\n')
f.write('then catch a live jazz concert downtown,\n')
f.write('and end the night with a walk along the waterfront.\n')
f.close()


