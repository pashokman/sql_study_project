from modules.database import Database

from utilities.list_of_tuples_in_dictionaty import list_of_tuples_in_dictionary


class Marvels(Database):

    def __init__(self):
        super().__init__()


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

        return record
    

    def get_characters_by_gender_hometown_energy_Projection(self, database_name, gender, hometown, energy_Projection):
        query = f'''SELECT * FROM {database_name}\
                    WHERE gender = "{gender}"\
                    AND hometown = "{hometown}"\
                    AND energy_Projection = {energy_Projection};'''
        record = self.query_to_execute(query)

        return record


    def get_parameter_sum_of_all_characters(self, database_name, param):
        query = f'''SELECT SUM({param}) FROM {database_name};'''
        record = self.query_to_execute(query)
        return record[0][0]
    

    def get_few_parameters_sum_of_all_characters(self, database_name, *args):
        params_sum_list = []
        for arg in args:
            param_sum = self.get_parameter_sum_of_all_characters(database_name, arg)
            params_sum_list.append(param_sum)

        return params_sum_list
    

    def can_all_characters_defeat_badguy(self, all_characters_param_sum_list, badguy_params):
        for i in range(0, len(badguy_params)):
            if all_characters_param_sum_list[i] <= badguy_params[i]:
                return False
            
        return True


    def get_characters_with_more_popularity_or_more_weight(self, database_name, popularity, weight):
        query = f'''SELECT * FROM {database_name}\
                    WHERE popularity < {popularity}\
                    OR weight_kg > {weight};'''
        record = self.query_to_execute(query)

        return record
    

    def group_characters_by_param(self, database_name, param):
        query = f'''SELECT {param}, COUNT(*) FROM {database_name}\
                    GROUP BY {param};'''
        record = self.query_to_execute(query)

        dictionaty = list_of_tuples_in_dictionary(record)
        return dictionaty
    