from modules.database import Database


class Movies(Database):

    def __init__(self):
        super().__init__()


    def get_self_join(self, table_name):
        # LEFT - means that SQL should return every row of the left table
        # OUTER - means that SQL should return the row even if there is no match in the right table
        # SELF - means that SQL will JOIN the same table
        query = f'''SELECT {table_name}.title, sequels.title as sequels_title\
                   FROM {table_name}\
                   LEFT OUTER JOIN {table_name} sequels\
                   ON {table_name}.sequel_id = sequels.id;'''
        record = self.query_to_execute(query)
        
        return record
    

    def add_new_movie(self, table_name, movie_data):
        query = f'''INSERT INTO {table_name} (id, title, released, sequel_id)\
                    VALUES ({movie_data});'''
        record = self.query_to_execute(query)
        self.connection.commit()
        
        return record
    

    def delete_movie(self, table_name, movie_name):
        query = f'''DELETE FROM {table_name} WHERE title = "{movie_name}";'''
        record = self.query_to_execute(query)
        self.connection.commit()
        
        return record        
    

    def add_new_column(self, table_name, column_name):
        query = f'''ALTER TABLE {table_name} ADD {column_name} TEXT default "nothing";'''
        record = self.query_to_execute(query)
        self.connection.commit()
        
        return record  
    

    def delete_column(self, table_name, column_name):
        query = f'''ALTER TABLE {table_name} DROP COLUMN {column_name};'''
        record = self.query_to_execute(query)
        self.connection.commit()
        
        return record  
    

    def update_movie_year(self, table_name, movie_title, released):
        query = f'''UPDATE {table_name} SET released = {released}\
                    WHERE {table_name}.title = "{movie_title}";'''
        record = self.query_to_execute(query)
        self.connection.commit()
        
        return record  
