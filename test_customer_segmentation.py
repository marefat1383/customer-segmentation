import unittest

from customer_segmentation import assign_segment


class CustomerSegmentationTests(unittest.TestCase):
    def test_valid_customer_gets_a_segment(self):
        self.assertIn(assign_segment(1200, 18), range(3))

    def test_invalid_spend_is_rejected(self):
        with self.assertRaises(ValueError):
            assign_segment(0, 18)


if __name__ == "__main__":
    unittest.main()
