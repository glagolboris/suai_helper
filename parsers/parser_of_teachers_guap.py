from bs4 import BeautifulSoup
import aiohttp
import json


class ParserProfessors:
    def __init__(self, session: aiohttp.ClientSession, self_bot):
        self.session = session
        self.self_bot = self_bot

    async def get_professors(self) -> list:
        url = 'https://pro.guap.ru/professors?position=0&facultyWithChairs=389&subunit=0&fullname=&perPage=100'
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15'
        }
        async with self.session.get(url=url, headers=headers) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            professors = [professor.text.strip().replace("\n", "") for professor in soup.find_all('h5', class_='mb-sm-1 fw-semibold')]
            return professors

    async def send_data_to_bd(self):
        professors = await self.get_professors()
        dict_professors = {'professors': professors}

        self.self_bot.cursor.execute("""INSERT INTO professors(full_name) VALUES(%s)""", [json.dumps(dict_professors, indent=4)])
        self.self_bot.connection.commit()
