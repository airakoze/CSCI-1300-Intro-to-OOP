# Authors: andyflorian.irakoze@slu.edu, harishaan.suthan@slu.edu

dnaString = input('Enter a DNA sequence: ') # DNA String

pattern = input('Enter the pattern: ') # Forward Pattern

patternIndex = dnaString.find(pattern) # Pattern index in the DNA String

patternCharNum = len(pattern) # Length of the Pattern

prefix = dnaString[:patternIndex] # Subsection of the DNA String from the beginning to the Pattern Index

print('Prefix:', prefix)

marker = pattern 

print('Marker:', marker)

reversedMarker = marker[::-1] # Reversing the marker

searchMarkerIndex = dnaString[(patternIndex + patternCharNum):] # DNA String subsection used to find the reversed marker

reversedMarkerIndex = searchMarkerIndex.find(reversedMarker) # Reverse Marker Index

middle = searchMarkerIndex[:reversedMarkerIndex] # Part between the marker and the reversed marker

print('Middle:', middle)

reversedMiddle = middle[::-1]

print('Reversed Middle:', reversedMiddle)

print('Reversed Marker:', reversedMarker)

suffix = searchMarkerIndex[(reversedMarkerIndex + patternCharNum):]

print('Suffix:', suffix)

result = prefix + marker + reversedMiddle + reversedMarker + suffix

print('Result:', result)
