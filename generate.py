__DATA = []

with open("data.txt","r") as _DATA:
    for _line in _DATA:
        __DATA.append( _line.replace("\n","").strip("\t"))
    
    
for _dataLine in __DATA:
    _dataLine =  _dataLine.split("\t")
    with  open("patron.html","r") as _FILE:
        _FILECONTENT = []
        _NEWFILECONTENT = []

        for _line in _FILE:
            if("-" in _line[0] ):
                _newline = "     <div id='div_title'> Prueba %s/20</div>" % (_dataLine[0])
                print _newline
                _NEWFILECONTENT.append(_newline)
            elif("+" in _line[0] ):
                _newline = "<div id='big_number'> %s </div> " % (_dataLine[0])
                _NEWFILECONTENT.append(_newline)
            elif("**" in _line[0:2] ):
                _newline = "                      window.location.href = '%s.html';" %( str ( int ( _dataLine[0])+1) )
                _NEWFILECONTENT.append(_newline)
            elif(_line[0] == "*"):
                _newline = "               <button id='play_button' onclick='play_sounds(keyNoteToFreq(%s),keyNoteToFreq(%s),keyNoteToFreq(%s))'>Reproducir </button>" % (_dataLine[1],_dataLine[2],_dataLine[3])
                _NEWFILECONTENT.append(_newline)
            else:
                _NEWFILECONTENT.append(_line)


        _FILENAME = "%s.html" %( str( _dataLine[0]))
        with open( "server/static/"+_FILENAME,"w") as _OUTPUT_FILE:
                _OUTPUT_FILE.writelines(_NEWFILECONTENT)
