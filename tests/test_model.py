# pylint: skip-file

import unittest
import ltk


class TodoModel(ltk.LocalStorageModel):
    note: str = ""
    completed: bool = False
    suggestion: str = ""



class TestTodoModel(unittest.TestCase):
    def setUp(self):
        self.todo = TodoModel()

    def test_suggestion_type(self):
        self.assertIsInstance(self.todo.suggestion, ltk.ModelAttribute)

    def test_note_type(self):
        self.assertIsInstance(self.todo.note, ltk.ModelAttribute)

    def test_default_values(self):
        self.assertEqual(self.todo.note, "")
        self.assertEqual(self.todo.completed, False)
        self.assertEqual(self.todo.suggestion, "")

    def test_note(self):
        test_note = "Buy groceries"
        self.todo.note = test_note
        self.assertEqual(self.todo.note, test_note)

    def test_completed(self):
        self.assertFalse(self.todo.completed)
        self.todo.completed = True
        self.assertTrue(self.todo.completed)

    def test_suggestion(self):
        test_suggestion = "Don't forget milk"
        self.todo.suggestion = test_suggestion
        self.assertEqual(self.todo.suggestion, test_suggestion)


if __name__ == '__main__':
    unittest.main()

