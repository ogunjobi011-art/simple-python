try:
    file.write("data.json","w+")
    file.seek()
except:
    print("An error occurred while writing to the file.")