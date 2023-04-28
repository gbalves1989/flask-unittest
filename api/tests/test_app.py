import unittest
import json
from api import app
from api.models.course_model import CourseModel
from sqlalchemy import desc
from api import db


class AppTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_create_course(self):
        response = self.client.post(
            '/api/v1/courses/',
            data=json.dumps(dict(
                name='curso teste',
                description='formação teste'
            )),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn('application/json', response.content_type)

        result = json.loads(response.data)

        self.assertEqual(result.get('name'), 'curso teste')
        self.assertEqual(result.get('description'), 'formação teste')

    def test_find_all(self):
        response = self.client.get('/api/v1/courses/?page=1&per_page=10')

        result = json.loads(response.data)
        count_registers = len(result)

        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.content_type)
        self.assertEqual(len(result), count_registers)

    def test_find_by_id_course(self):
        last_course = db.session.query(CourseModel).order_by(desc(CourseModel.id)).first()
        response = self.client.get(f'/api/v1/courses/{last_course.id}')

        result = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.content_type)
        self.assertEqual(result.get('id'), last_course.id)

    def test_update_course(self):
        last_course = db.session.query(CourseModel).order_by(desc(CourseModel.id)).first()
        response = self.client.put(
            f'/api/v1/courses/{last_course.id}',
            data=json.dumps(dict(
                name='curso teste 2',
                description='formação teste 2'
            )),
            content_type='application/json'
        )

        result = json.loads(response.data)

        self.assertEqual(response.status_code, 202)
        self.assertIn('application/json', response.content_type)
        self.assertEqual(result.get('id'), last_course.id)
        self.assertEqual(result.get('name'), 'curso teste 2')
        self.assertEqual(result.get('description'), 'formação teste 2')

    def test_delete_course(self):
        last_course = db.session.query(CourseModel).order_by(desc(CourseModel.id)).first()
        response = self.client.delete(f'/api/v1/courses/{last_course.id}')

        self.assertEqual(response.status_code, 204)
