import pandas as pd
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year':  [2000, 2001, 2002, 2001, 2002, 2003],
         'pop':  [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
frame.set_index('year')
frame.head()

# Columns can be referenced using Dictionary notation
# or using attribute

frame['state']
frame.state

# Specify order / selection of columns
rearranged = pd.DataFrame(data, columns=['year', 'pop'])


