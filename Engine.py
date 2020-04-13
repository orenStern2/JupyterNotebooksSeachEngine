from IPython.display import display, Markdown, clear_output
import ipywidgets as widg
from ipywidgets import Button, Layout
import os


root_directory = 'Path to your *.ipynb files'


input_text = widg.Text(
    value = "",
    placeholdr='Word to search for',
    description='String:',
    disabled=False
)

box_layout = Layout(display='flex',
                    flex_flow='row',
                    border='solid',
                    width='10%')


button = widg.Button(
    description='Search for it...',
    button_style='success',
    #layout=box_layout
)

out = widg.Output()

def on_button_clicked(_):

    #linking function with output

    with out:
        clear_output()
        def find_text_in_file(path, file):
            result = []
            with open(path+"/"+file, 'r', encoding="utf-8") as search:
                for line in search:
                    line = line.rstrip()
                    if input_text.value in line:
                        if len(line) < 60:
                            return path, file, line
                        else:
                            return path, file,"the line is too long to display"



        list_files_results = []
        show_up = 0
        fc = 0
        for path, subdir, files in os.walk(root_directory):
            fc += 1
            for file in files:
                if "ipynb" in file and ".ipynb_checkpoints" not in path:

                    word_exists = find_text_in_file(path, file)
                    if word_exists is not None:
                        path_to_file, file_name, line_included_the_searched_word = find_text_in_file(path, file)
                        for char in path_to_file:
                            path_to_file = path_to_file.replace("/", "\\")

                        list_files_results.append("{}\{}\n\n{}\n".format(path_to_file, file_name,line_included_the_searched_word))

        for (i, item) in enumerate(list_files_results, start=1):
            print("{}. {}".format(i, item))
            show_up = i
        if show_up > 0:
            print("\n\n({} results)".format(show_up))
        else:
            print("No matches found.\nSearched in {} files,".format(fc))
# linking button and function toghter using button's method
button.on_click(on_button_clicked)
#displaying button and it's output toghter
widg.VBox([input_text, button, out])
