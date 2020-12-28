temp =  '_octo=GH1.1.1102395001.1582362358; _ga=GA1.2.454155278.1582362359; _device_id=0442b4dd494cafc0301c2ad3e9eeca31; experiment:homepage_signup_flow=eyJ2ZXJzaW9uIjoiMSIsInJvbGxPdXRQbGFjZW1lbnQiOjI1LjY3MjIzNTIyOTQ0MTk1Miwic3ViZ3JvdXAiOiJjb250cm9sIiwiY3JlYXRlZEF0IjoiMjAyMC0wMy0yNlQxNDozNToxNC45ODdaIiwidXBkYXRlZEF0IjoiMjAyMC0wMy0yNlQxNDozNToxNC45ODdaIn0=; user_session=vsC4WPrJRjDLSTC3Up0h0D5i0Knfyah9hGXzhfrchfW_5eyc; __Host-user_session_same_site=vsC4WPrJRjDLSTC3Up0h0D5i0Knfyah9hGXzhfrchfW_5eyc; logged_in=yes; dotcom_user=Zhimin7; has_recent_activity=1; tz=Asia%2FShanghai; _gh_sess=e9HSDZpXyMNlwvsRH7kjV39DisarWcGKdXqnr65Z3VfFlChN0onUNHwROBPqX2yfS9WudAE71IQF2h7TRiVQ3rvVp1KbvbmfOOkULatFZsHoVRi5UUCI%2FY8wz0QVBLXF3VY0WgLwoUoZhaJ5MhPG%2F22am%2Bowt2XigTISZm289i%2BCYxkDvWz8N7J61WTPz9i3--3YPo3PUW%2B3asHJSS--AmjAHcbcaKfU%2BneNyzA13w%3D%3D'
cookie_list = temp.split(';')
cookies = {}

for cookie in cookie_list:
    cookies[cookie.split('=')[0]] = cookie.split('=')[-1]
print(cookies)