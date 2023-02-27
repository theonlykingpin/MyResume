from django.test import RequestFactory, TestCase
from .models import Specification, Experience, Education
from .views import Landing, Resume
from core.settings import BASE_DIR


class TestServer(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.specification = Specification.objects.create(
            full_name='test full name',
            title='test title',
            cv=str(BASE_DIR) + '\\static\\cv\\resume.pdf',
            picture=str(BASE_DIR) + '\\static\\image\\avatar.jpg',
            about='some about text',
            age=30,
            email='test@gmail.com',
            email2='test@gmail.com',
            phone='09164442233',
            address='some addresses',
            python=50,
            django=50,
            drf=50,
            git=50,
            database=50,
            docker=50,
            telegram='some addresses',
            linkedin='some addresses',
            instagram='some addresses',
            github='some addresses',
            twitter='some addresses',
            stackoverflow='some addresses',
            gitlab='some addresses',
            discord='some addresses',
            reddit='some addresses',
            quora='some addresses'
        )
        self.experience = Experience.objects.create(
            specification=self.specification,
            title='some title',
            company='some company',
            description='some description',
            start_date='2022-12-01',
            end_date='2022-12-05'
        )
        self.education = Education.objects.create(
            specification=self.specification,
            title='some titles',
            fromm='some addreeses',
            start_date='2022-12-01',
            end_date='2022-12-05'
        )

    def test_landing(self):
        request = self.factory.get('/')
        response = Landing.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_resume(self):
        request = self.factory.get('/resume/')
        response = Resume.as_view()(request)
        self.assertEqual(response.status_code, 200)
