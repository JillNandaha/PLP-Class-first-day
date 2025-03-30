def read_and_write_file():
    try:
        # Ask the user for the input file name
        input_filename = input("Enter the name of the file to read: ")
        
        # Open the file for reading
        with open(input_filename, "r") as file:
            content = file.read()
        
        # Modify the content (Example: Convert to uppercase)
        modified_content = content.upper()
        
        # Ask for the output file name
        output_filename = input("Enter the name of the file to write to: ")
        
        # Write the modified content to the new file
        with open(output_filename, "w") as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print("Error: The file you entered does not exist.")
    except IOError:
        print("Error: There was a problem reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()
