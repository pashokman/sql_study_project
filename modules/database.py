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

    
    def get_table_columns_names(self, table_name):
        query = f'PRAGMA table_info({table_name});'
        self.cursor.execute(query)
        columns = [column[1] for column in self.cursor.fetchall()]

        return columns


    def get_all_table_data(self, table_name):
        query = f'SELECT * FROM {table_name};'
        record = self.query_to_execute(query)
        return record


    def result_with_all_table_columns_names(self, data, database_name):
        columns = self.get_table_columns_names(database_name)
        return make_data_as_a_table(data, [*columns])


    def result_with_all_table_columns_names(self, data, databases_names):
        columns = self.get_table_columns_names(databases_names)
        return make_data_as_a_table(data, [*columns])
    

    def result_with_few_tables_columns_names(self, data, *databases_names):
        all_columns = []

        for base in databases_names:
            columns = self.get_table_columns_names(base)
            new_columns = []
            for column in columns:
                column = base + '_' + column
                new_columns.append(column)
            all_columns += new_columns
        
        return make_data_as_a_table(data, [*all_columns])
    

    def result_with_specific_column_names(self, data, *args):
        return make_data_as_a_table(data, [*args])
    

    def get_avg_column_value(self, table_name, column):
        query = f'SELECT ROUND(AVG({column})) FROM {table_name};'
        record = self.query_to_execute(query)
        return record[0][0]
