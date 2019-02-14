import argparse
import sys


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--x' , type=float, default=1.0,
		help = 'Mi az elso szam ? ')
	parser.add_argument('--y' , type=float, default=5.0,
		help = 'Mi az masodik szam ? ')
	parser.add_argument('--operation' , type=str, default='osszeadas',
		help = 'Mi a muvelet ? (osszeadas, kivonas, szorzas, osztas) ')

	args = parser.parse_args()
	sys.stdout.write(str(calc(args)))

def calc( args ):
	#operation = args.operation
	if args.operation =='osszeadas':
		return args.x + args.y
	elif args.operation =='kivonas':
		return args.x - args.y
	elif args.operation =='szorzas':
		return args.x * args.y
	elif args.operation =='osztas':
		return args.x / args.y

#operation( 7 , 9 , 'osszeadas')
#print(operation)

if __name__ == '__main__':
	main()