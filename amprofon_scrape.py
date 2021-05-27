import requests as r
import lxml.html as html
import csv

#Amprofon Certificaciones Link
amp_certif = 'https://amprofon.com.mx/es/pages/certificaciones.php'
table_head = '//table/thead/tr/th/text()'
table_content = '//table//tr//td'



def scrape_amprofon():
    try:
        response = r.get(amp_certif)
        if response.status_code == 200: 
            data = []
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            t_head_link = parsed.xpath(table_head)
            t_content_link = parsed.xpath(table_content)

            for i in range(0, len(t_content_link)) :
                data.append(t_content_link[i].text_content().lower())
            
            with open('certificaciones.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(t_head_link)
                
                for artist in range(0, len(data), 7) :
                    writer.writerow(data[artist : artist + 7 ])
                print('CSV creado en la carpeta')

        else:
            raise ValueError(f'Error: {status_code}')
    
    except ValueError as ve:
        print(ve)


def run():
    scrape_amprofon()

if __name__ == '__main__':
    run()