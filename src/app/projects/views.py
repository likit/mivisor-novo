import os
from flask import request, redirect, render_template, url_for
from . import project_bp as project


@project.route('/new')
def create_project():
    proj_name = request.args.get('name')
    if os.path.exists(proj_name):
        return 'Exists'
    else:
        return 'Not exists'