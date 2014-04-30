#!/usr/bin/env python
'''
	pyPassGenCLI v0.01alpha
	By: Adam Koch <crackpot.mytouch@gmail.com>
	http://github.com/adamjkoch/pyPassGen
'''

'''
	pyPassGenCLI:  Command-line version of pyPassGen
	Copyright (C) 2014  Adam Koch

	This program is free software; you can redistribute it and/or
	modify it under the terms of the GNU General Public License
	as published by the Free Software Foundation; either version 2
	of the License, or (at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program; if not, write to the Free Software
	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''
import os, random, string, optparse, sys

pyPassGenCLIVersion = '0.01alpha'

def generate(length, seed, chars):
	random.seed = seed
	return '' . join(random.choice(chars) for i in range(length))

# main code function
def main(argv):
	# setup the option parser
	parser = optparse.OptionParser(
		description='A simple command-line based pseudo secure password generator',
		usage='Usage: %prog <args> <quantity>',
		version='%prog version ' + pyPassGenCLIVersion,
	)
	
	# character settings group
	charSet = optparse.OptionGroup(parser, 'Character Settings')
	charSet.add_option('-l', '--letters', dest='letters', help='don\'t use ascii letters', action='store_false', default=True)
	charSet.add_option('-m', '--mixed', dest='mixed', help='don\'t use mixed case ascii letters', action='store_false', default=True)
	charSet.add_option('-d', '--digits', dest='digits', help='don\'t use digits (0-9)', action='store_false', default=True)
	charSet.add_option('-s', '--special', dest='special', help='don\'t use special characters', action='store_false', default=True)
	charSet.add_option('-S', '--similar', dest='similar', help='remove similar characters', action='store_true', default=False)
	
	# output settings group
	outSet = optparse.OptionGroup(parser, 'Output Settings')
	outSet.add_option('-L', '--length', dest='length', help='password legnth, default: %default', metavar='<int>', action='store', default=15, type='int')
	outSet.add_option('-q', '--quantity', dest='quantity', help='generated password quantity, default: %default', metavar='<int>', action='store', default=1, type='int')
	outSet.add_option('-o', '--output', dest='output', help='pipe output to file', metavar='<filename>', action='store', type='string')
	
	# debug settings group
	debugSet = optparse.OptionGroup(parser, 'Debugging Options')
	debugSet.add_option('-c', '--chars', dest='charlist', help='print character list used and exit', action='store_true', default=False)
	debugSet.add_option('-e', '--seed', dest='seed', help='print the seed used and exit', action='store_true', default=False)
	
	# add options groups
	parser.add_option_group(charSet)
	parser.add_option_group(outSet)
	parser.add_option_group(debugSet)
	
	# parse it!
	(args, opts) = parser.parse_args()

	# do some variable type checks
	if args.length is None or type(args.length) is not int:
		print 'Error: Length (-L, --length) must be an integer.'
		return
	elif args.quantity is None or type(args.quantity) is not int:
		print 'Error: Quantity (-q, --quantity) must be an integer.'
		return
	elif args.output is not None and type(args.output) is not string:
		print 'Error: Output file (-o, --output) must be a valid filename.'
		return
		
	# let's do some generating!
	# generate the seed
	seed = (os.urandom(1024))
	
	# print seed if requested
	if args.seed is True:
		print seed
		return
	
	# character list
	chars = ''
	
	# add letters
	if args.letters is True:
		# lowercase
		chars += string.ascii_lowercase
		# uppercase
		if args.mixed is True:
			chars += string.ascii_uppercase
	
	# add digits
	if args.digits is True:
		chars += string.digits
		
	# add "special" characters
	if args.special is True:
		chars += '!@#$%^&*?'
	
	# remove similar characters
	if args.similar is True:
		chars = chars.replace('i', '') # lowercase i
		chars = chars.replace('I', '') # uppercase i
		chars = chars.replace('l', '') # lowercase L
		chars = chars.replace('O', '') # uppercase O
		chars = chars.replace('0', '') # zero
	
	# print character list if requested
	if args.charlist is True:
		print chars
		
if __name__ == '__main__':
	sys.exit(main(sys.argv))