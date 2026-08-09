with open("invoice.txt", "r") as file:
    for line in file:
        print(line.strip())

try:
    with open("abc.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist.")

""" 
with open("invoice_output.txt","a") as file:
    file.write("Pestpac Invoice2\n")
    file.write("Customer: Sai\n")
    file.write("Cost: 1000\n")
    file.write("Technican: Phanish\n") """
