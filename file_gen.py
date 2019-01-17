#############################################

# Generate text files by sampling characters from a various distributions with mutable stats.

#############################################

import numpy as np
import numpy.random as npr
import os

# Virtual env used: lztest

# Python: 3.5.2

MAX_CHAR = 128

class file_generator():

    def __init__(self, path, max_size=50000000, char_count=1000000, file_count=1):
        self.path = path
        self.max_size = max_size
        self.char_count = char_count
        self.file_count = file_count

        if char_count > self.max_size:
            print("char_count is greater than limit. Increase max_size for object.")

        if not os.access(self.path,os.W_OK):
            print("Path is inaccessible. Object creation failed.")
            del self

    def np_to_str(self, arr):
        arrl = list()
        for elem in [int(el)%MAX_CHAR for el in list(arr)]:
            if elem > 32:
                arrl.append(chr(elem))
            else:
                arrl.append(chr(elem+32))
        #print(max(arrl), min(arrl))

        return ''.join(arrl)

    def poisson(self, lam=64, verbose=1, char_count=None, file_count=None):

        if file_count:
            self.file_count = file_count

        if char_count:
            self.char_count = char_count

        for _ in range(self.file_count):
            if verbose == 1:
                print("Working on file #"+str(_+1)+'.....',end='')

            curr_file = self.path + 'l' + str(lam) + '_pois' + str(_+1) + '_sz' +\
            str(self.char_count/1000000).replace('.','-',1) + '.txt'
            with open(curr_file, 'w',encoding='utf-8') as f:
                pass

            char_count = self.char_count
            while char_count > 10000000:
                curr_count = 10000000;
                char_count -= curr_count
                arr_str = self.np_to_str(npr.poisson(lam=lam, size=curr_count))
                with open(curr_file,'a',encoding='utf-8') as f:
                    f.write(arr_str);

            arr_str = self.np_to_str(npr.poisson(lam=lam, size=char_count))
            with open(curr_file,'a', encoding='utf-8') as f:
                f.write(arr_str);
            if verbose == 1:
                print('Done')
        print(str(self.file_count)+' files created with Poisson distribution.')


    def gaussian(self, mean=64, std=16, verbose=1, char_count=None, file_count=None):

        if file_count:
            self.file_count = file_count

        if char_count:
            self.char_count = char_count

        for _ in range(self.file_count):
            if verbose == 1:
                print("Working on file #"+str(_+1)+'.....',end='')

            curr_file = self.path + 'm'+ str(mean) + '_s' + str(std) + '_gaus' + str(_+1)+'_sz'+\
            str(self.char_count/1000000).replace('.','-',1) + '.txt'
            with open(curr_file, 'w',encoding='utf-8') as f:
                pass

            char_count = self.char_count
            while char_count > 10000000:
                curr_count = 10000000;
                char_count -= curr_count
                arr_str = self.np_to_str(npr.normal(loc=mean, scale=std, size=curr_count))
                with open(curr_file,'a',encoding='utf-8') as f:
                    f.write(arr_str);

            arr_str = self.np_to_str(npr.normal(loc=mean, scale=std, size=char_count))
            with open(curr_file,'a', encoding='utf-8') as f:
                f.write(arr_str);
            if verbose == 1:
                print('Done')
        print(str(self.file_count)+' files created with Gaussian distribution.')

    def uniform(self, low=1, high=127, verbose=1, char_count=None, file_count=None):

        if file_count:
            self.file_count = file_count

        if char_count:
            self.char_count = char_count

        for _ in range(self.file_count):
            if verbose == 1:
                print("Working on file #"+str(_+1)+'.....',end='')

            curr_file = self.path + 'l'+ str(low) + '_h' + str(high) + '_uni' + str(_+1)+'_sz'+\
            str(self.char_count/1000000).replace('.','-',1) + '.txt'
            with open(curr_file, 'w',encoding='utf-8') as f:
                pass

            char_count = self.char_count
            while char_count > 10000000:
                curr_count = 10000000;
                char_count -= curr_count
                arr_str = self.np_to_str(npr.uniform(low=low, high=high, size=curr_count))
                with open(curr_file,'a',encoding='utf-8') as f:
                    f.write(arr_str);

            arr_str = self.np_to_str(npr.uniform(low=low, high=high, size=char_count))
            with open(curr_file,'a', encoding='utf-8') as f:
                f.write(arr_str);
            if verbose == 1:
                print('Done')
        print(str(self.file_count)+' files created with uniform distriubution.')


    def exponential(self, scale=64, verbose=1, char_count=None, file_count=None):

        if file_count:
            self.file_count = file_count

        if char_count:
            self.char_count = char_count

        for _ in range(self.file_count):
            if verbose == 1:
                print("Working on file #"+str(_+1)+'.....',end='')

            curr_file = self.path + 'sc'+ str(scale) + '_exp' + str(_+1)+'_sz'+\
            str(self.char_count/1000000).replace('.','-',1) + '.txt'
            with open(curr_file, 'w',encoding='utf-8') as f:
                pass

            char_count = self.char_count
            while char_count > 10000000:
                curr_count = 10000000;
                char_count -= curr_count
                arr_str = self.np_to_str(npr.exponential(scale=scale, size=curr_count))
                with open(curr_file,'a',encoding='utf-8') as f:
                    f.write(arr_str);

            arr_str = self.np_to_str(npr.exponential(scale=scale, size=char_count))
            with open(curr_file,'a', encoding='utf-8') as f:
                f.write(arr_str);
            if verbose == 1:
                print('Done')
        print(str(self.file_count)+' files created with exponential distriubution.')
