#!/usr/bin/node
const request = require('request')

const peopleList = []
let charactersUriList = []
const id = process.argv[2]
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${id}`

request({uri: filmUrl, json: true}, (error, res) => {
		if (error) {
			console.log(error)
		} else if (res.error) {
			 console.log(res.error)
		} else {
			console.log(res.body['characters'])
			charactersUriList = res.body['characters']
		}
	})

async function getCharacter(uri){
	await request({uri: uri, json: true}, (error, res) => {
		if(error) {
			console.log(error)
		} else if (res.error) {
			console.log(res.error)
		} else {
			peopleList.push(res.body['name'])
		}
	})
}

charactersUriList.map(async (uri, _) => {
	await getCharacter(uri)
	return
})

console.log("await!",peopleList)
