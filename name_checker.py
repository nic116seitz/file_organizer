test = "test.jpg"

# Name checker section
class File:
   
    tags = []
    ext = ""

    def __init__(self, name):
        self.name = name

def name_splitter (filename_comp):
    if "." not in filename_comp:
        file = File(filename)
        file.ext = "none"
        return [ file, file.ext ]
    else:    
        name_ext = filename_comp.split(".")
        name = name_ext[0]
        ext = name_ext[1]
        file = File(name)
        file.ext = ext
        return [ file, ext ]

def tagger(file, ext):
    if "-" in file.name:
        filename_tags = (file.name[:-file.name.index("-")]).split(" ")
        file.tags = filename_tags[0]
        file.name = filename_tags[1]
    else:
        if ext == "none":
            file.tags.append("untagged") 
            return [filename, filename.tags, ext]
        # Image sorter
        elif (ext == "jpg" or 
            ext ==  "png" or 
            ext == "tiff" or 
            ext == "tif" or 
            ext == "webp" or
            ext == "gif"):
            file.tags.append("image")
            return [file.name, file.tags, ext]
        elif (ext == "mp3" or 
              ext == "wav"):
            file.tags.append("audio")
            return [file.name, file.tags, ext]



split_name = name_splitter(test)[0]       
split_ext = name_splitter(test)[1]
print(tagger(split_name, split_ext))
# Debug

        
