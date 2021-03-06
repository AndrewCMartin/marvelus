import json

from app.models import db, Character, Movie, Event, TvShow, Actor, ComicSeries
from testing_config import BaseTestConfig


class TestAPI(BaseTestConfig):
    def test_get_from_index(self):
        result = self.app.get("/")
        self.assertIn('<html', result.data.decode("utf-8"))
        self.assert200(result)

    def test_add_character(self):
        c = Character(123, "Example_name", "Description", "/.jpg", "")
        db.session.merge(c)
        db.session.commit()
        q = Character.query.filter_by(id=123).first()
        self.assertEqual(q.id, c.id)
        self.assertEqual(q.name, c.name)

    def test_add_movie(self):
        m = Movie(443, "Example_movie", "", False, "", 200, None, "en", 5)
        db.session.merge(m)
        db.session.commit()
        q = Movie.query.filter_by(id=443).first()
        self.assertEqual(q.id, m.id)
        self.assertEqual(q.title, m.title)

    def test_get_character(self):
        c = Character(123, "Example_name", "Description", "/.jpg", "")
        db.session.merge(c)
        db.session.commit()
        correct_data = {'id': 123, 'name': 'Example_name'}
        result = self.app.get("/api/character/123")
        result_data = json.loads(result.data.decode("utf-8"))
        for key in correct_data:
            self.assertEqual(correct_data[key], result_data[key])

    def test_add_actor_to_movie(self):
        a = Actor(12, "Robert Downey Jr.", None, "", "")
        m = Movie(42, "Iron Man", "", False, "", 50, None, "", 5)
        a.movies.append(m)
        db.session.merge(a)

        q_a = Actor.query.filter_by(id=12).first()
        q_m = q_a.movies[0]
        self.assertEqual(q_m.id, m.id)

    def test_get_movie(self):
        m = Movie(443, "Example_movie", "", False, "", 200, None, "en", 5)
        db.session.merge(m)
        db.session.commit()

        correct_data = {'id': 443, 'title': 'Example_movie'}
        result = self.app.get("/api/movie/443")

        result_data = json.loads(result.data.decode("utf-8"))
        for key in correct_data:
            self.assertEqual(correct_data[key], result_data[key])

    def test_get_series(self):
        s = ComicSeries(554, "Example_series1", "", False, None, None)
        db.session.merge(s)
        db.session.commit()

        correct_data = {'id': 554, 'title': 'Example_series1'}
        result = self.app.get("/api/comic_series/554")

        result_data = json.loads(result.data.decode("utf-8"))
        for key in correct_data:
            self.assertEqual(correct_data[key], result_data[key])

    def test_add_comicseries(self):
        m = ComicSeries(412, "Example_series2", "", False, None, None)
        db.session.merge(m)
        db.session.commit()
        correct_data = {'id': 412, 'title': 'Example_series2'}
        result = self.app.get("/api/comic_series/412")
        result_data = json.loads(result.data.decode("utf-8"))
        for key in correct_data:
            self.assertEqual(correct_data[key], result_data[key])

    def test_add_events(self):
        e = Event(123, "Example_event", "lol", "/.jpg", 1234, "Hmm")
        db.session.merge(e)
        db.session.commit()
        q = Event.query.filter_by(id=123).first()
        self.assertEqual(q.id, e.id)
        self.assertEqual(q.title, e.title)

    def test_get_event(self):
        e = Event(253, "Example_event", "Description", "/.jpg", 5134, "")
        db.session.merge(e)
        db.session.commit()
        correct_data = {'id': 253, 'title': 'Example_event'}
        result = self.app.get("/api/event/253")
        result_data = json.loads(result.data.decode("utf-8"))
        for key in correct_data:
            self.assertEqual(correct_data[key], result_data[key])

    def test_get_actor(self):
        a = Actor(123, "Natalie Dormer", None, "Model", "gorgeous.jpg")
        db.session.merge(a)
        db.session.commit()
        correct_data = {'id': 123, 'name': 'Natalie Dormer', 'birthday': None, 'bio': 'Model', 'image': 'gorgeous.jpg'}
        result = self.app.get("/api/actor/123")
        result_data = json.loads(result.data.decode("utf-8"))
        for key in correct_data:
            self.assertEqual(correct_data[key], result_data[key])

    def test_get_actor_2(self):
        a = Actor(129, "Emma Watson", None, "She is pretty good looking", "model.jpg")
        db.session.merge(a)
        db.session.commit()
        correct_data = {'id': 129, 'name': 'Emma Watson', 'birthday': None, 'bio': 'She is pretty good looking',
                        'image': 'model.jpg'}
        result = self.app.get("/api/actor/129")
        result_data = json.loads(result.data.decode("utf-8"))
        for key in correct_data:
            self.assertEqual(correct_data[key], result_data[key])

    def test_add_tv_show(self):
        t = TvShow(678, "Example_name", "Description", "/.jpg", None, None, 0, 0)
        db.session.merge(t)
        db.session.commit()
        q = TvShow.query.filter_by(id=678).first()
        self.assertEqual(q.id, t.id)
        self.assertEqual(q.name, t.name)

    def test_get_tv_show(self):
        t = TvShow(123, "Example_name", "Description", "/.jpg", None, None, 0, 0)
        db.session.merge(t)
        db.session.commit()
        correct_data = {'id': 123, 'name': 'Example_name'}
        result = self.app.get("/api/tv_show/123")
        result_data = json.loads(result.data.decode("utf-8"))
        for key in correct_data:
            self.assertEqual(correct_data[key], result_data[key])

    def test_search_comic1(self):
        m = ComicSeries(412, "Example_series2", "", False, None, None)
        db.session.merge(m)
        db.session.commit()
        a = ComicSeries.query.whoosh_search('Example_series2').all()
        comic1 = ComicSeries.query.filter_by(id=412).first()
        self.assertIn(comic1, a)

    def test_search_comic2(self):
        s = ComicSeries(554, "Example_series1", "", False, None, None)
        db.session.merge(s)
        db.session.commit()
        a = ComicSeries.query.whoosh_search('Example_series1').all()
        comic1 = ComicSeries.query.filter_by(id=554).first()
        self.assertIn(comic1, a)

    def test_search_movie(self):
        m = Movie(443, "Example movie", "", False, "", 200, None, "en", 5)
        db.session.merge(m)
        db.session.commit()
        search_results = Movie.query.whoosh_search('movie').all()
        hulk_movie = Movie.query.filter_by(id=443).first()
        self.assertIn(hulk_movie, search_results)

    def test_search_event_2(self):
        e = Event(253, "Example_event", "Description", "/.jpg", 5134, "")
        db.session.merge(e)
        db.session.commit()
        search_results = Event.query.whoosh_search('example_event').all()
        spider_event = Event.query.filter_by(id=253).first()
        self.assertIn(spider_event, search_results)

    def test_search_actor(self):
        a = Actor(123, "Natalie Dormer", None, "Model", "gorgeous.jpg")
        db.session.merge(a)
        db.session.commit()
        a = Actor.query.whoosh_search('Natalie').all()
        tom_holland = Actor.query.filter_by(id=123).first()
        self.assertIn(tom_holland, a)

    def test_search_actor_2(self):
        a = Actor(129, "Emma Watson", None, "She is pretty good looking", "model.jpg")
        db.session.merge(a)
        db.session.commit()
        a = Actor.query.whoosh_search('Watson').all()
        sam_jackson = Actor.query.filter_by(id=129).first()
        self.assertIn(sam_jackson, a)

    def test_search_tv_show_1(self):
        t = TvShow(678, "Example_name", "Description", "/.jpg", None, None, 0, 0)
        db.session.merge(t)
        db.session.commit()
        search_results = TvShow.query.whoosh_search('Example_name').all()
        agent_carter_tvshow = TvShow.query.filter_by(id=678).first()
        self.assertIn(agent_carter_tvshow, search_results)

    def test_search_character(self):
        c = Character(123, "Example name", "Description", "/.jpg", "")
        db.session.merge(c)
        db.session.commit()
        search_results = Character.query.whoosh_search('example').all()
        iron_man_character = Character.query.filter_by(id=123).first()
        self.assertIn(iron_man_character, search_results)