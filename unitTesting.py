import unittest
import funcNextCafe as cal


class Testing(unittest.TestCase):

    def test_buyCoffee(self):
        for i in range(1, 1):
            self.run(cal.buyCoffee())

    def test_addCoffee(self):
        for i in range(1, 1):
            self.run(cal.addCoffee())

    def test_updateCoffee(self):
        for i in range(1, 1):
            self.run(cal.updateCoffee())

    def test_deleteCoffee(self):
        for i in range(1, 1):
            self.run(cal.deleteCoffee())

if __name__ == "__main__":
    unittest.main()
