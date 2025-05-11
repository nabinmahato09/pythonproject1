import requests

def random_youtube_video():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos?page=1&limit=10&query=javascript&sortBy=keep%20one%3A%20mostLiked%20%7C%20mostViewed%20%7C%20latest%20%7C%20oldest"
    response = requests.get(url)
    data = response.json()
    
    if data.get("success") and "data" in data:
        user_data = data["data"]
        page_no = user_data.get("page", None)
        page_limit = user_data.get("limit", None)
        total_page = user_data.get("total", page_limit)
        previous_page = user_data.get("previous", False)
        next_page = user_data.get("next", True)
        
        return page_no, page_limit, total_page, previous_page, next_page
    else:
        raise Exception("Failed to fetch video data")
    
def main():
    try:
      page_no, page_limit, total_page, previous_page, next_page = random_youtube_video()
      print(f"Page No: {page_no} \nPage limit: {page_limit} \nTotal page: {total_page} \nPrevious page: {previous_page} \nNext page: {next_page}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
        
        