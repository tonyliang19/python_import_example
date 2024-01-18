# This file helps to run python and test functionality
print("\nHello World")

print("Trying to import functions")
# The good one that has __init__.py file
try:
  print("Importing the one with __init__.py, it should work")
  from good_pkg.good_sum import good_sum
  print("Imported")
except Exception as e:
  print("It should not fail here, if failed, then cause is:")
  print(e)
# The bad one that does not have __init__.py
try:
  print("Trying to import the one without __init__.py, should NOT work")
  from bad_pkg.bad_sum import bad_sum
except Exception as e:
  print("It should fail, and cause is:")
  print(e)
