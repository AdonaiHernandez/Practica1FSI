from unittest import TestCase
import search

class TestSearch(TestCase):
    def setUp(self):
        # Este código se ejecutará antes de cada test, y nos ayuda a preparar
        # nuestro un escenario genérico sobre el que ejecutar nuestro testing.
        self.problem = search.GPSProblem('A', 'B', search.romania)

    def test_bfs(self):
        self.assertEqual(search.breadth_first_graph_search(self.problem)[0].path_cost, 450)

    def test_dfs(self):
        self.assertEqual(search.depth_first_graph_search(self.problem)[0].path_cost, 733)

    def test_branch_and_bound(self):
        self.assertEqual(search.branch_and_bound_search(self.problem)[0].path_cost, 418)

    def test_branch_and_bound_substimation(self):
        self.assertEqual(search.branch_and_bound_search(self.problem)[0].path_cost, 418)