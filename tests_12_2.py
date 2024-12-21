import runner as r
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = r.Runner("Усэйн", 10)
        self.runner_2 = r.Runner("Андрей", 9)
        self.runner_3 = r.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    def test_run_1_3(self):
        test_1_3 = r.Tournament(90, self.runner_1, self.runner_3)
        results_1_3 = test_1_3.start()

        run_2 = ""
        for key, value in results_1_3.items():
            run_2 += str(key) + ": " + str(value) + " "
        TournamentTest.all_results.append(run_2)

        self.assertTrue(results_1_3[2], 'Ник')


    def test_run_2_3(self):
        test_2_3 = r.Tournament(90, self.runner_2, self.runner_3)
        results_2_3 = test_2_3.start()

        run_3 = ""
        for key, value in results_2_3.items():
            run_3 += str(key) + ": " + str(value) + " "
        TournamentTest.all_results.append(run_3)

        self.assertTrue(results_2_3[2], 'Ник')

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