def extract_function(_line):
    words = _line.split(" ")
    for index,word in  enumerate(words) :
        if word in ["function","def"]:
            function_name =  words[index+1]
            arguements = function_name.split("(")[1].split(',')
            dict = {
                'name':function_name.split("(")[0],
                'arguments':arguements
            }
            return dict
def extract_class(_line):
    words = _line.split(" ")
    for index,word in  enumerate(words) :
        if word in ["class"]:
            class_name =  words[index+1]
            print(class_name)
            return class_name

def is_comment_start(_line):
    comment_tags = ["'''","/*"]
    for tag in comment_tags:
        if tag in _line:
            return True
    return False
def is_comment_end(_line):
    comment_tags = ["'''","*/"]
    for tag in comment_tags:
        if tag in _line:
            return True
    return False

def interpret_script(_path):
    html_blocks = []
    count = 0
    with open(_path) as fp:
        Lines = fp.readlines()
        comment = False
        html = ""
        comment_count = 0
        for line in Lines:
            if is_comment_start(line) and comment == False :
                    comment = True
                    html = "<div class = 'comment'><p>"
                    continue
            if is_comment_end(line) and comment == True :
                    comment = False
                    html += "</p></div>"
                    html_blocks.append(html)
            if comment == False:
                function_ = extract_function(line)
                class_ = extract_class(line)
                if function_ :
                    html_blocks.append("<div class = 'function'>"+function_.get("name")+" arguments : "+" , ".join(function_.get("arguments"))+"</div>")
                if class_ :
                    html_blocks.append("<div class = 'class'>"+class_.get("name")+"</div>")
            
            if comment  == True:
                if line != "":
                    html +='<br>'+line
                    


            print(comment)

            
           # html = extract_function(line)
    final_html = "\n".join(html_blocks)
    print(final_html )
    return final_html

def create_html(script_path,html_path):
    html = ""
    html+=get_header()
    html+=interpret_script(script_path)
    html+=get_footer()
    with open(html_path, "w") as fp:
        fp.write(html )
    


def get_header():
    return '''
    <html>
    <head>
    <style>
    .function{
       color:blue;
    }
    </style>
    </head>
    <body>
    
    '''
def get_footer():
     return '''
    </body>
</html>
'''


class Comment:
    def __init__(self):
        self.starts=["'''","*/"]
        self.ends=["'''","*/"]
        self.current_start_index = 0

    def is_start(self,_string):
        for index,start in enumerate(self.starts):
            if start  in _string:
                self.current_index = index
                return True
        return False
    def is_end(self,_string):
        if self.ends[self.current_start_index]  in _string:
            return True
        return False

            

create_html("D:/1_TRAVAIL/WIP/ALARIGGER/CODING/PYTHON/REPOSITORIES/AL_Doc/Test_material/test_script.py","D:/1_TRAVAIL/WIP/ALARIGGER/CODING/PYTHON/REPOSITORIES/AL_Doc/Test_material/test_script.html")




'''

python D:/1_TRAVAIL/WIP/ALARIGGER/CODING/PYTHON/REPOSITORIES/AL_Doc/generate_html.py
'''