#!/usr/bin/env python
'''
	pyPassGen v0.01alpha
	By: Adam Koch <crackpot.mytouch@gmail.com>
	http://github.com/adamjkoch/pyPassGen
'''

'''
	pyPassGen: A simple secure password generator written in Python.
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
import os, random, string, optparse

# the "guts"
def main(argv):
	# the characters we'll use

	# set up the option parser
	parser = optparse.OptionParser('usage: %prog [options] length')
	parser.add_option('-s', '--nospecial', action='store_true', dest='nospecial', help='Do not use special characters.')
	parser.add_option('-l', '--lowercase', action='store_true', dest='lowercase', help='Use all lowercase characters.')
	parser.add_option('-u', '--uppercase', action='store_true', dest='uppercase', help='Use only uppercase.')
	parser.add_option('-n', '--nonumbers', action='store_true', dest='nonumbers', help='Do not use numbers.')
	parser.add_option('-q', '--unique', action='store_false', dest='unique', help='Allow similar looking characters.')

# generate the password using the given length and characters
def genpwd(length, chars):
	random.seed = (os.urandom(1024))
	return '' . join(random.choice(chars) for i in range(length))

	
if __name__ == '__main__':
	sys.exit(main(sys.argv))