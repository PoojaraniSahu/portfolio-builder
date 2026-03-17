from flask import Blueprint,render_template,redirect,url_for,request
from .models import *
from . import db
import os
import uuid
from flask import current_app
from flask_login import current_user

workspaces=Blueprint('workspaces',__name__)

@workspaces.route('/workspace/<workspace_id>', methods=['GET','POST'])
def work(workspace_id):
    personalinfo=Personalinfo.query.filter_by(workid=workspace_id).one_or_none()
    print(personalinfo.name)
    skill=Skill.query.filter_by(workid=workspace_id).all()
    education=Education.query.filter_by(workid=workspace_id).all()
    experience = Experience.query.filter_by(workid=workspace_id).all()
    
    workspace= Workspace.query.get(workspace_id)
    print("experience is:",experience)
    return render_template(f'/users/{workspace_id}/home.html',workspace=workspace,personalinfo=personalinfo,education=education,experience=experience,skill=skill)

@workspaces.route('/workspace/<workspace_id>/skills', methods=['GET','POST'])
def skills(workspace_id):
    workspace= Workspace.query.get(workspace_id)
    return render_template(f'/users/{workspace_id}/skill.html',workspace=workspace)
from flask_login import current_user

@workspaces.route('/workspace/<workspace_id>/add_exp', methods=['POST'])
def add_experience(workspace_id):
    # # Get user's work_id
    # if current_user.is_authenticated:
    #     work_id = workspace_id
    # else:
    #     # Handle unauthenticated user
    #     return redirect(url_for('login'))
    work_id = workspace_id
    # Get submitted form data
    titles = request.form.getlist('titles[]')
    years = request.form.getlist('years[]')
    companies = request.form.getlist('companies[]')
    descs = request.form.getlist('descs[]')

    # Retrieve all existing experiences for the user
    existing_experiences = Experience.query.filter_by(workid=work_id).all()

    if existing_experiences:
        # Update existing experiences and add new ones as necessary
        for existing_experience, title, year, company, desc in zip(existing_experiences, titles, years, companies, descs):
            # Update existing experience with new data
            existing_experience.title = title
            existing_experience.year = year
            existing_experience.company = company
            existing_experience.descr = desc
        # Add new experiences for any additional submitted data
        for i in range(len(existing_experiences), len(titles)):
            experience = Experience(workid=work_id,ids=str(uuid.uuid4), title=titles[i], year=years[i], company=companies[i], descr=descs[i])
            db.session.add(experience)
    else:
        # Add new experiences for all submitted data
        for title, year, company, desc in zip(titles, years, companies, descs):
            experience = Experience(workid=work_id,ids=str(uuid.uuid4), title=title, year=year, company=company, descr=desc)
            db.session.add(experience)

    # Commit changes to the database
    db.session.commit()
    return redirect(f'/workspace/{workspace_id}')
@workspaces.route('/workspace/<workspace_id>/add_edu', methods=['POST'])
def add_education(workspace_id):
    # # Get user's work_id
    # if current_user.is_authenticated:
    #     work_id = workspace_id
    # else:
    #     # Handle unauthenticated user
    #     return redirect(url_for('login'))
    work_id = workspace_id
    # Get submitted form data
    courses = request.form.getlist('course[]')
    years = request.form.getlist('year[]')
    institutes = request.form.getlist('institute[]')
    descs = request.form.getlist('desc[]')

    # Retrieve all existing experiences for the user
    existing_educations = Education.query.filter_by(workid=work_id).all()

    if existing_educations:
        # Update existing experiences and add new ones as necessary
        for existing_education, course, year, institute, desc in zip(existing_educations, courses, years, institutes, descs):
            # Update existing experience with new data
            existing_education.course = course
            existing_education.year = year
            existing_education.clg = institute
            existing_education.descr = desc
        # Add new experiences for any additional submitted data
        for i in range(len(existing_educations), len(courses)):
            print(institute[i])
            education = Education(workid=work_id,ids=str(uuid.uuid4), course=courses[i], year=years[i],clg=institutes[i], descr=descs[i])
            db.session.add(education)
    else:
        # Add new experiences for all submitted data
        for course, year, institute, desc in zip(courses, years, institutes, descs):
            education = Education(workid=work_id,ids=str(uuid.uuid4), course=course, year=year,clg=institute, descr=desc)
            db.session.add(education)

    # Commit changes to the database
    db.session.commit()
    return redirect(f'/workspace/{workspace_id}')

#for skills
@workspaces.route('/workspace/<workspace_id>/add_skill', methods=['POST'])
def add_skill(workspace_id):
    # # Get user's work_id
    # if current_user.is_authenticated:
    #     work_id = workspace_id
    # else:
    #     # Handle unauthenticated user
    #     return redirect(url_for('login'))
    work_id = workspace_id
    # Get submitted form data
    skills = request.form.getlist('skill[]')
    percs = request.form.getlist('perc[]')

    # Retrieve all existing experiences for the user
    existing_skills = Skill.query.filter_by(workid=work_id).all()

    if existing_skills:
        # Update existing experiences and add new ones as necessary
        for existing_skill, skill, perc in zip(existing_skills, skills, percs):
            # Update existing experience with new data
            existing_skill.skill = skill
            existing_skill.perc = perc
        # Add new experiences for any additional submitted data
        for i in range(len(existing_skills), len(skills)):
            skill = Skill(workid=work_id,ids=str(uuid.uuid4()), skill=skills[i], perc=percs[i])
            db.session.add(skill)
    else:
        # Add new experiences for all submitted data
        for skill, perc in zip(skills, percs):
            skill = Skill(workid=work_id,ids=str(uuid.uuid4()), skill=skill, perc=perc)
            db.session.add(skill)

    # Commit changes to the database
    db.session.commit()
    return redirect(f'/workspace/{workspace_id}')

#for personal information
@workspaces.route('/workspace/<workspace_id>/add_pf', methods=['POST'])
def add_pf(workspace_id):
    # # Get user's work_id
    # if current_user.is_authenticated:
    #     work_id = workspace_id
    # else:
    #     # Handle unauthenticated user
    #     return redirect(url_for('login'))
    work_id = workspace_id
    # Get submitted form data
    names = request.form.get('name')
    abouts = request.form.get('about')
    emails = request.form.get('email')
    phones = request.form.get('phone')
    degrees = request.form.get('degree')
    freelances = request.form.get('freelance')
    ages = request.form.get('age')
    designations = request.form.get('designation')
    yoexs = request.form.get('yoex')
    projects = request.form.get('project')
    hpclients = request.form.get('hpclient')
    awards = request.form.get('award')
    # Retrieve all existing experiences for the user()
    existing_pfs = Personalinfo.query.filter_by(workid=work_id).all()

    if existing_pfs:
        # Update existing experiences and add new ones as necessary
            # Update existing experience with new data
        for existing_pf in existing_pfs:
            existing_pf.name = names
            existing_pf.about = abouts
            existing_pf.email = emails
            existing_pf.phone = phones
            existing_pf.degree = degrees
            existing_pf.freelance = freelances
            existing_pf.age = ages
            existing_pf.designation = designations
            existing_pf.yoex = yoexs
            existing_pf.project = projects
            existing_pf.hpclients = hpclients
            existing_pf.awards = awards
            print("name is",names)
    else:
        # Add new experiences for all submitted data
        pf = Personalinfo(workid=work_id,ids=str(uuid.uuid4()), name=names,about=abouts,email=emails,phone=phones,freelance=freelances,age=ages,designation=designations,yoex=yoexs,project=projects,hpclients=hpclients,awards=awards)
        db.session.add(pf)

    # Commit changes to the database
    db.session.commit()
    return redirect(f'/workspace/{workspace_id}')