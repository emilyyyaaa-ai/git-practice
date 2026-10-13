#状态码
status_code = int(input("状态响应码:"))
if status_code == 400:
    description = "Bad Request"
elif status_code == 401:
    description = "Unauthorized"   
elif status_code == 403:
    description = "Forbidden"
elif status_code == 404:
    description = "Not Fond"
elif status_code == 405:
    description = "Method Not Allowed" 
elif status_code == 418:
    description = "I am a taepot"  
elif status_code == 429:
    description = "Too many request"  
else:
    description = "Unknown status code"    
print("状态描述：",description)