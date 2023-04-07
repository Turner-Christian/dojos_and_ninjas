from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db = 'dojos_and_ninjas_schema'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO ninjas (first_name,last_name,age,dojo_id,created_at,updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW())
        """
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def delete(cls,id):
        query = """
        DELETE FROM ninjas WHERE id=%(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query,{'id':id})
        return result

    @classmethod
    def update(cls,data):
        query = """
        UPDATE ninjas 
        SET
        first_name=%(first_name)s,
        last_name=%(last_name)s,
        age=%(age)s,
        updated_at=NOW()
        WHERE id=%(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query,data)
        if result:
            return result
        else:
            return None

    @classmethod
    def ninja_show_one(cls,id):
        query = """
        SELECT * FROM ninjas WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query,{'id':id})
        if result:
            return cls(result[0])
        else:
            return None