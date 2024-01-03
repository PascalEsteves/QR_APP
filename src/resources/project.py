from flask.views import MethodView
from flask_smorest import Blueprint, abort
from src.models.database import db
from src.schemas.schemas import PlainProjectSchema
from src.models.models import ProjectModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Project",
                __name__,
                description = "Operation on Project"
                )

blp.route("/project/<str:hascode>")
class Project(MethodView):

    @blp.response(200, PlainProjectSchema)
    def get(self, hascode:str):
        """
        Get a specific project
        Args:
            :params hascode - hascode of QR Code
        Returns:
            project
        """
        project = ProjectModel.query.filter(ProjectModel.hascode==hascode).first()
        return project

    def delete(self, hascode:str):
        """
        Delete a specific project
        Args:
            :params hascode - hascode of QR Code
        Retunrs:
            204 if deleted successfully else 404
        """
        project = ProjectModel.query.filter(ProjectModel.hascode==hascode).first()
        if project is not None:
            abort(404, message="Project not found")
        else:
            db.session.delete(project)
            db.commit()
            return {"message":"Project successfully deleted"},204

@blp.route("/projects")
class ProjectList(MethodView):
    @blp.response(200, PlainProjectSchema)
    def get(self):
        """
        Return all projects in database
        Args:
            :params: None
        Returns:
            List of projects
        """
        return ProjectModel.query.all()

    @blp.arguments(PlainProjectSchema)
    @blp.response(200, PlainProjectSchema)
    def post(self, project_data:str):
        """
        Add Project to database
        Args:
            :params project data
        Return
            project
        """
        project = ProjectModel(**project_data)
        try:
            db.session.add(project)
            db.session.commit()

        except IntegrityError:
            abort(400, message="A project with that name already exists")

        except SQLAlchemyError:
            abort(500, message = "An error occurred creating the project.")

        return project

@blp.route("/projects/active")
class ProjectList(MethodView):
    @blp.response(200, PlainProjectSchema)
    def get(self):
        """
        Return all active projects in database
        Args:
            :params - None
        Returns
            Active projects
        """
        project = ProjectModel.query.filter(ProjectModel.status=='active')
        return project







