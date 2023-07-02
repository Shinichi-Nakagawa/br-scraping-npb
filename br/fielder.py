from requests_html import Element, HTMLResponse
from service import get_element


class Fielder:
    COLUMNS = [
        'url',
        'name',
        'Age',
        'POS',
        'G',
        'GS',
        'CG',
        'Inn',
        'Ch',
        'PO',
        'A',
        'E',
        'DP',
        'Fld_per',
        'RF9',
        'RFG',
        'PB',
        'WP',
        'SB',
        'CS',
        'CS_per',
        'lg_CS_per',
        'PickOff',
    ]

    @classmethod
    def get_player_npb_stats(cls, url: str, name: str, response: HTMLResponse) -> list:
        """
        NPB通算成績
        """
        results = []
        tfoot = get_element(selector='#standard_fielding > tfoot', response=response)
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
            'Age': element.find('td:nth-child(4)', first=True).text,
            'POS': element.find('td:nth-child(5)', first=True).text,
            'G': element.find('td:nth-child(6)', first=True).text,
            'GS': element.find('td:nth-child(7)', first=True).text,
            'CG': element.find('td:nth-child(8)', first=True).text,
            'Inn': element.find('td:nth-child(9)', first=True).text,
            'Ch': element.find('td:nth-child(10)', first=True).text,
            'PO': element.find('td:nth-child(11)', first=True).text,
            'A': element.find('td:nth-child(12)', first=True).text,
            'E': element.find('td:nth-child(13)', first=True).text,
            'DP': element.find('td:nth-child(14)', first=True).text,
            'Fld_per': element.find('td:nth-child(15)', first=True).text,
            'RF9': element.find('td:nth-child(16)', first=True).text,
            'RFG': element.find('td:nth-child(17)', first=True).text,
            'PB': element.find('td:nth-child(18)', first=True).text,
            'WP': element.find('td:nth-child(19)', first=True).text,
            'SB': element.find('td:nth-child(20)', first=True).text,
            'CS': element.find('td:nth-child(21)', first=True).text,
            'CS_per': element.find('td:nth-child(22)', first=True).text,
            'lg_CS_per': element.find('td:nth-child(23)', first=True).text,
            'PickOff': element.find('td:nth-child(24)', first=True).text,
        }
