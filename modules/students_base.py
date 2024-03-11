from modules.database import Database


class Students(Database):

    def __init__(self):
        super().__init__()


    def get_cross_join(self, table1_name, table2_name):
        query = f'''SELECT * FROM {table1_name}, {table2_name}'''
        record = self.query_to_execute(query)
        
        return record
    

    def get_implicit_inner_join(self, table1_name, table2_name):
        query = f'''SELECT * FROM {table1_name}, {table2_name}\
                    WHERE {table1_name}.id = {table2_name}.student_id'''
        record = self.query_to_execute(query)
        
        return record
    

    def get_explicit_inner_join(self, table1_name, table2_name):
        query = f'''SELECT * FROM {table1_name}\
                    JOIN {table2_name}\
                    ON {table1_name}.id = {table2_name}.student_id'''
        record = self.query_to_execute(query)
        
        return record
    

    def get_left_outer_join(self, table1_name, table2_name):
        # LEFT - means that SQL should return every row of the left table
        # OUTER - means that SQL should return the row even if there is no match in the right table
        query = f'''SELECT {table1_name}.first_name, {table1_name}.last_name, {table2_name}.title\
                    FROM {table1_name}\
                    LEFT OUTER JOIN {table2_name}\
                    ON {table1_name}.id = {table2_name}.student_id'''
        record = self.query_to_execute(query)
        
        return record