import unittest
from search import *

test_list = ["the", "eager", "fox", "dropped", "the", "ball", "in", "the", "case", "of", "the", "ball", "case"]

class TestSearch(unittest.TestCase):
    def test_Node_initializes_with_correct_values(self):
        node = Node("test")
        self.assertEqual(node.word, "test")
        self.assertEqual(node.frequency, 0)
        self.assertEqual(node.left, None)
        self.assertEqual(node.right, None)

    def test_Linear_count_returns_word_count(self):
        count = Linear_count("case", test_list)
        self.assertEqual(count, 2)
    
    def test_Linear_count_returns_zero_for_word_not_in_list(self):
        count = Linear_count("clever", test_list)
        self.assertEqual(count, 0)
    
    def test_Generate_binary_tree_from_word_list_returns_correct_values(self):
        the_node = Generate_binary_tree_from_word_list(test_list)
        self.assertEqual(the_node.word, "the")
        self.assertEqual(the_node.frequency, 4)
        self.assertIsNone(the_node.right)

        eager_node = the_node.left
        self.assertEqual(eager_node.word, "eager")
        self.assertEqual(eager_node.frequency, 1)

        dropped_node = eager_node.left
        self.assertEqual(dropped_node.word, "dropped")
        self.assertEqual(dropped_node.frequency, 1)
        self.assertIsNone(dropped_node.right)

        ball_node = dropped_node.left
        self.assertEqual(ball_node.word, "ball")
        self.assertEqual(ball_node.frequency, 2)
        self.assertIsNone(ball_node.left)

        case_node = ball_node.right
        self.assertEqual(case_node.word, "case")
        self.assertEqual(case_node.frequency, 2)
        self.assertIsNone(case_node.left)
        self.assertIsNone(case_node.right)

        fox_node = eager_node.right
        self.assertEqual(fox_node.word, "fox")
        self.assertEqual(fox_node.frequency, 1)
        self.assertIsNone(fox_node.left)

        in_node = fox_node.right
        self.assertEqual(in_node.word, "in")
        self.assertEqual(in_node.frequency, 1)
        self.assertIsNone(in_node.left)

        of_node = in_node.right
        self.assertEqual(of_node.word, "of")
        self.assertEqual(of_node.frequency, 1)
        self.assertIsNone(of_node.left)
        self.assertIsNone(of_node.right)
    
    def test_Binary_count_returns_word_count(self):
        tree = Generate_binary_tree_from_word_list(test_list)
        count = Binary_count("case", tree)
        self.assertEqual(count, 2)

    def test_Binary_count_returns_zero_for_word_not_in_tree(self):
        tree = Generate_binary_tree_from_word_list(test_list)
        count = Binary_count("clever", tree)
        self.assertEqual(count, 0)

if __name__ == '__main__':
    unittest.main()