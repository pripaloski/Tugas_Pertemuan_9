from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Course, CourseMember
from http import HTTPStatus

# Create your tests here.

class TestUnitCases(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.course = Course.objects.create(
            name="Python Course",
            description="Learn Python Programming",
            price=100.00,
            teacher="John Doe"
        )

    def test_course_creation(self):
        self.assertEqual(self.course.name, "Python Course")
        self.assertEqual(self.course.teacher, "John Doe")

    def test_course_member(self):
        member = CourseMember.objects.create(
            course=self.course,
            user_id=self.user.id,
            roles="student"
        )
        self.assertTrue(self.course.is_member(self.user.id))

class TestIntegrationCases(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.course = Course.objects.create(
            name="Test Course",
            description="Test Description",
            price=50.00,
            teacher="Jane Doe"
        )

    def test_course_access_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_course_access_unauthenticated(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)
