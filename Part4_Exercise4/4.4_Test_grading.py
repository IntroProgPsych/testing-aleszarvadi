import unittest
from grading import grade_student


class TestGradeStudent(unittest.TestCase):
    # TODO:
    # - Write tests for typical values:
    #   * 95 -> "A"
    #   * 85 -> "B"
    #   * 75 -> "C"
    #   * 65 -> "D"
    #   * 30 -> "F"
    # - Write tests for boundary values:
    #   * 90 -> "A", 89 -> "B"
    #   * 80 -> "B", 79 -> "C"
    #   * 70 -> "C", 69 -> "D"
    #   * 60 -> "D", 59 -> "F"
    # - Write tests that check ValueError for:
    #   * score < 0
    #   * score > 100
    # - Use assertEqual for grades and assertRaises for invalid scores.
    #
    # write your tests here
  
    def test_grade_student(self):
        self.assertEqual(grade_student(95), "A")
    
        self.assertEqual(grade_student(85), "B")
    
        self.assertEqual(grade_student(75), "C")
    
        self.assertEqual(grade_student(65), "D")
    def test_grade_student(self):
        self.assertEqual(grade_student(30), "F")

    def test_grade_student(self):
        self.assertEqual(grade_student(90), "A")
    def test_grade_student(self):
        self.assertEqual(grade_student(89), "B")
    def test_grade_student(self):
        self.assertEqual(grade_student(80), "B")
    def test_grade_student(self):
        self.assertEqual(grade_student(79), "C")
    def test_grade_student(self):
        self.assertEqual(grade_student(70), "C")
    def test_grade_student(self):
        self.assertEqual(grade_student(69), "D")
    def test_grade_student(self):
        self.assertEqual(grade_student(60), "D")
    def test_grade_student(self):
        self.assertEqual(grade_student(30), "F")

    def test_grade_student(self):
        with self.assertRaises(ValueError):
             grade_student(-1)

    def test_grade_student(self):
        with self.assertRaises(ValueError):
             grade_student(101)

if __name__ == "__main__":
    unittest.main() 
