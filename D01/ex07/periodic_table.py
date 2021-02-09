def print_start_line(out, old):
    if 999 != old:
        out.write("\t\t</tr>\n")
    out.write("\t\t<tr>\n")
        
def print_intermediate(out, old, position):
    for i in range(old + 1, position):
                   out.write("\t\t\t<td class=\"tr_void\"/>\n")
    
def read_file():
    out = open("periodic_table.html", "w")
    out.write("<!DOCTYPE html>\n")
    out.write("<html lang=\"en\">\n")
    out.write("<head>\n")
    out.write("\t<style>\n")
    out.write("\t\t.tr_full { border: 1px solid black; padding:10px }\n")
    out.write("\t\t.tr_void { border: 0px padding:10px }\n")
    out.write("\t</style>\n")
    out.write("</head>\n")
    out.write("<body>\n")
    out.write("\t<table>\n")
    old = 999;
    with open('periodic_table.txt') as f:
        for element in f:
            end = element.index(" = position:")
            name = element[0: end]
            start = end + len(" = position:")
            end = element.index(", number:", start)
            position = int(element[start: end])
            start = end + len(", number:")
            end = element.index(", small: ", start)
            number = element[start: end]
            start = end + len(", small: ")
            end = element.index(", molar:", start)
            small = element[start: end]
            start = end + len(", molar:")
            end = element.index(", electron", start)
            molar = element[start: end]
            start = end + len(", number:")
            end = len(element) - 1
            electron = element[start: end]
            if old >= position:
                print_start_line(out, old)
            print_intermediate(out, old,position);
            out.write("\t\t\t<td class=\"tr_full\">\n")
            out.write("\t\t\t\t<h4>" + name + "</h4>\n")
#            out.write("\t\t\t\t<ul>\n")
#            out.write("\t\t\t\t\t<li>No " + number + "</li>\n")
#            out.write("\t\t\t\t\t<li>" + electron + " electron</li>\n")
#            out.write("\t\t\t\t</ul>\n")
            out.write("\t\t\t</td\n")
            old = position;
    f.closed
    out.write("\t\t</tr>\n")
    out.write("\t</table>\n")
    out.write("</body>\n")
    out.write("</html>\n")
    out.closed
def test1(i):
    i = i + 2;
    return i;

def test():
    i = 0;
    j = test1(i)
    print("i:", i, ", j:", j);
    a = (1, "toto", 3)
    print(a)
       
if __name__ == '__main__':
    read_file()
#    read_file()