const fetch = require("node-fetch");
function randomuser() {
    const users = [ ]
    fetch('https://randomuser.me/api/?results=10')
            //.then --> take response data and format
            .then((res) => {
                console.log("response came back!")
                return res.json() 
            })
            //.then --> use response JSON data
            .then((jsonData) => {
                peopleRes =  jsonData.results
                for(let i = 0; i< 10; i++) {
                firstName = peopleRes[i].name.first
                lastName = peopleRes[i].name.last
                peopleImg = peopleRes[i].picture.thumbnail
                const user = {
                    "first name": firstName,
                    "last name": lastName,
                    "picture": peopleImg
                }
                users.push(user)
                }
                console.log(users)
            })
            //.catch --> catch errors
            .catch((err) => {
                console.log(err)
                return err
            })
        }
randomuser()