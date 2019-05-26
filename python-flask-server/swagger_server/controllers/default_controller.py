import connexion
import six

from swagger_server.models.project import Project  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def assign_mentor(user_id, proj_id):  # noqa: E501
    """assign_mentor

    Assign a project mentor to a project. # noqa: E501

    :param user_id: ID of user
    :type user_id: int
    :param proj_id: ID of project
    :type proj_id: int

    :rtype: None
    """
    return 'do some magic!'


def assign_project(user_id, proj_id):  # noqa: E501
    """assign_project

    Assign a project mentor to a project. # noqa: E501

    :param user_id: ID of user
    :type user_id: int
    :param proj_id: ID of project
    :type proj_id: int

    :rtype: None
    """
    return 'do some magic!'


def create_project(name):  # noqa: E501
    """create_project

    Create a project # noqa: E501

    :param name: Name of project
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = Project.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_mentees(user_id):  # noqa: E501
    """get_mentees

    Get the list of IDs of the users being mentored by the queried user. # noqa: E501

    :param user_id: ID of the user
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_mentoring_projects(user_id):  # noqa: E501
    """get_mentoring_projects

    Get the list of IDs of the projects being mentored by the queried user. # noqa: E501

    :param user_id: ID of the user
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_users_and_mentors(project_id):  # noqa: E501
    """get_users_and_mentors

    Get the list of IDs of the mentors and users of the project # noqa: E501

    :param project_id: ID of the project
    :type project_id: int

    :rtype: None
    """
    return 'do some magic!'


def user_create(name):  # noqa: E501
    """user_create

    Create a new user # noqa: E501

    :param name: The name of the person
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
