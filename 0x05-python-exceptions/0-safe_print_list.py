def safe_print_list(my_list=[], x=0):

  counter = 0
  for i in range(x):
    try:
      print(my_list[i], end="")
      counter += 1
    except IndexError:
      break

  print()
  return counter


if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 5]
  print(safe_print_list(my_list, 3))
  print(safe_print_list(my_list, 10))
