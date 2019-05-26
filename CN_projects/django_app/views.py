import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view

from .models import User, Project, ProjectUser


@csrf_exempt
@require_http_methods(['POST'])
@api_view(['POST'])
def create_user(request):
    data = json.loads(request.body.decode('utf-8'))
    name = data.get('name')
    user = User(name=name)
    user.save()
    return HttpResponse('202 : User added successfully')


@csrf_exempt
@require_http_methods(['POST'])
@api_view(['POST'])
def create_project(request):
    data = json.loads(request.body.decode('utf-8'))
    name = data.get('name')
    project = Project(name=name)
    project.save()
    return HttpResponse('202 : Project created successfully')


@csrf_exempt
@require_http_methods(['POST'])
@api_view(['POST'])
def assign_project(request,user_id,proj_id):
    user = user_id
    project = Project.objects.get(id=proj_id)
    user_object = User.objects.get(id=user)
    proj_user = ProjectUser(user=user_object, project=project)
    proj_user.save()
    return HttpResponse('202 : Project assigned to user')


@csrf_exempt
@require_http_methods(['POST'])
@api_view(['POST'])
def assign_mentor(request,proj_id,user_id):
    user = user_id
    user_object = User.objects.get(id=user)
    proj_id = proj_id
    project = Project.objects.get(id=proj_id)
    pu = ProjectUser(user=user_object, project=project, is_mentor=True)
    pu.save()
    return HttpResponse('202 : Mentor assigned to project successfully')


@csrf_exempt
@require_http_methods(['GET'])
@api_view(['GET'])
def get_projects(request, user_id):
    user_object = User.objects.get(id=user_id)
    project_users = ProjectUser.objects.filter(user=user_object, is_mentor=True).values_list('project_id', flat=True)
    projects = []
    for pu in project_users:
        projects.append(pu)
    response = {
        'result': projects,
        'message': "Projects Fetched",
        'status_code': '202'
    }
    return HttpResponse(json.dumps(response), content_type='application/json')


@csrf_exempt
@require_http_methods(['GET'])
@api_view(['GET'])
def get_mentees(request, user_id):
    """
        get:
        Get all the mentees of a user.
    """
    # print(request.body)
    user_object = User.objects.get(id=user_id)
    project_users = ProjectUser.objects.filter(user=user_object, is_mentor=True).values_list('project_id', flat=True)
    projects = []
    for pu in project_users:
        projects.append(pu)
    users = []
    for proj in projects:
        cur_proj = Project.objects.get(id=proj)
        cur_usrs = ProjectUser.objects.filter(project=cur_proj, is_mentor=False).values_list('user_id', flat=True)
        for usr in cur_usrs:
            users.append(usr)
    users = list(set(users))
    response = {
        'result': users,
        'message': "Mentees Fetched",
        'status_code': '202'
    }
    return HttpResponse(json.dumps(response), content_type='application/json')


@csrf_exempt
@require_http_methods(['GET'])
@api_view(['GET'])
def get_user_mentor(request, proj_id):
    print(request, proj_id)
    proj_object = Project.objects.get(id=proj_id)
    proj_users = ProjectUser.objects.filter(project=proj_object, is_mentor=False).values_list('user_id', flat=True)
    project_mentor = ProjectUser.objects.get(project=proj_object, is_mentor=True).user_id
    users = []
    for pu in proj_users:
        users.append(pu)
    print(users, project_mentor)
    response = {
        'result': {'users': users, 'mentor': project_mentor},
        'message': "Mentors and Users Fetched",
        'status_code': '202'
    }
    return HttpResponse(json.dumps(response), content_type='application/json')
