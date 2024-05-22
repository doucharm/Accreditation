import aiohttp
class DBWriter:
    def __init__(self, username="johnson.newbie@world.com", password="johnson.newbie@world.com"):
        self.username = username
        self.password = password
        self.token = None
        pass
    async def getToken(self):
        if self.token:
            return self.token
        keyurl = "http://localhost:33001/oauth/login3"
        async with aiohttp.ClientSession() as session:
            async with session.get(keyurl) as resp:
                keyJson = await resp.json()
            payload = {"key": keyJson["key"], "username": self.username, "password": self.password}
            async with session.post(keyurl, json=payload) as resp:
                tokenJson = await resp.json()
        self.token = tokenJson.get("token", None)
        return self.token
    async def queryGQL(self, query, variables):
        gqlurl = "http://localhost:33001/api/gql"
        token = self.token
        if token is None:
            token = await self.getToken()
        payload = {"query": query, "variables": variables}
        cookies = {'authorization': token}
        async with aiohttp.ClientSession() as session:
            async with session.post(gqlurl, json=payload, cookies=cookies) as resp:
                if resp.status != 200:
                    text = await resp.text()
                    raise Exception(f"Unexpected GQL response", text)
                else:
                    response = await resp.json()
                    return response  
