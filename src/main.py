import argparse

def process_cli(argc, argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('--add-recipie','-a',help="This to add recipie")
	parser.add_argument('--search','-s',help="This is to search recipies")
	args = parser.parse_args(argv[1:])
	print(args)	
