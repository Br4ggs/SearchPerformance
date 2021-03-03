class Node:
    def __init__(self, word):
        self.word = word
        self.frequency = 0
        self.left = None
        self.right = None

# TODO: if time allows (probably not)
def Generate_frequency_map_from_word_list(word_list):
    return -1

def Generate_binary_tree_from_word_list(word_list):
    root_node = Node(word_list[0])
    for word in word_list:
        current_node = root_node
        while current_node.word != word:
            if word < current_node.word:
                if current_node.left == None:
                    current_node.left = Node(word)
                current_node = current_node.left
            else:
                if current_node.right == None:
                    current_node.right = Node(word)
                current_node = current_node.right
        current_node.frequency += 1
    return root_node

def Linear_count(word, word_list):
    search_word = word.lower()
    frequency = 0
    for a_word in word_list:
        if search_word == a_word:
            frequency += 1
    return frequency

def Binary_count(word, binary_tree):
    node = binary_tree
    while node != None and node.word != word:
        if word < node.word:
            node = node.left
        else:
            node = node.right
    if node == None:
        return 0
    else:
        return node.frequency