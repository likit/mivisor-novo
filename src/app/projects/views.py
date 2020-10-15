import os
import glob
from flask import request, redirect, render_template, url_for, jsonify
from . import project_bp as project

PROJECT_DIR = os.path.join(os.getcwd(), 'projects')

@project.route('/api/new')
def create_project():
    proj_name = request.args.get('name')
    if not proj_name:
        return jsonify(success=False, message='No project name specified.')
    proj_dir = os.path.join('projects', proj_name)
    proj_dir = os.path.join(os.getcwd(), proj_dir)
    if os.path.exists(proj_dir):
        return jsonify(success=False, message='Project already exists.')
    else:
        os.makedirs(proj_dir)
        return jsonify(success=True)


@project.route('/')
def list_projects():
    dirs = [d for d in os.listdir(PROJECT_DIR)]
    return render_template('projects/list.html', projects=dirs)