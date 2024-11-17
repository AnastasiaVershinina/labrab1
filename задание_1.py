volume_of_disk_in_megabytes = 1.44
volume_of_disk_in_bytes = volume_of_disk_in_megabytes*1024*1024
number_of_lists_in_books = 100
number_of_strings = 50
number_of_symbols = 25
number_of_bytes_foe_one_symbol = 4
number_of_books = int(volume_of_disk_in_bytes//(number_of_lists_in_books*number_of_strings*number_of_symbols*number_of_bytes_foe_one_symbol))
print('Количество книг, помещающихся на дискету:', number_of_books)
