import os, pdfkit


path = r"C:\Program Files\wkhtmltopdf\bin"
os.environ["PATH"] += os.pathsep + path

pdfkit.from_file('template\PrintTemplate\getComeDaysData.html', 'passDataReport.pdf')

os.environ.update()