import httpx
from bs4 import BeautifulSoup

class FreeSearchService:
    def __init__(self):
        self.timeout = 10

    async def search(self, query: str) -> list[dict]:
        """Search using DuckDuckGo free search"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "https://duckduckgo.com/",
                    params={"q": query},
                    timeout=self.timeout,
                    follow_redirects=True
                )

                soup = BeautifulSoup(response.text, 'html.parser')
                results = []

                for result in soup.find_all('div', class_='web-result')[:3]:
                    try:
                        title_elem = result.find('a', class_='result__a')
                        snippet_elem = result.find('a', class_='result__snippet')

                        if title_elem and snippet_elem:
                            results.append({
                                "title": title_elem.get_text(strip=True),
                                "snippet": snippet_elem.get_text(strip=True),
                                "link": title_elem.get('href', '')
                            })
                    except:
                        continue

                return results
        except Exception as e:
            print(f"Search error: {e}")
            return []

    async def search_ingredient(self, ingredient: str) -> list[dict]:
        """Search specific ingredient halal info"""
        query = f"{ingredient} halal haram"
        return await self.search(query)

    async def search_product(self, product_name: str) -> list[dict]:
        """Search specific product halal info"""
        query = f"{product_name} halal certification"
        return await self.search(query)

