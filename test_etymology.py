

from unittest import TestCase, main
import etymology


class Test_Methd(TestCase):
    def test_get_etymology(self):
        """
        Test the function
        """
        lemma_list = ["ţelină", "șmecher" ,"urdă", "răboj","taraf", "veni"]
        result = etymology.get_etymology(lemma_list)
        target = (['veni'], ['răboj'], ['urdă'], ['ţelină'], ['taraf'], ['șmecher'])
        self.assertIsInstance( result, tuple, "Returns a tuple.")
        self.assertEqual(result, target)


if __name__ == '__main__':
    main()