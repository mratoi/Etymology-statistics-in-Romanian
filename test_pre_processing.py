
from unittest import TestCase, main
import pre_processing as tested


class Test_Meth(TestCase):
    def test_get_list_lemma(self):
        """
        Test the output of the function for the given text:
        """
        text = " acest test pierde timp "
        result = tested.get_list_lemma(text)
        target = ["acest", "test", "pierde", "timp"]
        self.assertIsInstance(result, list, "Required type of output is list")
        self.assertEqual(result, target)

       

if __name__ == '__main__':
    main()