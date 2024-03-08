import sqlite3

from utilities.data_into_table import make_data_as_a_table


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(r'./first_database.db')
        self.cursor = self.connection.cursor()


    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"\nConnected successfully. SQLite Database Version is: {record}")


    def query_to_execute(self, query):
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record


    def create_new_table(self, query_str):
        query_list = query_str.split(';')

        try:
            for query in query_list:
                self.query_to_execute(query)
                self.connection.commit()
        except Exception as e:
            print(f'\nException message: {e}')

    
    def get_tables_column_names(self, table_name):
        query = f'PRAGMA table_info({table_name});'
        self.cursor.execute(query)
        columns = [column[1] for column in self.cursor.fetchall()]

        return columns


    def get_all_table_data(self, table_name):
        query = f'SELECT * FROM {table_name};'
        record = self.query_to_execute(query)

        columns = self.get_tables_column_names(table_name)
        
        return make_data_as_a_table(record, columns)
        # return record


    def get_avg_column_value(self, table_name, column):
        query = f'SELECT ROUND(AVG({column})) FROM {table_name};'
        record = self.query_to_execute(query)

        return record[0][0]


    def sort_characters_by_avg_column_value(self, table_name, identify_column, calc_avg_column, result_column):

        avg = self.get_avg_column_value(table_name, calc_avg_column)

        query = f'''SELECT {identify_column}, {calc_avg_column},\
                        CASE\
                            WHEN {calc_avg_column} > {avg} THEN "Best"\
                            WHEN {calc_avg_column} = {avg} THEN "Common"\
                            ELSE "Silly"
                        END as "{result_column}"
                    FROM {table_name};'''
        
        record = self.query_to_execute(query)

        return make_data_as_a_table(record, [identify_column, calc_avg_column, result_column])
    
    
    def get_characters_by_gender_hometown_energy_Projection(self, database_name, gender, hometown, energy_Projection):
        query = f'''SELECT * FROM {database_name}\
                    WHERE gender = "{gender}"\
                    AND hometown = "{hometown}"\
                    AND energy_Projection = {energy_Projection};'''
        
        record = self.query_to_execute(query)

        columns = self.get_tables_column_names(database_name)

        return make_data_as_a_table(record, [*columns])