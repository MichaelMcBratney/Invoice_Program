import os, csv, sys
from MyInvoiceHandler import MyInvoiceHandler

import HomePage
import EndPage

number = 1  # Keeps track of which number file the program is on for naming purposes


def resource_path(relative):
    # Method to find absolute path of given resource
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )


page1 = HomePage.HomePage()  # Creates an instance of the home page
page1.make_window()  # Displays the homepage


if page1.get_paths() != 0:
    for filename in page1.get_paths():

        final_product = MyInvoiceHandler()  # Creates an instance of the invoice handler

        if filename.endswith(".csv"):
            invoice_file = str(filename)

            inc_cols = [2, 14, 15, 47, 46, 56]  # Only provides relevant columns from the CSV file

            with open(filename, newline='') as textfile:
                my_reader = csv.reader(textfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)  # Creates a CSV reader
                count = 0
                for row in my_reader:

                    if count == 1:
                        # Uses setter methods to set invoice handler properties from the CSV file
                        final_product.set_inv_num(row[0])
                        final_product.set_inv_amt(row[15], row[14])
                        final_product.set_date(row[2])
                        final_product.set_short_amt(row[13])
                        final_product.set_amt_payable()
                        final_product.set_dept(row[4])

                    if count > 0:
                        new_text = list(row[i] for i in inc_cols)
                        final_product.compare_list(new_text, resource_path('guide.txt'))  #

                    count += 1

            final_product.inv_round() # Rounds all values to dollar amounts
            final_product.format_final_values()  # Formats all numbers in order for them to be added to the word document.
            final_product.write_to_word(number, page1.getDir(), resource_path('Invoice_Form.docx'))  # Adds all values to microsoft word template.
            final_product.get_innacuracies()  # Checks for inaccuracies with the listed price
            final_product.add_new(resource_path('guide.txt'))  # Updates the current record of known food prices
            number += 1

    page2 = EndPage.EndPage()
    page2.make_window()
