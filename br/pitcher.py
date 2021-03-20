from requests_html import Element, HTMLResponse
from service import get_element


class Pitcher:
    COLUMNS = [
        'url',
        'name',
        'W',
        'L',
        'W_per',
        'ERA',
        'RA9',
        'G',
        'GS',
        'GF',
        'CG',
        'SHO',
        'SV',
        'IP',
        'H',
        'R',
        'ER',
        'HR',
        'BB',
        'IBB',
        'SO',
        'HBP',
        'BK',
        'WP',
        'BF',
        'WHIP',
        'H9',
        'HR9',
        'BB9',
        'SO9',
        'SO_per_BB',
    ]

    @classmethod
    def get_player_npb_stats(cls, url: str, name: str, response: HTMLResponse) -> list:
        """
        NPB通算成績
        """
        results = []
        tfoot = get_element(selector='#standard_pitching > tfoot', response=response)
        for tr in tfoot.find('tr'):
            level = tr.find('td:nth-child(3)', first=True)
            if level.text == 'NPB':
                results.append(cls.get_player_stats(element=tr, url=url, name=name))
        return results

    @classmethod
    def get_player_stats(cls, element: Element, url: str, name: str) -> dict:
        """
        成績
        """
        return {
            'url': url,
            'name': name,
            'W': element.find('td:nth-child(5)', first=True).text,
            'L': element.find('td:nth-child(6)', first=True).text,
            'W_per': element.find('td:nth-child(7)', first=True).text,
            'ERA': element.find('td:nth-child(8)', first=True).text,
            'RA9': element.find('td:nth-child(9)', first=True).text,
            'G': element.find('td:nth-child(10)', first=True).text,
            'GS': element.find('td:nth-child(11)', first=True).text,
            'GF': element.find('td:nth-child(12)', first=True).text,
            'CG': element.find('td:nth-child(13)', first=True).text,
            'SHO': element.find('td:nth-child(14)', first=True).text,
            'SV': element.find('td:nth-child(15)', first=True).text,
            'IP': element.find('td:nth-child(16)', first=True).text,
            'H': element.find('td:nth-child(17)', first=True).text,
            'R': element.find('td:nth-child(18)', first=True).text,
            'ER': element.find('td:nth-child(19)', first=True).text,
            'HR': element.find('td:nth-child(20)', first=True).text,
            'BB': element.find('td:nth-child(21)', first=True).text,
            'IBB': element.find('td:nth-child(22)', first=True).text,
            'SO': element.find('td:nth-child(23)', first=True).text,
            'HBP': element.find('td:nth-child(24)', first=True).text,
            'BK': element.find('td:nth-child(25)', first=True).text,
            'WP': element.find('td:nth-child(26)', first=True).text,
            'BF': element.find('td:nth-child(27)', first=True).text,
            'WHIP': element.find('td:nth-child(28)', first=True).text,
            'H9': element.find('td:nth-child(29)', first=True).text,
            'HR9': element.find('td:nth-child(30)', first=True).text,
            'BB9': element.find('td:nth-child(31)', first=True).text,
            'SO9': element.find('td:nth-child(32)', first=True).text,
            'SO_per_BB': element.find('td:nth-child(33)', first=True).text,
        }
