import runner as r
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = r.Runner("Вася")
        for i in range(0,10):
            runner.walk()
        self.assertEqual(runner.distance, 50)



    def test_run(self):
        runner = r.Runner("Петя")
        for i in range(0,10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_3 = r.Runner("Игорь")
        runner_4 = r.Runner("Петя")

        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)



if __name__ == "__main__":
    unittest.main()