# Open the text file in read mode
file_path = 'input.txt'  # Replace with the actual path to your file
list = []
with open(file_path, 'r') as file:
    # Read the contents of the file
    for line in file:
        # Process each line as needed
        content = line.strip()
        list.append('<option value="'+content+'">'+content+'</option>')

# Open the text file in write mode
file_path = 'output.txt'  # Replace with the actual path to your file
with open(file_path, 'w') as file:
    # Truncate the file to delete its contents
    file.truncate()
    # Write content to the file
    file.write('<select class="form-select form-control" aria-label="Default select example">\n')
    file.write('<option selected>-- Select --</option>\n')
    for line in list:
        file.write(line+'\n')