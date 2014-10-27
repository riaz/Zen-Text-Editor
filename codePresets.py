def insertSnippet(lang):
	if lang == 'C':
		str = '#include<stdio.h>\n\nint main(){\n\tprintf("Zen Editor v1.0");\n\treturn 0;\n}'
		
	elif lang == 'C++':
		str = '#include<iostream>\n\nusing namespace std;\nint main(){\n\tcout << "Zen Editor v1.0";\n\treturn 0;\n}'
		
	elif lang == 'Java':
                str = 'public class Hello\n{\n\tpublic static void main(String args[])\n\t{\n\t\tSystem.out.println("Hello World");\n\t}\n}'
                
        elif lang == 'Python':
                str = 'a = 10\nb=10\n\nfor i in range(1,10):\n\tprint i\n\nprint "Hello World"'
                
        elif lang == 'Go':
                str = 'Go'
                
        elif lang == 'Asm':
                str = 'section .text\norg 0x100\n\tmov\tah,0x9\n\tmov\tdx,hello\n\tint\t0x21\n\n\tmov\tax,0x4c00\n\tint\t0x21\n\nsection .data\nhello:db  "Hello, World!",13,10,"$"'
                
        elif lang == 'Perl':
                str = 'Perl'
                
        elif lang == 'Haskel':
                str = 'Haskel'
                
        elif lang == 'Ruby':
                str = 'Ruby'
                
        elif lang == 'C#':
                str = 'C#'
                
        elif lang == 'Erlang':
                str = 'Erlang',
                
        elif lang == 'Javascript':
                str = 'var a=10,b=20,sum;\n\nsum = a + b;\n\n document.writeln("Sum of a + b = " + sum);\n\ndocument.writeln("Hello World");'
                
        elif lang == 'ActionScript':
                str = 'package\n{\n\timport flash.display.Sprite;\n\n\tpublic class ActionScript3 extends Sprite\n\t{\n\t\tpublic function ActionScript3()\n\t\t{\n\t\t\ttrace("Hello World");\n\t\t}\n\t}\n}'
                
        elif lang == 'Lua':
                str = 'Lua'
                
        elif lang == 'Pascal':
                str = 'Pascal'
                
        elif lang == 'Fortran':
                str = 'Fortran'
                
        elif lang == 'Tcl':
                str = 'Tcl'
                
        elif lang == 'Bash':
                str = 'Bash'
                
        elif lang == 'Batch':
                str = 'Batch'
                
        elif lang == 'VBScript':
                str = 'VBScript'
                
        elif lang == 'Html':
                str = 'Html'
                
        elif lang == 'Xml':
                str = 'Xml'
                
        elif lang == 'NodeJS':
                str = 'NodeJS'
                
        elif lang == 'Abap':
                str = 'PROGRAM helloworld\n\nWRITE "hello world".'
                
	return str

if __name__ == '__main__':
	print 'insertSnippet'
