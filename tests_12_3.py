import runner as r
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = r.Runner("Вася")
        for i in range(0,10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = r.Runner("Петя")
        for i in range(0,10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner_3 = r.Runner("Игорь")
        runner_4 = r.Runner("Петя")

        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.runner_1 = r.Runner("Усэйн", 10)
        self.runner_2 = r.Runner("Андрей", 9)
        self.runner_3 = r.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run_1_3(self):
        test_1_3 = r.Tournament(90, self.runner_1, self.runner_3)
        results_1_3 = test_1_3.start()

        run_2 = ""
        for key, value in results_1_3.items():
            run_2 += str(key) + ": " + str(value) + " "
        TournamentTest.all_results.append(run_2)

        self.assertTrue(results_1_3[2], 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run_2_3(self):
        test_2_3 = r.Tournament(90, self.runner_2, self.runner_3)
        results_2_3 = test_2_3.start()

        run_3 = ""
        for key, value in results_2_3.items():
            run_3 += str(key) + ": " + str(value) + " "
        TournamentTest.all_results.append(run_3)

        self.assertTrue(results_2_3[2], 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run_1_2_3(self):
        test_1_2_3 = r.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results_1_2_3 = test_1_2_3.start()

        run_3 = ""
        for key, value in results_1_2_3.items():
            run_3 += str(key) + ": " + str(value) + " "
        TournamentTest.all_results.append(run_3)

        self.assertTrue(results_1_2_3[2], 'Ник')



if __name__ == "__main__":
    unittest.main()