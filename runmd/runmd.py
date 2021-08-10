import mistletoe
from bs4 import BeautifulSoup

def export_file_as_script(infile, outfile):
	with open(infile, 'r') as f:
		soup = BeautifulSoup(mistletoe.markdown(f.read()), 'html.parser')
	with open(outfile, 'w') as f:
		f.write("#!/usr/bin/env python3\n")
		for codeblock in soup.find_all('code'):
			f.write(codeblock.string)