#! /usr/bin/env python3
# coding: utf-8

import collections, os

def addToFile(what_add, target_file):
	outfile = open(target_file, 'a+')
	outfile.write(what_add)
	outfile.close()


true_chars = 'ёйцукенгшўзх\'фывапролджэячсмітьбю-ЁЙЦУКЕНГШЎЗХФЫВАПРОЛДЖЭЯЧСМІТЬБЮ'
input_file_1 = 'text'
input_file = input_file_1
output_file = 'only_words'
try:
	os.remove(output_file)
except:
	None

title_flag = 0
for idx, line in enumerate(open(input_file)):
	if line == '\n':					#~ skip empty lines
		continue
	if line.startswith('<doc '):		#~ skip markup titles
		title_flag = 1
		continue
	if line.startswith('</doc>'):		#~ skip markup ends
		continue
	if title_flag:						#~ skip titles after markup
		title_flag = 0
		continue
	
	new_line = ''						#~ convert all noncyrillic symbols to space
	for char in line:
		if char not in true_chars:
			new_line += ' '
			continue
		new_line += char
	new_line_list = new_line.split(' ')
	
	new_line_finally = ''				#~ convert multiple spaces to one
	for item in new_line_list:
		if item:
			new_line_finally += item + ' '
	new_line_finally = new_line_finally.rstrip()
	new_line_finally = new_line_finally.lower()
	
	addToFile(new_line_finally + '\n', output_file)

print('Words has been extracted. Generating freq dict...')


#~ =============== create freq dict ===================

input_file_2 = 'only_words'
input_file = input_file_2
output_file = 'freq_dict'
try:
	os.remove(output_file)
except:
	None
c = collections.Counter()

for line in open(input_file):			#~ fill the counter
	new_line = line.rstrip()
	for word in new_line.split():
		c.update([word])

print('Freq dict has been generated. Writing it to file...')

c_sorted = collections.OrderedDict(reversed(sorted(c.items(), key=lambda t: t[1])))

for key in c_sorted.keys():				#~ write to file
	line = '{0} {1}\n'.format(key, c_sorted[key])
	addToFile(line, output_file)


os.remove(input_file_1)
os.remove(input_file_2)
print('Done. The file is {0}'.format(output_file))
