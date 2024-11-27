import itertools
import time

# Задание №2
class Iterator:
    def __init__(self):
        pass

    def pick_function(self, func, value): # Добавление функций к итератору
        a = ['sum', 'multiplication', 'difference', 'division']
        
        if func not in a:
            raise ValueError('Данная функция не поддерживается, выберите одну из списка:', a)
        
        if func == 'division' and value == 0:
            raise ZeroDivisionError
        
        try:
            int(value)
        except ValueError:
            try:
                float(value)
            except ValueError:
                raise ValueError('Данные значения value могут быть только типа int или float')
            
        self.func_flag = True
        self.func = func
        self.value = value

    def infinit_iterator(self): # Запускает бесконечный итератор
        gen = itertools.count(start=0, step=1)

        try:
            if self.func == 'sum':
                for i in gen:
                    time.sleep(0.5)
                    print(i + self.value)

            elif self.func == 'multiplication':
                for i in gen:
                    time.sleep(0.5)
                    print(i * self.value)

            elif self.func == 'difference':
                for i in gen:
                    time.sleep(0.5)
                    print(i - self.value)

            elif self.func == 'division':
                for i in gen:
                    time.sleep(0.5)
                    print(i / self.value)

        except AttributeError:
            for i in gen:
                    time.sleep(0.5)
                    print(i)

        except KeyboardInterrupt:
            print('Done!')
        
    def get_iterator_info(self): # Возвращает функцию, примененную к итератору, и значение, которое использует функция     
        try: 
            if self.func_flag == True:
                return self.func, self.value
        except AttributeError:
            return (None, 0)




            
class Join_iterators: # Класс, собирающие все итераторы в один
    def __init__(self):
        self.iterators_list = []
    
    def add_iterators(self, cls): # Добавляет параметры созданных итераторов в общий
        try:
            self.iterators_list.append(cls.get_iterator_info())
        except AttributeError:
            print("Был передан неправильный объект")

    def run_massive_iterator(self): # Запускает все добавленные итераторы
        try:
            iter = True
            index = 0
            while iter == True:
                index += 1
                for i in range(len(self.iterators_list)):
                    val1, val2 = self.iterators_list[i][0], self.iterators_list[i][1]
                    if val1 == 'sum':
                        time.sleep(0.5)
                        print(index + val2)
                    elif val1 == 'multiplication':
                        time.sleep(0.5)
                        print(index * val2)
                    elif val1 == 'difference':
                        time.sleep(0.5)
                        print(index - val2)
                    elif val1 == 'division':
                        time.sleep(0.5)
                        print(index / val2)
                    elif val1 == None:
                        time.sleep(0.5)
                        print(index)
        except KeyboardInterrupt:
            print('Done!')





# Проверка
big = Join_iterators()
q=Iterator()
w=Iterator()
e=Iterator()
r=Iterator()
t=Iterator()
t.pick_function('difference', 333)
q.pick_function('sum', 10)
w.pick_function('division', 1.5)
e.pick_function('multiplication', 0.1)
big.add_iterators(t)
big.add_iterators(q)
big.add_iterators(w)
big.add_iterators(e)
big.add_iterators(r)

t.infinit_iterator()
q.infinit_iterator()
big.run_massive_iterator()
