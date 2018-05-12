# from __future__ import print_function

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print('\n'.join(map(''.join, zip(*grid))))

for j in range(len(grid[0])):
 	for i in range(len(grid)):
 		print 'inner %s' % j
 		print 'outer %s' % i
 		print grid[i][j],
  	print '\n'