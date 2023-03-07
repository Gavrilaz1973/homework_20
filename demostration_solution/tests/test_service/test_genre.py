import pytest
from unittest.mock import MagicMock
from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.genre import Genre
from demostration_solution.service.genre import GenreService
from demostration_solution.setup_db import db


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    d_1 = Genre(id=1, name='jonh')
    d_2 = Genre(id=2, name='kate')
    d_3 = Genre(id=3, name='max')

    genre_dao.get_one = MagicMock(return_value=d_1)
    genre_dao.get_all = MagicMock(return_value=[d_1, d_2])
    genre_dao.create = MagicMock(return_value=d_3)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre != None
        assert genre.id == 1

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) == 2

    def test_create(self):
        genre_s = {
            "name": "Ivan"
        }
        genre = self.genre_service.create(genre_s)
        assert genre.id != None

    def test_delete(self):
        genre = self.genre_service.delete(1)
        assert genre is None

    def test_update(self):
        genre_u = {
            "id": 3,
            "name": "Ivan"
        }
        self.genre_service.update(genre_u)


