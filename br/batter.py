from requests_html import Element, HTMLResponse
from service import get_element


class Batter:
    COLUMNS = [
        'url',
        'name',
        'G',
        'PA',
        'AB',
        'R',
        'H',
        '2B',
        '3B',
        'HR',
        'RBI',
        'SB',
        'CS',
        'BB',
        'SO',
        'BA',
        'OBP',
        'SLG',
        'OPS',
        'TB',
        'GIDP',
        'HBP',
        'SH',
        'SF',
        'IBB',
    ]

    @classmethod
    def get_player_npb_stats(cls, url: str, name: str, response: HTMLResponse) -> list:
        """
        NPB通算成績
        """
        results = []
        tfoot = get_element(selector='#standard_batting > tfoot', response=response)
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
            'G': element.find('td:nth-child(5)', first=True).text,
            'PA': element.find('td:nth-child(6)', first=True).text,
            'AB': element.find('td:nth-child(7)', first=True).text,
            'R': element.find('td:nth-child(8)', first=True).text,
            'H': element.find('td:nth-child(9)', first=True).text,
            '2B': element.find('td:nth-child(10)', first=True).text,
            '3B': element.find('td:nth-child(11)', first=True).text,
            'HR': element.find('td:nth-child(12)', first=True).text,
            'RBI': element.find('td:nth-child(13)', first=True).text,
            'SB': element.find('td:nth-child(14)', first=True).text,
            'CS': element.find('td:nth-child(15)', first=True).text,
            'BB': element.find('td:nth-child(16)', first=True).text,
            'SO': element.find('td:nth-child(17)', first=True).text,
            'BA': element.find('td:nth-child(18)', first=True).text,
            'OBP': element.find('td:nth-child(19)', first=True).text,
            'SLG': element.find('td:nth-child(20)', first=True).text,
            'OPS': element.find('td:nth-child(21)', first=True).text,
            'TB': element.find('td:nth-child(22)', first=True).text,
            'GIDP': element.find('td:nth-child(23)', first=True).text,
            'HBP': element.find('td:nth-child(24)', first=True).text,
            'SH': element.find('td:nth-child(25)', first=True).text,
            'SF': element.find('td:nth-child(26)', first=True).text,
            'IBB': element.find('td:nth-child(27)', first=True).text,
        }
