class Data:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    
    def __str__(self):
        res = "Data for: " + str(self.b) + "\n"
        res += "a " + str(self.a) + "\n"
        res += "c " + str(self.c) + "\n"
        res += "Amount in e " + str(f) + "\n"
        res += "Percentage " + str(self.f) + "\n"
        return res
        

values = []
f = open("data.csv", "r")

for line in f.readlines():
    sep_values = line.split(",")
    d = Data(int(sep_values[0]), sep_values[1], sep_values[2], int(sep_values[3]), int(sep_values[4]), float(sep_values[5]))
    values.append(d)

f.close()

def sort_f(d):
    return d.f

def sort_e(d):
    return d.e

def sort_D(d):
    return d.D

def print_percent(start, end):
    result = ""
    for x in sorted(values, key = sort_f)[start:end]:
        result += str(x)
        result += "\n"

    return result

def print_sort_e(start, end):
    result = ""
    for x in sorted(values, key = sort_e)[start:end]:
        result += str(x)
        result += "\n"

    return result

def print_sort_D(start, end):
    result = ""
    for x in sorted(values, key = sort_E)[start:end]:
        result += str(x)
        result += "\n"

    return result


if __name__ == "__main__":

    #print(str(len(values)))
    while True:
        print("Enter the starting and ending indices of the values you wish to view\n")
        start = int(input())
        end = int(input())
        print("Chose how to sort data:\n")
        print("1 for %, 2 for E and 3 for D\n")
        print("Press -1 to terminate\n")
        value = int(input())
        if value == -1:
            print("Closing the program \n")
            break
        elif value == 1:
            print(print_sort_F(start, end))
        elif value == 2:
            print(print_sort_E(start, end))
        elif value == 3:
            print(print_sort_D(start, end))
     
