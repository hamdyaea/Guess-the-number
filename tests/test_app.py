# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
import importlib.util
from pathlib import Path
import unittest
spec=importlib.util.spec_from_file_location("application",Path(__file__).resolve().parents[1]/"GuessTheNumber.py")
app=importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)
class Tests(unittest.TestCase):
    def test_comparison(self):
        self.assertEqual(app.compare(10,10),"Correct!")
        self.assertEqual(app.compare(1,10),"Too low")
        self.assertEqual(app.compare(20,10),"Too high")
        with self.assertRaises(ValueError):app.compare(0,10)
    def test_gui(self):
        win=app.GuessApp()
        try:
            win.secret=7
            win.value.set("7")
            win.guess()
            self.assertIn("Correct!",win.message.get())
            self.assertEqual(win.count,1)
        finally:win.destroy()

if __name__=="__main__":unittest.main()
