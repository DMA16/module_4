def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

 #inner_function() - вызов этой функции выдаёт ошибку, так как функция была определена в локальном пространстве, а вызов производиться в глобальном