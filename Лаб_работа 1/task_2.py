# TODO Найдите количество книг, которое можно разместить на дискете
Volume_disc = 1.44 # в Мегабайтах
Num_of_pages = 100
Num_of_lines_per_pages = 50
Num_of_sym_per_line = 25
inf_one_sym = 4 # в байтах

Volume_book = Num_of_pages * Num_of_lines_per_pages * Num_of_sym_per_line * inf_one_sym / 1024**2 # в Мегабайтах


print("Количество книг, помещающихся на дискету:", int(Volume_disc // Volume_book))
