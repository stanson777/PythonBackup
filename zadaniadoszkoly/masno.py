def czy_palindrom(zdanie):
    zdanie="".join(zdanie.split())
    return zdanie.lower()==zdanie.lower()[::-1];



print(czy_palindrom('Kobyła ma mały bok'))
