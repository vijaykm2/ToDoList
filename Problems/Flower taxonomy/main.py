iris = {}


def add_iris(id, species, petal_length, petal_width, **kwargs):
    new_iris = {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}
    for key, value in kwargs.items():
        new_iris.update({key: value})
    iris.update({id: new_iris})

#
# add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')
# print(iris)
