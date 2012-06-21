'''
	distances.py
	
	Copyright (c) 2012, gnTEAM, School of Computer Science, University of Manchester.
	All rights reserved. This program and the accompanying materials
	are made available under the terms of the GNU General Public License.
	
	authors: Michele Filannino
	email:  filannim@cs.man.ac.uk
	
	Distances is a collection of distance metrics between strings.
	For details, see www.cs.man.ac.uk/~filannim/
'''
 
#!/usr/bin/python
'''This module contains different useful string function.
'''

def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in xrange(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in xrange(-1,lenstr2+1):
        d[(-1,j)] = j+1
 
    for i in xrange(lenstr1):
        for j in xrange(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
 
    return d[lenstr1-1,lenstr2-1]
    
def levenshtein_distance(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
    return current[n]
    
def main():
	dist1 = damerau_levenshtein_distance("12-13-2010", "12-13-2010")
	print "Damerau Levenshtein: " + str(dist1)
	dist2 = levenshtein_distance("12-13-2010", "12-13-2010")
	print "Levenshtein: " + str(dist2)
	
if __name__ == '__main__':
	main()
