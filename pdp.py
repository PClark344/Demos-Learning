class Member:

    def __init__(self, m_id, name, dept):
        self.__m_id = m_id
        self.__m_name = name
        self.__dept = dept
    
    def get_name(self):
        pass

    def get_dept(self):
        pass
    
class Department:

    def __init__(self,name,purpose,head_honcho):
        self.__d_name = name
        self.__purpose = purpose
        self.__head_honcho = head_honcho
        self.__products = []

    def get_products(self):
        return self.__products

    def add_product(self,prodcct):
        return self.__products.append(product.get_name)

    def get_name(self):
        return self.__d_name

    def get_purpose(self):
        return self.__purpose

    def get_head_honcho(self):
        return self.__head_honcho

class MemDbOps:

    def remove_member(self, m_id):
        pass
    
    def transfer_member(self, m_id, dept):
        pass
    
    def save_to_database(self,m_id):
        pass
    
    def update_personal_details(self, m_id, personal_details):
        pass

class Product:
    def __init__(self, name, department):
        self.__p_name = name
        self.__dept = dept

    def get_name(self):
        return self.__p_name

    def get_dept(self):
        return self.__dept.get_name()

