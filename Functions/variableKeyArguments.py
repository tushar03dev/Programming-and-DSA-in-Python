def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

print_kwargs(fname="tushar",lname="sharma")
print_kwargs(lname="sharma")
print_kwargs(fname="tushar")