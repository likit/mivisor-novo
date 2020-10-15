import os
from flask import request, redirect, render_template, url_for, jsonify
from flask.signals import message_flashed
from . import project_bp as project


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