from unittest import TestCase
import search

class TestSearchAB(TestCase):
    def setUp(self):
        self.problem = search.GPSProblem('A', 'B', search.romania)

    def test_bfs(self):
        bfs_res = search.breadth_first_graph_search(self.problem)

        self.assertEqual(bfs_res[0].path_cost, 450)
        self.assertEqual(bfs_res[1], 16)
        self.assertEqual(bfs_res[2], 21)

    def test_dfs(self):
        dfs_res = search.depth_first_graph_search(self.problem)
        self.assertEqual(dfs_res[0].path_cost, 733)
        self.assertEqual(dfs_res[1], 10)
        self.assertEqual(dfs_res[2], 18)

    def test_branch_and_bound(self):
        bab_res = search.branch_and_bound_search(self.problem)
        self.assertEqual(bab_res[0].path_cost, 418)
        self.assertEqual(bab_res[1], 24)
        self.assertEqual(bab_res[2], 31)

    def test_branch_and_bound_substimation(self):
        babs_res = search.branch_and_bound_substimation_search(self.problem)
        self.assertEqual(babs_res[0].path_cost, 418)
        self.assertEqual(babs_res[1], 6)
        self.assertEqual(babs_res[2], 16)


class TestSearchOE(TestCase):
    def setUp(self):
        self.problem = search.GPSProblem('O', 'E', search.romania)

    def test_bfs(self):
        bfs_res = search.breadth_first_graph_search(self.problem)

        self.assertEqual(bfs_res[0].path_cost, 730)
        self.assertEqual(bfs_res[1], 43)
        self.assertEqual(bfs_res[2], 45)

    def test_dfs(self):
        dfs_res = search.depth_first_graph_search(self.problem)
        self.assertEqual(dfs_res[0].path_cost, 698)
        self.assertEqual(dfs_res[1], 31)
        self.assertEqual(dfs_res[2], 41)

    def test_branch_and_bound(self):
        bab_res = search.branch_and_bound_search(self.problem)
        self.assertEqual(bab_res[0].path_cost, 698)
        self.assertEqual(bab_res[1], 40)
        self.assertEqual(bab_res[2], 43)

    def test_branch_and_bound_substimation(self):
        babs_res = search.branch_and_bound_substimation_search(self.problem)
        self.assertEqual(babs_res[0].path_cost, 698)
        self.assertEqual(babs_res[1], 15)
        self.assertEqual(babs_res[2], 32)


class TestSearchGZ(TestCase):
    def setUp(self):
        self.problem = search.GPSProblem('G', 'Z', search.romania)

    def test_bfs(self):
        bfs_res = search.breadth_first_graph_search(self.problem)

        self.assertEqual(bfs_res[0].path_cost, 615)
        self.assertEqual(bfs_res[1], 34)
        self.assertEqual(bfs_res[2], 41)

    def test_dfs(self):
        dfs_res = search.depth_first_graph_search(self.problem)
        self.assertEqual(dfs_res[0].path_cost, 1284)
        self.assertEqual(dfs_res[1], 21)
        self.assertEqual(dfs_res[2], 32)

    def test_branch_and_bound(self):
        bab_res = search.branch_and_bound_search(self.problem)
        self.assertEqual(bab_res[0].path_cost, 583)
        self.assertEqual(bab_res[1], 34)
        self.assertEqual(bab_res[2], 41)

    def test_branch_and_bound_substimation(self):
        babs_res = search.branch_and_bound_substimation_search(self.problem)
        self.assertEqual(babs_res[0].path_cost, 583)
        self.assertEqual(babs_res[1], 12)
        self.assertEqual(babs_res[2], 26)


class TestSearchND(TestCase):
    def setUp(self):
        self.problem = search.GPSProblem('N', 'D', search.romania)

    def test_bfs(self):
        bfs_res = search.breadth_first_graph_search(self.problem)

        self.assertEqual(bfs_res[0].path_cost, 765)
        self.assertEqual(bfs_res[1], 26)
        self.assertEqual(bfs_res[2], 32)

    def test_dfs(self):
        dfs_res = search.depth_first_graph_search(self.problem)
        self.assertEqual(dfs_res[0].path_cost, 1151)
        self.assertEqual(dfs_res[1], 19)
        self.assertEqual(dfs_res[2], 31)

    def test_branch_and_bound(self):
        bab_res = search.branch_and_bound_search(self.problem)
        self.assertEqual(bab_res[0].path_cost, 765)
        self.assertEqual(bab_res[1], 26)
        self.assertEqual(bab_res[2], 32)

    def test_branch_and_bound_substimation(self):
        babs_res = search.branch_and_bound_substimation_search(self.problem)
        self.assertEqual(babs_res[0].path_cost, 765)
        self.assertEqual(babs_res[1], 12)
        self.assertEqual(babs_res[2], 23)


class TestSearchMF(TestCase):
    def setUp(self):
        self.problem = search.GPSProblem('M', 'F', search.romania)

    def test_bfs(self):
        bfs_res = search.breadth_first_graph_search(self.problem)

        self.assertEqual(bfs_res[0].path_cost, 520)
        self.assertEqual(bfs_res[1], 23)
        self.assertEqual(bfs_res[2], 31)

    def test_dfs(self):
        dfs_res = search.depth_first_graph_search(self.problem)
        self.assertEqual(dfs_res[0].path_cost, 928)
        self.assertEqual(dfs_res[1], 18)
        self.assertEqual(dfs_res[2], 29)

    def test_branch_and_bound(self):
        bab_res = search.branch_and_bound_search(self.problem)
        self.assertEqual(bab_res[0].path_cost, 520)
        self.assertEqual(bab_res[1], 27)
        self.assertEqual(bab_res[2], 36)

    def test_branch_and_bound_substimation(self):
        babs_res = search.branch_and_bound_substimation_search(self.problem)
        self.assertEqual(babs_res[0].path_cost, 520)
        self.assertEqual(babs_res[1], 14)
        self.assertEqual(babs_res[2], 25)