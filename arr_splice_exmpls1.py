--Various List Splicing commands. 

>>> print 'test-01'
>>>  'test-01' [ 0 ]
 
>>> 'test-01'[ 0 ]
't'
>>> 'test-01'[ -]
>>> 'test-01'[ -1 ]
'1'
>>> 'test-01'[ -2 ]
'0'
>>> 'test-01'[ -4 ]
't'
>>> 'test-01'[ -5 ]
's'
>>> 'test-01'[ -3, ]

>>> 'test-01'[ 1, ]

>>> 'test-01'[ 1: ]
'est-01'
>>> 'test-01'[ 1:3 ]
'es'
>>> 'test-01'[ 1:4 ]
'est'
>>> 'test-01'[ :4 ]
'test'
>>> 'test-01'[ :-4]
'tes'
>>> 'test-01'[ :-4 ]
'tes'
>>> 'test-01'[ -4: ]
't-01'
>>> 'test-01'[ -4: ]
't-01'
>>> len ( 'test-01'[ -4: ])
4
>>> len ( 'test-01'[ -4: ])
4
