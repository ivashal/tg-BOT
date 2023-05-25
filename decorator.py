def check(input_func):
    def output_func(*args):
        name = args[0]
        age = args[1]
        if age < 0: age = 1
        input_func(name, age)
    return output_func


@check
def print_person(name, age):
    print(f"Name: {name} Age: {age}")


print_person("Tom", 38)
print_person("Bob", -4)

