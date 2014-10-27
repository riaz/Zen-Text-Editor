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
                str = 'package main\n\nimport "fmt"\n\nfunc main(){\n\tfmt.Println("Hello, World")\n}'
                
        elif lang == 'Asm':
                str = 'section .text\norg 0x100\n\tmov\tah,0x9\n\tmov\tdx,hello\n\tint\t0x21\n\n\tmov\tax,0x4c00\n\tint\t0x21\n\nsection .data\nhello:db  "Hello, World!",13,10,"$"'
                
        elif lang == 'Perl':
                str = 'print "Hello World!"\n'
                
        elif lang == 'Haskell':
                str = 'module Main where\n\nmain :: IO()\nmain = putStrLn "Hello, World!"'
                
        elif lang == 'Ruby':
                str = 'puts "Hello World!\n\n$stdout.puts "Hello World!"'
                
        elif lang == 'C#':
                str = 'using System;\nclass HelloWorld\n{\n\tstatic void Main()\n\t{\n\t\tSystem.Console.WriteLn("Hello World");\n\t}\n}'
                
        elif lang == 'Erlang':
                str = '-module(hello).\n-export([hello_world/0]).\n\nhello_world() -> io.fwrite("Hello, World").',
                
        elif lang == 'Javascript':
                str = 'var a=10,b=20,sum;\n\nsum = a + b;\n\ndocument.writeln("Sum of a + b = " + sum);\n\ndocument.writeln("Hello World");'
                
        elif lang == 'ActionScript':
                str = 'package\n{\n\timport flash.display.Sprite;\n\n\tpublic class ActionScript3 extends Sprite\n\t{\n\t\tpublic function ActionScript3()\n\t\t{\n\t\t\ttrace("Hello World");\n\t\t}\n\t}\n}'
                
        elif lang == 'Lua':
                str = 'print "Hello, World!"'
                
        elif lang == 'Pascal':
                str = 'program HelloWorld(output);\nbegin\n\tWriteLn("Hello World!")\nend.'
                
        elif lang == 'Fortran':
                str = 'print *,"Hello World"'
                
        elif lang == 'Tcl':
                str = 'puts "Hello, World"'
                
        elif lang == 'Bash':
                str = 'echo "Hello World"'
                
        elif lang == 'Batch':
                str = 'rem "Welcome to Batch Programming"\n\necho "Hello World"'
                
        elif lang == 'VBScript':
                str = 'WScript.Echo("Hello,World")'
                
        elif lang == 'Html':
                str = '<html>\n<head>\n\t<title>\n\t\tHello World\n\t</title>\n\t<script></script>\n</head>\n<body>\n\tHello,World\n</body>\n</html>'
                
        elif lang == 'Xml':
                str = '<xml>\n<text>\n\tHello World\n</text>\n</xml>'
                
        elif lang == 'NodeJS':
                str = 'console.log("Hello World")'
                
        elif lang == 'Abap':
                str = 'PROGRAM helloworld\n\nWRITE "hello world".'
                
	return str

if __name__ == '__main__':
	print 'insertSnippet'
