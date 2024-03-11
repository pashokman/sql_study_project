from modules.database import Database


class Movies(Database):

    def __init__(self):
        super().__init__()


    def get_self_join(self, table_name):
        # LEFT - means that SQL should return every row of the left table
        # OUTER - means that SQL should return the row even if there is no match in the right table
        # SELF - means that SQL will JOIN the same table
        query = f'''SELECT {table_name}.title, sequels.title as sequels_title
                   FROM {table_name}
                   LEFT OUTER JOIN {table_name} sequels
                   ON {table_name}.sequel_id = sequels.id'''
        record = self.query_to_execute(query)
        
        return record