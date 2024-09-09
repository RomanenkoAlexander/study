def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

#Вызываем test_function
#test_function()
#Вызываем inner_function
inner_function()
