import os

def getFiles(dir):
	output = []
	for file in os.listdir(dir):
		path = dir + os.sep + file
		if os.path.isdir(path):
			output += getFiles(path)
		else:
			if file.endswith('.py'):
				output.append(path)
	return output
	
files = getFiles('source')
all = []
header = ''
footer = ''
priority = []
priority_files = [
	'LevelSpecial.py'
]
for file in files:
	c = open(file, 'rt')
	contents = c.read()
	c.close()
	
	if file == 'source' + os.sep + 'main.py':
		footer = contents
	elif file == 'source' + os.sep + 'header.py':
		header = contents
	elif file.split(os.sep)[-1] in priority_files:
		priority.append(contents)
	else:
		all.append(contents)

all = [header] + priority + all + [footer]

output = '\n\n'.join(all)

c = open('rungame.py', 'wt')
c.write(output)
c.close()
