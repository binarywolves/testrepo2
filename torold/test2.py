import pandas as pd
import os
import xlwings as xw

def convert_excels(folder, output_folder):
    def ...:
        ...

    @xw.func
    def select_input_folder():
        return xw.Book.caller().app.file_dialog(folder_title='Select input folder', multiselect=False).show()[0]

    @xw.func
    def select_output_folder():
        return xw.Book.caller().app.file_dialog(folder_title='Select output folder', multiselect=False).show()[0]

    @xw.func
    @xw.arg('folder', np.array, ndim=1)
    @xw.arg('output_folder', np.array, ndim=1)
    def process_files(folder, output_folder):
        if not os.path.exists(folder):
            raise ValueError(f"Folder '{folder}' does not exist.")
        if not os.path.exists(output_folder):
            raise ValueError(f"Folder '{output_folder}' does not exist.")
        files = os.listdir(folder)
        if len(files) == 0:
            print("No files uploaded")
        else:
            total_files = len(files)
            for i, file in enumerate(files, start=1):
                print(f"{i}/{total_files} in progress")
                ...
            print("\n\u2713 All files converted successfully")

    # Create an Excel ribbon tab "RegConv"
    xw.Book().ribbon.tabs.add("RegConv")
    
    # Add the "Input" button to the "RegConv" tab
    input_button = xw.Book().ribbon.tabs["RegConv"].groups.add("Input")
    input_button.button_on_action = "convert_excels.select_input_folder"
    input_button.icon = os.path.join(os.getcwd(), "input.png")
    
    # Add the "Output" button to the "RegConv" tab
    output_button = xw.Book().ribbon.tabs["RegConv"].groups.add("Output")
    output_button.button_on_action = "convert_excels.select_output_folder"
    output_button.icon = os.path.join(os.getcwd(), "output.png")
    
    # Add the "Process" button to the "RegConv" tab
    process_button = xw.Book().ribbon.tabs["RegConv"].groups.add("Process")
    process_button.button_on_action = "convert_excels.process_files"
    process_button.icon = os.path.join(os.getcwd(), "process.png")

    # Display a message to inform the user that the add-in was successfully loaded
    xw.Book().set_mock_caller()
    xw.Book().set_mock_environment()
    xw.Book().activate()
    xw.Book().sheets[0].range("A1").value = "The RegConv add-in has been successfully loaded!"

if __name__ == "__main__":
    convert_excels()
