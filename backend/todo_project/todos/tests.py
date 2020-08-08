from django.test import TestCase
from .models import Todo
# Create your tests here.

class  TodoModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='First Todo', body='a body here')

    def test_title_contents(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'First Todo')    

    def test_body_contents(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name, 'a body here')       