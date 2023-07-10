from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm
import pandas as pd
import io
import glob

passwords = [str(i) for i in range(0,10000)]


files = glob.glob("/content/*.pdf")

for filename in files:
    reader = PdfReader(filename)
    writer = PdfWriter()


    for i in tqdm(passwords):
        try :
            reader.decrypt(i)
            for page in reader.pages:
                writer.add_page(page)
            with open("decrypted-pdf.pdf", "w") as f:
                ans = i
                break
        except:
            pass
        
    temp  = filename.split("/")[-1].split("_")[-1] + " : " + str(ans) + "\n"
    f = open('decoded_passwords.txt', 'at')
    f.write(temp)
    f.close()
