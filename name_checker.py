test = "test.jpg"

# Name checker section
class File:
   
    tags = ""
    ext = ""

    def __init__(self, name):
        self.name = name

def name_splitter (filename_comp):
    if "." not in filename_comp:
        file = File(filename)
        file.ext = "none"
        return [file.name, file.ext]
    else:    
        name_ext = filename_comp.split(".")
        name = name_ext[0]
        ext = name_ext[1]
        file = File(name)
        return [file.name, file.ext]

def tagger(filename, ext):
    if "-" in filename:
        filename.tags = (filename[:-filename.index("-")]).split(" ")
    else:
        if ext == "none":
            filename.tags = "untagged"
            return [filename, filename.tags, ext]

        

# Debug
print(name_splitter(test))

        
