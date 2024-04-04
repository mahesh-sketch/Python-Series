import aiohttp
import asyncio

async def api_calling():
    try:
        url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                jsondata = await response.json()
                if jsondata['statusCode'] == 200 and "data" in jsondata:
                    user_data = jsondata['data']
                    username = user_data['login']['username']
                    country = user_data['location']['country']
                    return username,country
                else:
                    raise Exception("No data found !")
    except Exception as e:
        print("Something went wrong!", e)

def main():
    try:
        username,country = asyncio.run(api_calling())
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print("Something went wrong !",e)
        

if __name__ == "__main__":
    main()
