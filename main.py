import tkinter as tk

window = tk.Tk()
window.title("Salary Comparison")
def clear_results():
    for label in result_labels:
        label.destroy()

def compare():
    clear_results()

    tpt = 0
    ida = 38.3
    cafetaria = 26
    hra = 18

    bp = float(basic_pay_entry.get())
    level = int(pay_level_var.get())
    da = float(da_percentage_entry.get())
    cea = int(num_children_entry.get())

#calculation logic

    nbp = round((bp * ((1 + (da / 100)) / (1 + (ida / 100)))), 10)

    if nbp < 20000 and level == 1:
        nbp = 20000

    if nbp < 21000 and level == 2:
        nbp = 21000

    if nbp < 23000 and level == 3:
        nbp = 23000

    daval = round(bp * (da / 100))
    idaval = round(nbp * (ida / 100))

    hraval = round(bp * (hra / 100))
    ihraval = round(nbp * (hra / 100))

    ceaval = cea * 2250

    if level >= 7:
        newsval = 500
    else:
        newsval = 0

    if level >= 13:
        televal = 2000
    else:
        televal = 0

    if level >= 1 and level <= 2:
        if bp >= 24200:
            tpt = round(1800 * (1 + (da / 100)))
        else:
            tpt = round(900 * (1 + (da / 100)))
    elif level >= 3 and level <= 8:
        tpt = round(1800 * (1 + (da / 100)))
    elif level >= 9:
        tpt = round(3600 * (1 + (da / 100)))

    cafetariaval = round(nbp * (cafetaria / 100))

    allow = tpt + ceaval + newsval + televal

    if allow > cafetariaval:
        sca = allow - cafetariaval
    else:
        sca = 0

    #result label
    result_labels = []
    row_index = 5
    result_values = {
        "Basic Pay:": f"{bp:.2f}",
        "New Basic Pay:": f"{nbp:.2f}",
        "DA:": f"{daval:.2f}",
        "IDA:": f"{idaval:.2f}",
        "HRA:": f"{hraval:.2f}",
        "I HRA:": f"{ihraval:.2f}",
        "TPT:": f"{tpt:.2f}",
        "Cafeteria Allowance:": f"{cafetariaval:.2f}",
        "CEA:": f"{ceaval:.2f}",
        "Special Comp. Allowance:": f"{sca:.2f}",
        "Newspaper Allowance:": f"{newsval:.2f}",
        "Telephone Allowance:": f"{televal:.2f}",
        "Total Existing (Without LTC):": f"{bp + daval + hraval + tpt + ceaval:.2f}",
        "Total Proposed:": f"{nbp + idaval + ihraval + cafetariaval + sca:.2f}"
    }
     
     
    for label_text, value in result_values.items():
        result_label = tk.Label(window, text=label_text)
        result_label.grid(row=row_index, column=0, sticky="W")
        result_labels.append(result_label)

        result_value = tk.Label(window, text=value)
        result_value.grid(row=row_index, column=1)
        result_labels.append(result_value)

        row_index += 1

#input components
basic_pay_label = tk.Label(window, text="Basic Pay:")
basic_pay_label.grid(row=0, column=0, sticky="W")
basic_pay_entry = tk.Entry(window)
basic_pay_entry.grid(row=0, column=1)

pay_level_label = tk.Label(window, text="Pay Level:")
pay_level_label.grid(row=1, column=0, sticky="W")
pay_level_var = tk.StringVar()
pay_level_dropdown = tk.OptionMenu(window, pay_level_var, *range(1, 11))
pay_level_dropdown.grid(row=1, column=1)

da_percentage_label = tk.Label(window, text="DA Percentage:")
da_percentage_label.grid(row=2, column=0, sticky="W")
da_percentage_entry = tk.Entry(window)
da_percentage_entry.grid(row=2, column=1)

num_children_label = tk.Label(window, text="Number of Children for CEA:")
num_children_label.grid(row=3, column=0, sticky="W")
num_children_entry = tk.Entry(window)
num_children_entry.grid(row=3, column=1)

compare_button = tk.Button(window, text="Compare", command=compare)
compare_button.grid(row=4, columnspan=2)

result_labels = []
row_index = 5
window.mainloop()
