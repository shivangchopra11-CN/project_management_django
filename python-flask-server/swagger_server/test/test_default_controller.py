# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.project import Project  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_assign_mentor(self):
        """Test case for assign_mentor

        
        """
        response = self.client.open(
            '//project/{proj_id}/assign-mentor/{user_id}/'.format(user_id=56, proj_id=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_assign_project(self):
        """Test case for assign_project

        
        """
        response = self.client.open(
            '//users/{user_id}/assign-project/{proj_id}/'.format(user_id=56, proj_id=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_project(self):
        """Test case for create_project

        
        """
        name = Project()
        response = self.client.open(
            '//project/',
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mentees(self):
        """Test case for get_mentees

        
        """
        response = self.client.open(
            '//users/{user_id}/mentees/'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mentoring_projects(self):
        """Test case for get_mentoring_projects

        
        """
        response = self.client.open(
            '//users/{user_id}/projects/'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users_and_mentors(self):
        """Test case for get_users_and_mentors

        
        """
        response = self.client.open(
            '//project/{project_id}/get-user-mentor/'.format(project_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_create(self):
        """Test case for user_create

        
        """
        name = User()
        response = self.client.open(
            '//users/',
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
