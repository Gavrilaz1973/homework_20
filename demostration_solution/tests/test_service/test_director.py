import pytest
from unittest.mock import MagicMock
from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.service.director import DirectorService
from demostration_solution.setup_db import db


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    d_1 = Director(id=1, name='jonh')
    d_2 = Director(id=2, name='kate')
    d_3 = Director(id=3, name='max')

    director_dao.get_one = MagicMock(return_value=d_1)
    director_dao.get_all = MagicMock(return_value=[d_1, d_2])
    director_dao.create = MagicMock(return_value=d_3)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None
        assert director.id == 1

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) == 2

    def test_create(self):
        director_c = {'id': 3, "name": "max"}
        director = self.director_service.create(director_c)
        assert director.name == director_c['name']

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_u = {
            "id": 3,
            "name": "Ivan"
        }
        self.director_service.update(director_u)
