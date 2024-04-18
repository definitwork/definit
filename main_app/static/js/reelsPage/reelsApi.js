const token = 'EAAPiBXhWiuwBO83FwrvU6ZAheolXJ65qYfySLGHY35fckEYEnGhfkFMTQEZARTLjheQmXiRJYMPwHrT7RguNFW63SwkhZBeb5FYpTTC54AeAHZCV8ZCqO4LSbxKnFPA0YWYx1TgfX8m1N0dRD4kVZCzUXeZCQHZAUyuftT8NK0wehjdtEPjZCQohKFj2I3RCL8ZAIXp7TY9hCDyBjlayJYSyz11Id6ymFQKQz8vT9zhdI8OwH6odQjLin9MwZDZD'
const fields = ['id','media_type', 'media_url']
fetch(`https://graph.facebook.com/v19.0/122135527910211368?&access_token=${token}`, {
    method: 'GET',
})
    .then(resp => resp.json())
    .then(data => console.log(data))