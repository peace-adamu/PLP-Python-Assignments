


def modified_file():
    input_file = "requirements.txt"
    output_file = "modified_file"

    try:
        with open(input_file, "r") as infile:
            document = infile.read()
            modified_document = document.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_document)
            print(f"Modified document written to {output_file}")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found")
    except IOError:
        print(f"Error: Could not read the file")
    except Exception as e:
        print(f"An unexcepted error occured: {e}")


modified_file()
