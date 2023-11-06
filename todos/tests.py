from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="first todo",
            body="a body of text"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "first todo")
        self.assertEqual(str(self.todo), "first todo")
        self.assertEqual(self.todo.body, "a body of text")

    def test_api_listview(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        # response = self.client.get(
        #     reverse("todo_detail", kwargs={"pk": self.todo.id})
        # )
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "first todo")
