# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""First assignment for the CMEPDA course, 2022/23.
"""

import argparse
import string
import time
import math


def process(file_path, hist):
    freqs = {}
    letters = string.ascii_lowercase
    for letter in letters:
        freqs[letter] = 0
    rfreqs = freqs
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        text = input_file.read()
    for ch in text.lower():
        if ch in letters:
            freqs[ch] += 1
    sum = 0
    for letter in letters:
        sum += freqs[letter]
    for letter in letters:
        rfreqs[letter] = freqs[letter]/sum
    if hist:
        for letter in letters:
            print(f'{letter} ', end='')
            for i in range(math.ceil(rfreqs[letter]*1000)):
                print('\N{FULL BLOCK}', end='')
            print("\n", end='')
    else:
        print('{:<10}{:>10}'.format('Letter', 'Frequecy'))
        for letter in letters:
            print('{:<10}{:>10.3%}'.format(letter, rfreqs[letter]))


if __name__ == '__main__':
    start = time.time()
    parser = argparse.ArgumentParser(description='Print the relative frequence of each letter of the alphabet (without distinguishing between lower and upper case) in a book.')
    parser.add_argument('infile', type=str, help='path to the input file')
    parser.add_argument('--histogram', action='store_true', help='display a histogram of the frequencies')
    args = parser.parse_args()
    process(args.infile, args.histogram)
    elapsed = time.time() - start
    print(f"It took {elapsed} seconds")
