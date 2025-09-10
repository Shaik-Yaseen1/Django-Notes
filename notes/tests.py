from django.test import TestCase
from .models import Note

class NoteModelTest(TestCase):
    def test_create_note(self):
        n = Note.objects.create(title='Test', content='Hello')
        self.assertEqual(str(n), 'Test')
        self.assertIsNotNone(n.created_at)
