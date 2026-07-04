def file_handling():
    f=open("demo",mode="w+",buffering=1,encoding="utf-8",errors="strict",newline="\n")
    f.write("line1\n")
    f.writelines("line2\n""line3\n")