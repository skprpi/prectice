class LinkedList:

    HEAD_OK = 1 # успешный вызов head()
    HEAD_ERR = 2 # список пуст

    TAIL_OK = 1 # успешный вызов tail()
    TAIL_ERR = 2 # список пуст

    RIGHT_OK = 1 # успешный вызов right()
    RIGHT_ERR_EMPTY_LIST = 2 # список пуст
    RIGHT_ERR_LAST_ELEMENT = 3 # указатель стоит на последнем элементе

    REMOVE_OK = 1 # успешный вызов remove()
    REMOVE_ERR = 2 # курсор указывает на пустой элемент

    REPLACE_OK = 1 # успешный вызов replace()
    REPLACE_ERR = 2 # курсор указывает на пустой элемент

    FIND_OK = 1 # успешный вызов find()
    FIND_ERR = 2 # элемент не найден и курсор указывает на пустой элемент

    GET_OK = 1 # успешный вызов get()
    GET_ERR = 2 # курсор указывает на пустой элемент


# конструктор

    # предусловие: 
    # постусловие: создан новый связный список
    def __init__(self):
        self._cursor = None # курсор - указывает на элемент с которым предстоит работать
        pass

# команды

    # предусловие: список не пуст
    # постусловие: курсор установлен на первый элемент списка
    def head(self):
        pass

    # предусловие: список не пуст
    # постусловие: курсор установлен на последний элемент списка
    def tail(self):
        pass

    # предусловие: список не пуст и курсор указывает не на последний элемент
    # постусловие: курсор сдвинут вправо на 1 элемент
    def right(self):
        pass

    # предусловие:
    # постусловие: справа от текущего узла появился новый узел. если список был пуст,
    #              кусор будет указывать на первый элемент
    def put_rigth(self, value):
        pass

    # предусловие:
    # постусловие: слева от текущего узла появился новый узел. если список был пуст,
    #              кусор будет указывать на первый элемент
    def put_left(self, value):
        pass

    # предусловие: курсор указывает на какой-либо элемент (список не пуст)
    # постусловие: курсор смещается к правому соседу, если он есть,
    #              в противном случае к левому, если он есть
    def remove(self):
        pass

    # предусловие: 
    # постусловие: указатель указывает на пустой элемент, список отчищен
    def clear(self):
        pass

    # предусловие: 
    # постусловие: добавляем новый узел в конец списка
    def add_tail(self, value):
        pass

    # предусловие: курсор указывет не на пустой элемент
    # постусловие: текущий узел изменил значение
    def replace(self, value):
        pass

    # предусловие: курсор указывает не на пустой элемент
    # постусловие: устанавливаем курсор на следующий узел с искомым значением
    def find(self, value):
        pass

    # предусловие: 
    # постусловие: удалены все узлы списка имеющие переданное значение
    def remove_all(self, value):
        pass

# запросы

    # предусловие: курсор указывает не на пустой элемент
    # постусловие: 
    def get(self):
        pass

    # предусловие: 
    # постусловие: 
    def size(self):
        pass

    # предусловие: 
    # постусловие: 
    def is_head(self):
        pass

    # предусловие: 
    # постусловие: 
    def is_tail(self):
        pass

    # предусловие: 
    # постусловие: 
    def is_value(self):
        pass

# доп. запросы

    def get_head_status(self): # возвращает значение HEAD_*
        pass

    def get_tail_status(self): # возвращает значение TAIL_*
        pass

    def get_right_status(self): # возвращает значение RIGHT_*
        pass

    def get_remove_status(self): # возвращает значение REMOVE_*
        pass

    def get_replace_status(self): # возвращает значение REPLACE_*
        pass

    def get_find_status(self): # возвращает значение FIND_*
        pass

    def get_get_status(self): # возвращает значение GET_*
        pass
