def read_file():
    out = open("periodic_table.html", "w")
    out.write("<!DOCTYPE html>\n")
    out.write("<html lang=\"en\">\n")
    out.write("<head>\n")
    out.write("\t<title>Tableau de Mendeleiev</title>\n")
    out.write("\t<style>\n")
    out.write("\t\ttable {    width: 100%;}\n")
    out.write("\t\t.tr_full { border: 1px solid black; padding:1px;}\n")
    out.write("\t\t.tr_void { border: 0px; padding:1px;}\n")
    out.write("\t</style>\n")
    out.write("</head>\n")
    out.write("<body>\n")
    out.write("\t<table>\n")
    old = 998;
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
#            if old >= position:
#                print_start_line(out, old)
            if position - old > 1:
                out.write("\t\t\t<td colspan='"+ str(position - old - 1) + "' class=\"tr_void\"></td>\n")
            elif old >= position:
                if 998 != old:
                    out.write("\t\t</tr>\n")
                out.write("\t\t<tr>\n")
#            print_intermediate(out, old,position);
            out.write("\t\t\t<td class=\"tr_full\">\n")
            out.write("\t\t\t\t<h4>" + name + "</h4>\n")
            out.write("\t\t\t\t<ul>\n")
            out.write("\t\t\t\t\t<li>No " + number + "</li>\n")
            out.write("\t\t\t\t\t<li>" + small + "</li>\n")
            out.write("\t\t\t\t\t<li>" + molar + "</li>\n")
            out.write("\t\t\t\t</ul>\n")
            out.write("\t\t\t</td>\n")
            old = position;
    f.closed
    out.write("\t\t</tr>\n")
    out.write("\t</table>\n")
    out.write("</body>\n")
    out.write("</html>\n")
    out.closed
       
if __name__ == '__main__':
    read_file()
#    read_file()