#implicit
integer_number = 123
float_number = 1.23

number_baru = integer_number + float_number

print("Nilai : ",number_baru)
print("Tipe Data : ",type(number_baru))

#explicit
num_string = '12'
num_integer = 23

print("Tipe data dari num_string sebelum Type Casting:",type(num_string))

num_string = int(num_string)

print("Tipe data dari num_string setelah Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))
