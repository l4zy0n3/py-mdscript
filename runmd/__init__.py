from argparse import ArgumentParser
from runmd.runmd import export_file_as_script

parser = ArgumentParser()
__version__ = "0.0.1.dev0"

def initialize_arguments():
	config = {}
	parser.add_argument("-i", "--input", dest="infile", help="Input file", required=True)
	parser.add_argument("-o", "--output", dest="outfile", help="Output file", required=True)
	args, unknowns = parser.parse_known_args()
	config['infile'] = args.infile
	config['outfile'] = args.outfile
	return config
def run_as_script():
	config = initialize_arguments()
	export_file_as_script(config.get('infile'), config.get('outfile'))