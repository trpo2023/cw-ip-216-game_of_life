import unittest
import main
from main import game_scene
from cs_func import cell_status
from dl_func import draw_label
from inspect import signature #библиотека для подсчёта кол-ва аргументов функции

class GameTest(unittest.TestCase):

    def test_parameters(self):
        self.assertEqual(main.tile, 10)
        self.assertEqual(main.FPS, 12)

    def test_exit(self):
        self.assertRaises(SystemExit)

    def test_size(self):
        self.assertEqual(main.resolution, (1280, 720))

    def test_func_arg(self):
        mm_arg = signature(main.main_menu)
        gs_arg = signature(main.game_scene)
        cs_arg = signature(cell_status)
        dl_arg = signature(draw_label)
        self.assertEqual(len(mm_arg.parameters), 0)
        self.assertEqual(len(gs_arg.parameters), 3)
        self.assertEqual(len(cs_arg.parameters), 3)
        self.assertEqual(len(dl_arg.parameters), 6)
    
    def test_game_running(self):
        self.assertTrue(main.game_scene)

    def test_array_type(self):
        self.assertTrue(main.main_menu)

    def test_draw_value(self):
        self.assertTrue(draw_label)

if __name__ == '__main__':
    unittest.main()
