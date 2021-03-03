from lorem_text import lorem

import time
import numpy as np
import matplotlib.pyplot as plt
from search import *

def TextFile_to_list(file_name):
    with open(file_name) as f:
        word_list = [word.strip('.,!?').lower() for line in f for word in line.split()]
        return word_list

def Print_tree(node):
    print("word: " + node.word)
    print("frequency: " + str(node.frequency))
    if node.left != None:
        Print_tree(node.left)
    if node.right != None:
        Print_tree(node.right)

samples = 200
increment = 1000
N = 25

N_samples = N-1

linear_times = list()
binary_times = list()

for iteration in range(0, samples + N_samples):
    text = lorem.words(iteration * increment)

    words = [word.strip('.,!?\n').lower() for word in text.split(" ")]
    binary_tree = Generate_binary_tree_from_word_list(words)
    word = lorem.words(1)

    start_time = time.perf_counter()
    Linear_count(word, words)
    total_time = (time.perf_counter() - start_time)
    linear_times.append(total_time)
    
    start_time = time.perf_counter()
    Binary_count(word, binary_tree)
    total_time = (time.perf_counter() - start_time)
    binary_times.append(total_time)

x = np.linspace(0, samples*increment, samples)

linear_times_filtered = np.convolve(linear_times, np.ones(N)/N, mode='valid')
binary_times_filtered = np.convolve(binary_times, np.ones(N)/N, mode='valid')

del binary_times[-N_samples:]
del linear_times[-N_samples:]

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, linear_times, 'tab:red')
axs[0, 0].set_title("linear times")
axs[1, 0].plot(x, linear_times_filtered, 'tab:green')
axs[1, 0].set_title("linear times filtered")
axs[0, 1].plot(x, binary_times, 'tab:blue')
axs[0, 1].set_title("binary times")
axs[1, 1].plot(x, binary_times_filtered, 'tab:orange')
axs[1, 1].set_title("binary times filtered")
fig.tight_layout()

plt.show()
