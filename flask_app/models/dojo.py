from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = 'dojos_and_ninjas_schema'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas_list = []

    @classmethod
    def show_one(cls,id):
        query = """
        SELECT * FROM dojos WHERE id = %(id)s
        """
        result = connectToMySQL(cls.db).query_db(query,{'id':id})
        return cls(result[0])

    @classmethod
    def show_all(cls):
        query = """
        SELECT * FROM dojos
        """
        dojos = []
        results = connectToMySQL(cls.db).query_db(query)
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def create_dojo(cls,data):
        query = """
        INSERT
        INTO dojos(name,created_at,updated_at)
        VALUES(%(name)s,NOW(),NOW())
        """
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        return result

    @classmethod
    def get_ninjas(cls,id):
        query = """
        SELECT *
        FROM dojos
        LEFT JOIN ninjas
        ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,{'id':id})
        all_objects = []

        for row_from_db in results:
            db_object = cls(row_from_db)
            ninja_data = {
                'id' : row_from_db['ninjas.id'],
                'first_name' : row_from_db['first_name'],
                'last_name' : row_from_db['last_name'],
                'age' : row_from_db['age'],
                'dojo_id' : row_from_db['dojo_id'],
                'name' : row_from_db['name'],
                'created_at' : row_from_db['ninjas.created_at'],
                'updated_at' : row_from_db['ninjas.updated_at']
            }
            new_object = ninja.Ninja(ninja_data)
            db_object.ninjas_list = new_object
            all_objects.append(new_object)
        return all_objects