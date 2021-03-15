from requests_html import HTMLResponse, HTMLSession, Element


def get_page(url: str) -> HTMLResponse:
    """
    URLで指定したページを取得する
    """
    session = HTMLSession()
    response = session.get(url)
    response.html.render(timeout=60)
    return response


def get_element(selector: str, response: HTMLResponse) -> Element:
    """
    指定したエレメントのみ取得
    """
    section = response.html.find(selector=selector, first=True)
    if section:
        return section
    raise Exception('page not found')
