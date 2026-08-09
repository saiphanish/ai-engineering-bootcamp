customer = input("Customer Name:")
service = input("Service:")
cost = float(input("Cost:"))
gst = cost * 0.18
total = cost + gst

with open("invoice1.txt","a") as file:
    file.write("=" * 30 + "\n")
    file.write("Pestpac Invoice2\n")
    file.write("=" * 30 + "\n")
    
    file.write("Customer: Sai\n")
    file.write("Service : Bed Bugs\n")
    file.write("Cost: 1000\n")
    file.write(f"GST : {gst:.2f}\n")
    file.write(f"Total : {total:.2f}\n")

    file.write("=" * 30 + "\n")