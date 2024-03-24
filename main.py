# Importing Random module.
import random
# Importing PrettyTable for designing the grid.
from prettytable import PrettyTable as percTable


# Function for the main program.
def Main_prog():
    Columns = None
    Rows = None

    while True:     # Getting the grid size from the user.
        perc_dimension = input("\n\nYour Grid should be in between 3x3 or 9x9...\n\nPerc : ").strip()

        if perc_dimension == "":        # If the user just press the enter key then the default grid will create (5x5)
            Columns = 5
            Rows = 5
            break
        else:
            try:
                perc_dimension = perc_dimension.lower().split("x")
                Rows = int(perc_dimension[0])
                Columns = int(perc_dimension[1])

                # If the user enters a grid value more than 9x9 and less than 3x3 then,
                # the code will break and asking the user to input the valuer again.
                if Columns < 10 and Rows < 10 and Columns != 2 and Rows != 2:
                    break
            except:
                continue

    rowNum_List = [random.randint(0, 99) for x in range(Columns * Rows)]
    column_List = [rowNum_List[i:i + Rows] for i in range(0, len(rowNum_List), Rows)]
    List_Results = []

    # Printing the "OK" and "NO" Values.
    for i in range(Columns):
        Results = " OK"
        for j in range(Rows):
            if int(column_List[i][j]) < 10:
                Results = " NO"
                column_List[i][j] = "  "
        List_Results.append(Results)
    RowList = []

    for i in range(Rows):
        Rows = []
        for j in range(Columns):
            Rows.append(column_List[j][i])
        RowList.append(Rows)

    Printing_grid(RowList, Columns, List_Results)
    Write_file(RowList, List_Results)
    html_page(RowList, List_Results)


# Function for Printing the grid.
def Printing_grid(list_rows, Columns, Results_list):
    for i in list_rows:
        print("+----" * Columns + "+")  # Design of the Grid.
        for j in i:
            print("| {0} ".format(j), end="")
        print("|")
    print("+----" * Columns + "+")

    for i in Results_list:
        print(" {0} ".format(i), end="")


# Function for Writing the file.
def Write_file(list_rows, Results_list):
    i = 0
    while True:
        # Text file is created when the program is running each and every time. (Format = Perc_TextFile (0) )
        Text_File = "Perc_TextFile (" + str(i) + ").txt"
        try:
            open(Text_File)
            i += 1
            continue
        except:
            file = open(Text_File, "w")
            for i in list_rows:
                for j in i:     # Printing the grid values to the TextFile.
                    file.write("    {0}".format(j))
                file.write("\n\n")
            for i in Results_list:      # Printing "OK" and "NO" at the end of each column.
                file.write("   {0}".format(i))
            file.close()
            break


# Function for the HTML Page.
def html_page(list_rows, Results_list):
    # Using PrettyTable.
    html_table = percTable()
    html_table.add_rows(list_rows)  # Getting values for the table.
    html_table.add_row(Results_list)

    Web_Page = open("Perc_HTML.html", "w")  # Creating the WebPage ( Format = Perc_HTML.html )
    # Writing the code for the HTML Page.
    Web_Page.write("""
        <html>\n
            <head>\n
                <style>\n
                body {background-color: lightblue;}
                td, table {\n\t\n\tborder: 5px solid black;\n\t border-collapse: collapse;\n\t text-align: center;\n}\n
                th {\n\tdisplay:none;\n}\n
                </style>\n
                <h1><center><b><font color = "Black">Percolation</b>
            </head>\n
                <body>
        """)
    Web_Page.write(html_table.get_html_string(attributes={"id": "perc_table", "class": "CW"}))
    Web_Page.write("\n</body>\n</html>")
    Web_Page.close()


# Running the Main Program.
if __name__ == "__main__":
    Main_prog()
